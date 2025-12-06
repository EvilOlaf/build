#!/usr/bin/env python3
"""
Analyze patches and check if they might be in mainline Linux kernel.

This script analyzes patch files and generates a report with information
about each patch, making it easier to manually verify against mainline.
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


class PatchInfo:
    """Store information about a patch."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.relative_path = ""
        self.subject = ""
        self.from_commit = ""
        self.author = ""
        self.date = ""
        self.files_changed = []
        self.subsystem = ""
        
    def __repr__(self):
        return f"PatchInfo({self.filename})"


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
        
        # Determine subsystem from files
        if patch.files_changed:
            first_file = patch.files_changed[0]
            parts = first_file.split('/')
            if len(parts) > 1:
                patch.subsystem = parts[0]
            else:
                patch.subsystem = "other"
        
        return patch
        
    except Exception as e:
        print(f"Error parsing {filepath}: {e}", file=sys.stderr)
        return None


def get_all_patches(patch_dir: str) -> List[PatchInfo]:
    """Get all patch files from a directory recursively."""
    patches = []
    patch_dir_path = Path(patch_dir)
    
    for root, dirs, files in os.walk(patch_dir):
        for file in files:
            if file.endswith('.patch'):
                filepath = os.path.join(root, file)
                patch_info = parse_patch_file(filepath)
                if patch_info:
                    # Set relative path from patch_dir
                    rel_path = Path(filepath).relative_to(patch_dir_path)
                    patch_info.relative_path = str(rel_path.parent) if str(rel_path.parent) != '.' else ''
                    patches.append(patch_info)
    
    return patches


def analyze_patches(patches: List[PatchInfo]) -> Dict:
    """Analyze patches and generate statistics."""
    stats = {
        'total': len(patches),
        'by_subsystem': defaultdict(int),
        'by_directory': defaultdict(int),
        'with_commit_id': 0,
        'files_modified': defaultdict(int)
    }
    
    for patch in patches:
        # Count by subsystem
        if patch.subsystem:
            stats['by_subsystem'][patch.subsystem] += 1
        
        # Count by directory within patch dir
        if patch.relative_path:
            stats['by_directory'][patch.relative_path] += 1
        
        # Count patches with commit IDs
        if patch.from_commit:
            stats['with_commit_id'] += 1
        
        # Count files
        for file in patch.files_changed:
            stats['files_modified'][file] += 1
    
    return stats


def generate_detailed_report(patches: List[PatchInfo], output_file: str, patch_dir: str, kernel_version: str):
    """Generate a detailed report of the patches."""
    
    stats = analyze_patches(patches)
    
    with open(output_file, 'w') as f:
        f.write(f"# Patch Analysis Report: sunxi-6.16 vs Linux Kernel {kernel_version}\n\n")
        f.write(f"**Patch Directory:** `{patch_dir}`\n\n")
        f.write(f"**Analysis Date:** {get_current_date()}\n\n")
        
        # Summary
        f.write(f"## Summary\n\n")
        f.write(f"- **Total Patches Analyzed:** {stats['total']}\n")
        f.write(f"- **Patches with Commit IDs:** {stats['with_commit_id']}\n")
        f.write(f"- **Unique Files Modified:** {len(stats['files_modified'])}\n\n")
        
        # By subsystem
        if stats['by_subsystem']:
            f.write(f"## Patches by Subsystem\n\n")
            f.write(f"| Subsystem | Count |\n")
            f.write(f"|-----------|-------|\n")
            for subsystem, count in sorted(stats['by_subsystem'].items(), key=lambda x: -x[1]):
                f.write(f"| {subsystem} | {count} |\n")
            f.write(f"\n")
        
        # By directory
        if stats['by_directory']:
            f.write(f"## Patches by Directory\n\n")
            f.write(f"| Directory | Count |\n")
            f.write(f"|-----------|-------|\n")
            for directory, count in sorted(stats['by_directory'].items(), key=lambda x: -x[1]):
                f.write(f"| {directory} | {count} |\n")
            f.write(f"\n")
        
        # Most frequently modified files
        f.write(f"## Most Frequently Modified Files (Top 20)\n\n")
        f.write(f"These files are modified by multiple patches and might indicate areas of active development:\n\n")
        f.write(f"| File | Patches |\n")
        f.write(f"|------|--------|\n")
        top_files = sorted(stats['files_modified'].items(), key=lambda x: -x[1])[:20]
        for file, count in top_files:
            f.write(f"| `{file}` | {count} |\n")
        f.write(f"\n")
        
        # All patches organized by directory
        patches_by_dir = defaultdict(list)
        for patch in patches:
            key = patch.relative_path if patch.relative_path else 'root'
            patches_by_dir[key].append(patch)
        
        f.write(f"## Detailed Patch List\n\n")
        f.write(f"Complete list of all patches, organized by directory:\n\n")
        
        for directory in sorted(patches_by_dir.keys()):
            dir_patches = sorted(patches_by_dir[directory], key=lambda p: p.filename)
            
            f.write(f"### {directory} ({len(dir_patches)} patches)\n\n")
            f.write(f"| # | Patch File | Subject | Commit ID | Files Changed |\n")
            f.write(f"|---|------------|---------|-----------|---------------|\n")
            
            for i, patch in enumerate(dir_patches, 1):
                subject_short = patch.subject[:50] + "..." if len(patch.subject) > 50 else patch.subject
                subject_short = subject_short.replace('|', '\\|')  # Escape pipes in markdown
                
                commit_id = patch.from_commit[:12] if patch.from_commit else "N/A"
                
                files_str = ", ".join([f.split('/')[-1] for f in patch.files_changed[:2]])
                if len(patch.files_changed) > 2:
                    files_str += f" (+{len(patch.files_changed)-2})"
                
                f.write(f"| {i} | `{patch.filename}` | {subject_short} | `{commit_id}` | {files_str} |\n")
            
            f.write(f"\n")
        
        # Search instructions
        f.write(f"## How to Verify Patches in Mainline\n\n")
        f.write(f"To check if these patches are in Linux kernel {kernel_version}, you can:\n\n")
        f.write(f"### Method 1: Search by Commit ID\n\n")
        f.write(f"For patches with commit IDs (indicated in the table above):\n\n")
        f.write(f"```bash\n")
        f.write(f"# Clone the Linux kernel (if not already done)\n")
        f.write(f"git clone --depth=1 --branch v{kernel_version} \\\n")
        f.write(f"  https://github.com/torvalds/linux.git\n\n")
        f.write(f"cd linux\n\n")
        f.write(f"# Check if a commit exists\n")
        f.write(f"git cat-file -t <commit-id>\n")
        f.write(f"```\n\n")
        
        f.write(f"### Method 2: Search by Subject\n\n")
        f.write(f"```bash\n")
        f.write(f"# Search git log for a specific subject\n")
        f.write(f'git log --all --grep "subject line" --oneline\n')
        f.write(f"```\n\n")
        
        f.write(f"### Method 3: Use GitHub Search\n\n")
        f.write(f"1. Go to https://github.com/torvalds/linux\n")
        f.write(f"2. Search for the patch subject or modified file names\n")
        f.write(f"3. Check the commit history for the v{kernel_version} tag\n\n")
        
        f.write(f"### Method 4: Use git.kernel.org\n\n")
        f.write(f"1. Visit https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git\n")
        f.write(f"2. Use the search feature to find commits by:\n")
        f.write(f"   - Commit message (subject)\n")
        f.write(f"   - File path\n")
        f.write(f"   - Author name\n\n")
        
        # Export patch info for scripting
        f.write(f"## Patch Information Export\n\n")
        f.write(f"For automated verification, here's a list of commit IDs to check:\n\n")
        f.write(f"```\n")
        commit_ids = [p.from_commit for p in patches if p.from_commit]
        if commit_ids:
            for commit_id in sorted(set(commit_ids)):
                f.write(f"{commit_id}\n")
        else:
            f.write(f"# No commit IDs found in patches\n")
        f.write(f"```\n\n")
        
        # Additional notes
        f.write(f"## Notes\n\n")
        f.write(f"- This analysis is based on patch file metadata only\n")
        f.write(f"- Patches may have been modified when merged upstream\n")
        f.write(f"- Some patches might be split into multiple commits or combined\n")
        f.write(f"- The commit ID in a patch comes from the original source tree (e.g., vendor kernel)\n")
        f.write(f"- Manual verification is recommended for definitive confirmation\n")
    
    print(f"\nReport generated: {output_file}")


def get_current_date():
    """Get current date as a string."""
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def generate_commit_check_script(patches: List[PatchInfo], output_file: str, kernel_version: str):
    """Generate a bash script to check commits in kernel repo."""
    
    with open(output_file, 'w') as f:
        f.write(f"#!/bin/bash\n")
        f.write(f"# Script to check if sunxi-6.16 patches are in Linux kernel {kernel_version}\n")
        f.write(f"# Generated on {get_current_date()}\n\n")
        f.write(f"set -e\n\n")
        
        f.write(f"KERNEL_VERSION=\"{kernel_version}\"\n")
        f.write(f"KERNEL_DIR=\"linux-$KERNEL_VERSION\"\n\n")
        
        f.write(f"# Clone kernel if not exists\n")
        f.write(f"if [ ! -d \"$KERNEL_DIR\" ]; then\n")
        f.write(f"    echo \"Cloning Linux kernel v$KERNEL_VERSION...\"\n")
        f.write(f"    git clone --depth=1 --branch \"v$KERNEL_VERSION\" \\\n")
        f.write(f"        https://github.com/torvalds/linux.git \\\n")
        f.write(f"        \"$KERNEL_DIR\"\n")
        f.write(f"fi\n\n")
        
        f.write(f"cd \"$KERNEL_DIR\"\n\n")
        
        f.write(f"echo \"Checking patches...\"\n")
        f.write(f"echo \"\"\n\n")
        
        f.write(f"FOUND=0\n")
        f.write(f"NOT_FOUND=0\n\n")
        
        # Generate checks for patches with commit IDs
        patches_with_commits = [p for p in patches if p.from_commit]
        
        f.write(f"# Check patches by commit ID ({len(patches_with_commits)} patches)\n")
        for patch in patches_with_commits[:20]:  # Limit to first 20 for script size
            f.write(f"\n# {patch.filename}\n")
            f.write(f"# Subject: {patch.subject}\n")
            f.write(f"if git cat-file -t {patch.from_commit} >/dev/null 2>&1; then\n")
            f.write(f"    echo \"✓ FOUND: {patch.filename}\"\n")
            f.write(f"    echo \"  Commit: {patch.from_commit}\"\n")
            f.write(f"    ((FOUND++))\n")
            f.write(f"else\n")
            f.write(f"    echo \"✗ NOT FOUND: {patch.filename}\"\n")
            f.write(f"    ((NOT_FOUND++))\n")
            f.write(f"fi\n")
        
        if len(patches_with_commits) > 20:
            f.write(f"\n# ... {len(patches_with_commits) - 20} more patches with commit IDs\n")
            f.write(f"# (edit this script to check all of them)\n\n")
        
        f.write(f"\necho \"\"\n")
        f.write(f"echo \"Summary:\"\n")
        f.write(f"echo \"  Found: $FOUND\"\n")
        f.write(f"echo \"  Not found: $NOT_FOUND\"\n")
    
    # Make script executable
    os.chmod(output_file, 0o755)
    print(f"Check script generated: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze patches and generate report for mainline verification"
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
        "--output",
        default="patch_analysis_report.md",
        help="Output report file (default: patch_analysis_report.md)"
    )
    parser.add_argument(
        "--generate-script",
        default=None,
        help="Generate a bash script to check patches (default: None)"
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
    
    # Generate detailed report
    generate_detailed_report(patches, args.output, args.patch_dir, args.kernel_version)
    
    # Generate check script if requested
    if args.generate_script:
        generate_commit_check_script(patches, args.generate_script, args.kernel_version)
    
    # Print summary
    stats = analyze_patches(patches)
    print(f"\n{'='*60}")
    print(f"Analysis Complete")
    print(f"{'='*60}")
    print(f"Total patches: {stats['total']}")
    print(f"Patches with commit IDs: {stats['with_commit_id']}")
    print(f"Unique subsystems: {len(stats['by_subsystem'])}")
    print(f"Unique files modified: {len(stats['files_modified'])}")
    print(f"\nSee {args.output} for detailed report")
    print(f"{'='*60}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
