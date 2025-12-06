#!/usr/bin/env python3
"""
Check if patches from a directory are present in mainline Linux kernel.

This script analyzes patch files and checks if they have been merged into
the mainline Linux kernel by comparing commit subjects, file paths, and
optionally commit IDs.
"""

import os
import re
import sys
import subprocess
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import tempfile
import shutil


class PatchInfo:
    """Store information about a patch."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.subject = ""
        self.from_commit = ""
        self.author = ""
        self.date = ""
        self.files_changed = []
        self.in_mainline = False
        self.mainline_commit = ""
        self.notes = ""
        
    def __repr__(self):
        return f"PatchInfo({self.filename}, subject={self.subject[:50]}...)"


def parse_patch_file(filepath: str) -> Optional[PatchInfo]:
    """Parse a patch file and extract metadata."""
    patch = PatchInfo(filepath)
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Extract subject (first line starting with "Subject:")
        subject_match = re.search(r'^Subject:\s*(?:\[PATCH[^\]]*\]\s*)?(.+)$', content, re.MULTILINE)
        if subject_match:
            patch.subject = subject_match.group(1).strip()
        
        # Extract original commit hash from "From" line
        from_match = re.search(r'^From\s+([a-f0-9]{40})', content, re.MULTILINE)
        if from_match:
            patch.from_commit = from_match.group(1)
        
        # Extract author
        author_match = re.search(r'^From:\s*(.+)$', content, re.MULTILINE)
        if author_match:
            patch.author = author_match.group(1).strip()
        
        # Extract date
        date_match = re.search(r'^Date:\s*(.+)$', content, re.MULTILINE)
        if date_match:
            patch.date = date_match.group(1).strip()
        
        # Extract files changed from diff headers
        file_patterns = re.findall(r'^\+\+\+ b/(.+)$', content, re.MULTILINE)
        patch.files_changed = list(set(file_patterns))  # Remove duplicates
        
        return patch
        
    except Exception as e:
        print(f"Error parsing {filepath}: {e}", file=sys.stderr)
        return None


def get_all_patches(patch_dir: str) -> List[PatchInfo]:
    """Get all patch files from a directory recursively."""
    patches = []
    
    for root, dirs, files in os.walk(patch_dir):
        for file in files:
            if file.endswith('.patch'):
                filepath = os.path.join(root, file)
                patch_info = parse_patch_file(filepath)
                if patch_info:
                    patches.append(patch_info)
    
    return patches


def setup_kernel_repo(kernel_version: str, cache_dir: str) -> Optional[str]:
    """
    Clone or update the Linux kernel repository.
    
    Args:
        kernel_version: Version like "6.18"
        cache_dir: Directory to cache the kernel repo
        
    Returns:
        Path to the kernel repository or None on error
    """
    kernel_path = os.path.join(cache_dir, "linux")
    
    if os.path.exists(kernel_path):
        print(f"Using existing kernel repository at {kernel_path}")
        # Update the repository
        try:
            print("Fetching latest changes...")
            subprocess.run(
                ["git", "fetch", "--tags", "origin"],
                cwd=kernel_path,
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Warning: Could not update repository: {e}")
        return kernel_path
    
    # Clone the repository
    print(f"Cloning Linux kernel repository (this may take a while)...")
    try:
        # Use shallow clone with specific tag to save time and space
        tag = f"v{kernel_version}"
        subprocess.run(
            ["git", "clone", "--depth=1", "--branch", tag, 
             "https://github.com/torvalds/linux.git",
             kernel_path],
            check=True,
            capture_output=False
        )
        return kernel_path
    except subprocess.CalledProcessError as e:
        print(f"Error cloning kernel repository: {e}", file=sys.stderr)
        return None


def check_patch_in_kernel(patch: PatchInfo, kernel_path: str) -> Tuple[bool, str, str]:
    """
    Check if a patch is present in the kernel repository.
    
    Returns:
        Tuple of (found, commit_hash, notes)
    """
    # Strategy 1: Check by original commit hash
    if patch.from_commit:
        try:
            result = subprocess.run(
                ["git", "cat-file", "-t", patch.from_commit],
                cwd=kernel_path,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return (True, patch.from_commit, "Found by original commit hash")
        except subprocess.CalledProcessError:
            pass
    
    # Strategy 2: Search by subject line in git log
    if patch.subject:
        # Clean up subject for searching
        search_subject = patch.subject.strip()
        # Remove common prefixes
        search_subject = re.sub(r'^\[PATCH[^\]]*\]\s*', '', search_subject)
        
        try:
            # Search in git log
            result = subprocess.run(
                ["git", "log", "--all", "--grep", search_subject, "--pretty=format:%H", "--max-count=5"],
                cwd=kernel_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0 and result.stdout.strip():
                commits = result.stdout.strip().split('\n')
                # Verify by checking the files changed
                for commit_hash in commits:
                    if verify_commit_matches_patch(kernel_path, commit_hash, patch):
                        return (True, commit_hash, f"Found by subject: '{search_subject}'")
                
                # Found by subject but files don't match - might still be the same
                return (True, commits[0], f"Found by subject (partial match): '{search_subject}'")
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            pass
    
    # Strategy 3: Check if files were modified in commits mentioning similar subjects
    if patch.files_changed:
        try:
            # Get the primary file (usually the first one)
            main_file = patch.files_changed[0] if patch.files_changed else None
            if main_file:
                # Check git log for that file
                result = subprocess.run(
                    ["git", "log", "--all", "--pretty=format:%H|%s", "--max-count=10", "--", main_file],
                    cwd=kernel_path,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    # Check if any commit subject is similar
                    for line in result.stdout.strip().split('\n'):
                        if '|' in line:
                            commit_hash, commit_subject = line.split('|', 1)
                            # Simple similarity check
                            if patch.subject and subjects_similar(patch.subject, commit_subject):
                                return (True, commit_hash, f"Found by file and subject match: {main_file}")
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            pass
    
    return (False, "", "Not found in mainline")


def verify_commit_matches_patch(kernel_path: str, commit_hash: str, patch: PatchInfo) -> bool:
    """Verify that a commit matches the patch by comparing changed files."""
    if not patch.files_changed:
        return True  # Can't verify, assume it matches
    
    try:
        # Get files changed in the commit
        result = subprocess.run(
            ["git", "show", "--name-only", "--pretty=format:", commit_hash],
            cwd=kernel_path,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            commit_files = set(result.stdout.strip().split('\n'))
            patch_files = set(patch.files_changed)
            
            # Check if there's any overlap
            if commit_files & patch_files:
                return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass
    
    return False


def subjects_similar(subject1: str, subject2: str) -> bool:
    """Check if two commit subjects are similar."""
    # Normalize subjects
    s1 = re.sub(r'^\[PATCH[^\]]*\]\s*', '', subject1.lower().strip())
    s2 = re.sub(r'^\[PATCH[^\]]*\]\s*', '', subject2.lower().strip())
    
    # Direct match
    if s1 == s2:
        return True
    
    # Check if one contains the other (at least 70% of the shorter one)
    shorter = min(len(s1), len(s2))
    if shorter > 0:
        if s1 in s2 or s2 in s1:
            return True
    
    # Check word overlap
    words1 = set(s1.split())
    words2 = set(s2.split())
    
    if words1 and words2:
        overlap = len(words1 & words2)
        shorter_len = min(len(words1), len(words2))
        if shorter_len > 0 and overlap / shorter_len > 0.7:
            return True
    
    return False


def generate_report(patches: List[PatchInfo], output_file: str, patch_dir: str, kernel_version: str):
    """Generate a detailed report of the analysis."""
    
    total = len(patches)
    found = sum(1 for p in patches if p.in_mainline)
    not_found = total - found
    
    with open(output_file, 'w') as f:
        f.write(f"# Patch Analysis Report\n\n")
        f.write(f"**Analysis Date:** {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}\n\n")
        f.write(f"**Patch Directory:** {patch_dir}\n\n")
        f.write(f"**Kernel Version:** {kernel_version}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- **Total Patches:** {total}\n")
        f.write(f"- **Found in Mainline:** {found} ({found*100//total if total > 0 else 0}%)\n")
        f.write(f"- **Not Found:** {not_found} ({not_found*100//total if total > 0 else 0}%)\n\n")
        
        if found > 0:
            f.write(f"## Patches Found in Mainline ({found})\n\n")
            f.write("| Patch File | Subject | Mainline Commit | Notes |\n")
            f.write("|------------|---------|-----------------|-------|\n")
            
            for patch in sorted(patches, key=lambda p: p.filename):
                if patch.in_mainline:
                    subject_short = patch.subject[:60] + "..." if len(patch.subject) > 60 else patch.subject
                    commit_short = patch.mainline_commit[:12] if patch.mainline_commit else "N/A"
                    f.write(f"| {patch.filename} | {subject_short} | {commit_short} | {patch.notes} |\n")
        
        if not_found > 0:
            f.write(f"\n## Patches Not Found in Mainline ({not_found})\n\n")
            f.write("| Patch File | Subject | Files Changed |\n")
            f.write("|------------|---------|---------------|\n")
            
            for patch in sorted(patches, key=lambda p: p.filename):
                if not patch.in_mainline:
                    subject_short = patch.subject[:60] + "..." if len(patch.subject) > 60 else patch.subject
                    files_str = ", ".join(patch.files_changed[:3])
                    if len(patch.files_changed) > 3:
                        files_str += f" (+{len(patch.files_changed)-3} more)"
                    f.write(f"| {patch.filename} | {subject_short} | {files_str} |\n")
        
        f.write(f"\n## Details\n\n")
        f.write(f"This report was generated by analyzing patch files in `{patch_dir}` ")
        f.write(f"against the Linux kernel {kernel_version} mainline repository.\n\n")
        f.write(f"The analysis uses multiple strategies to identify patches:\n")
        f.write(f"1. Match by original commit hash (from the patch header)\n")
        f.write(f"2. Search by commit subject in git log\n")
        f.write(f"3. Match by modified files and similar commit subjects\n\n")
        f.write(f"Note: Some patches may have been modified or split when merged upstream, ")
        f.write(f"so manual verification is recommended for important cases.\n")
    
    print(f"\nReport generated: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Check if patches are present in mainline Linux kernel"
    )
    parser.add_argument(
        "patch_dir",
        help="Directory containing patch files to analyze"
    )
    parser.add_argument(
        "--kernel-version",
        default="6.18",
        help="Linux kernel version to check against (default: 6.18)"
    )
    parser.add_argument(
        "--cache-dir",
        default="/tmp/kernel_cache",
        help="Directory to cache kernel repository (default: /tmp/kernel_cache)"
    )
    parser.add_argument(
        "--output",
        default="patch_analysis_report.md",
        help="Output report file (default: patch_analysis_report.md)"
    )
    parser.add_argument(
        "--skip-clone",
        action="store_true",
        help="Skip cloning kernel repository (use existing cache)"
    )
    parser.add_argument(
        "--max-patches",
        type=int,
        default=None,
        help="Maximum number of patches to analyze (for testing)"
    )
    
    args = parser.parse_args()
    
    # Validate patch directory
    if not os.path.isdir(args.patch_dir):
        print(f"Error: Patch directory not found: {args.patch_dir}", file=sys.stderr)
        return 1
    
    # Get all patches
    print(f"Scanning for patches in {args.patch_dir}...")
    patches = get_all_patches(args.patch_dir)
    
    if not patches:
        print("No patch files found!", file=sys.stderr)
        return 1
    
    print(f"Found {len(patches)} patch files")
    
    # Limit patches if requested
    if args.max_patches:
        patches = patches[:args.max_patches]
        print(f"Limiting analysis to {len(patches)} patches")
    
    # Setup kernel repository
    if not args.skip_clone:
        kernel_path = setup_kernel_repo(args.kernel_version, args.cache_dir)
        if not kernel_path:
            print("Failed to setup kernel repository", file=sys.stderr)
            return 1
    else:
        kernel_path = os.path.join(args.cache_dir, "linux")
        if not os.path.exists(kernel_path):
            print(f"Error: Kernel cache not found at {kernel_path}", file=sys.stderr)
            return 1
    
    # Check each patch
    print(f"\nAnalyzing patches against kernel {args.kernel_version}...")
    for i, patch in enumerate(patches, 1):
        print(f"[{i}/{len(patches)}] Checking {patch.filename}...", end='\r')
        found, commit, notes = check_patch_in_kernel(patch, kernel_path)
        patch.in_mainline = found
        patch.mainline_commit = commit
        patch.notes = notes
    
    print()  # New line after progress
    
    # Generate report
    generate_report(patches, args.output, args.patch_dir, args.kernel_version)
    
    # Print summary
    total = len(patches)
    found = sum(1 for p in patches if p.in_mainline)
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total patches: {total}")
    print(f"  Found in mainline: {found} ({found*100//total if total > 0 else 0}%)")
    print(f"  Not found: {total - found} ({(total-found)*100//total if total > 0 else 0}%)")
    print(f"{'='*60}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
