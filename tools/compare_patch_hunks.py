#!/usr/bin/env python3
"""
Compare patch hunks against Linux kernel mainline.

This script breaks down patches into individual hunks and searches for
matching code in the Linux kernel to determine which changes are present.
"""

import os
import re
import sys
import subprocess
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import hashlib


@dataclass
class Hunk:
    """Represents a single hunk (chunk) from a patch."""
    patch_file: str
    file_path: str
    hunk_number: int
    old_start: int
    old_count: int
    new_start: int
    new_count: int
    header: str
    lines: List[str]
    added_lines: List[str]
    removed_lines: List[str]
    context_lines: List[str]
    
    def get_signature(self) -> str:
        """Generate a signature for this hunk based on added content."""
        # Create signature from non-whitespace added lines
        content = []
        for line in self.added_lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('//') and not stripped.startswith('/*'):
                content.append(stripped)
        return '\n'.join(content)
    
    def get_search_patterns(self) -> List[str]:
        """Extract meaningful search patterns from added lines."""
        patterns = []
        for line in self.added_lines:
            stripped = line.strip()
            # Skip empty lines, comments, and very short lines
            if len(stripped) < 10:
                continue
            if stripped.startswith('//') or stripped.startswith('/*') or stripped.startswith('*'):
                continue
            # Extract function names, variable declarations, etc.
            patterns.append(stripped)
        return patterns[:5]  # Return top 5 patterns


def parse_patch_into_hunks(patch_file: str) -> List[Hunk]:
    """Parse a patch file and extract all hunks."""
    hunks = []
    
    try:
        with open(patch_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {patch_file}: {e}", file=sys.stderr)
        return hunks
    
    # Split by file sections (starting with "diff --git" or "--- a/" or "+++ b/")
    current_file = None
    current_hunk_lines = []
    current_hunk_header = None
    hunk_count = 0
    in_hunk = False
    
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Detect new file
        if line.startswith('+++ b/'):
            current_file = line[6:].strip()
            i += 1
            continue
        
        # Detect hunk header
        hunk_match = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(.*)$', line)
        if hunk_match:
            # Save previous hunk if exists
            if in_hunk and current_hunk_lines:
                hunk = create_hunk_from_lines(
                    patch_file, current_file, hunk_count,
                    current_hunk_header, current_hunk_lines
                )
                if hunk:
                    hunks.append(hunk)
            
            # Start new hunk
            hunk_count += 1
            current_hunk_header = line
            current_hunk_lines = []
            in_hunk = True
            i += 1
            continue
        
        # Collect hunk lines
        if in_hunk:
            if line.startswith('diff --git') or line.startswith('--- a/'):
                # End of current hunk, start of new file
                if current_hunk_lines:
                    hunk = create_hunk_from_lines(
                        patch_file, current_file, hunk_count,
                        current_hunk_header, current_hunk_lines
                    )
                    if hunk:
                        hunks.append(hunk)
                in_hunk = False
                current_hunk_lines = []
            elif line.startswith('+') or line.startswith('-') or line.startswith(' '):
                current_hunk_lines.append(line)
        
        i += 1
    
    # Save last hunk
    if in_hunk and current_hunk_lines:
        hunk = create_hunk_from_lines(
            patch_file, current_file, hunk_count,
            current_hunk_header, current_hunk_lines
        )
        if hunk:
            hunks.append(hunk)
    
    return hunks


def create_hunk_from_lines(patch_file: str, file_path: str, hunk_number: int,
                           header: str, lines: List[str]) -> Optional[Hunk]:
    """Create a Hunk object from parsed lines."""
    if not header or not file_path:
        return None
    
    # Parse hunk header
    hunk_match = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(.*)$', header)
    if not hunk_match:
        return None
    
    old_start = int(hunk_match.group(1))
    old_count = int(hunk_match.group(2)) if hunk_match.group(2) else 1
    new_start = int(hunk_match.group(3))
    new_count = int(hunk_match.group(4)) if hunk_match.group(4) else 1
    
    # Categorize lines
    added_lines = []
    removed_lines = []
    context_lines = []
    
    for line in lines:
        if line.startswith('+'):
            added_lines.append(line[1:])
        elif line.startswith('-'):
            removed_lines.append(line[1:])
        elif line.startswith(' '):
            context_lines.append(line[1:])
    
    return Hunk(
        patch_file=os.path.basename(patch_file),
        file_path=file_path,
        hunk_number=hunk_number,
        old_start=old_start,
        old_count=old_count,
        new_start=new_start,
        new_count=new_count,
        header=header,
        lines=lines,
        added_lines=added_lines,
        removed_lines=removed_lines,
        context_lines=context_lines
    )


def check_hunk_in_kernel(hunk: Hunk, kernel_path: str) -> Tuple[bool, str]:
    """Check if a hunk's changes are present in the kernel."""
    if not hunk.file_path or not hunk.added_lines:
        return False, "No file path or no added lines"
    
    # Check if the file exists in the kernel
    kernel_file = os.path.join(kernel_path, hunk.file_path)
    if not os.path.exists(kernel_file):
        return False, f"File {hunk.file_path} not found in kernel"
    
    try:
        with open(kernel_file, 'r', encoding='utf-8', errors='ignore') as f:
            kernel_content = f.read()
    except Exception as e:
        return False, f"Error reading kernel file: {e}"
    
    # Search for added lines in the kernel file
    found_lines = 0
    total_meaningful_lines = 0
    
    for line in hunk.added_lines:
        stripped = line.strip()
        # Skip empty lines and very short lines
        if len(stripped) < 5:
            continue
        # Skip comments
        if stripped.startswith('//') or stripped.startswith('/*') or stripped.startswith('*'):
            continue
        
        total_meaningful_lines += 1
        
        # Search for this line in kernel content
        if stripped in kernel_content:
            found_lines += 1
    
    if total_meaningful_lines == 0:
        return False, "No meaningful lines to check"
    
    # Consider it found if at least 70% of meaningful lines are present
    match_ratio = found_lines / total_meaningful_lines
    if match_ratio >= 0.7:
        return True, f"Found {found_lines}/{total_meaningful_lines} lines ({match_ratio*100:.0f}%)"
    else:
        return False, f"Only {found_lines}/{total_meaningful_lines} lines found ({match_ratio*100:.0f}%)"


def setup_kernel_repo(kernel_version: str, cache_dir: str) -> Optional[str]:
    """Clone or use cached Linux kernel repository."""
    kernel_path = os.path.join(cache_dir, "linux")
    
    if os.path.exists(kernel_path):
        print(f"Using existing kernel repository at {kernel_path}")
        return kernel_path
    
    print(f"Cloning Linux kernel v{kernel_version} (this will take some time)...")
    try:
        subprocess.run(
            ["git", "clone", "--depth=1", "--branch", f"v{kernel_version}",
             "https://github.com/torvalds/linux.git", kernel_path],
            check=True,
            capture_output=True
        )
        print(f"Kernel cloned successfully to {kernel_path}")
        return kernel_path
    except subprocess.CalledProcessError as e:
        print(f"Error cloning kernel: {e}", file=sys.stderr)
        return None


def generate_hunk_report(hunks: List[Hunk], output_file: str, kernel_version: str):
    """Generate a detailed report of hunk analysis."""
    
    total_hunks = len(hunks)
    found_hunks = sum(1 for h in hunks if hasattr(h, 'found') and h.found)
    
    # Group by patch file
    hunks_by_patch = {}
    for hunk in hunks:
        if hunk.patch_file not in hunks_by_patch:
            hunks_by_patch[hunk.patch_file] = []
        hunks_by_patch[hunk.patch_file].append(hunk)
    
    with open(output_file, 'w') as f:
        f.write(f"# Hunk-Level Analysis: sunxi-6.16 vs Linux Kernel {kernel_version}\n\n")
        f.write(f"**Analysis Date:** {get_current_date()}\n\n")
        
        f.write(f"## Summary\n\n")
        f.write(f"- **Total Hunks:** {total_hunks}\n")
        f.write(f"- **Found in Kernel:** {found_hunks} ({found_hunks*100//total_hunks if total_hunks > 0 else 0}%)\n")
        f.write(f"- **Not Found:** {total_hunks - found_hunks} ({(total_hunks-found_hunks)*100//total_hunks if total_hunks > 0 else 0}%)\n")
        f.write(f"- **Patches Analyzed:** {len(hunks_by_patch)}\n\n")
        
        # Statistics by file
        files_with_found_hunks = {}
        for hunk in hunks:
            if hasattr(hunk, 'found') and hunk.found:
                files_with_found_hunks[hunk.file_path] = files_with_found_hunks.get(hunk.file_path, 0) + 1
        
        if files_with_found_hunks:
            f.write(f"## Files with Found Hunks (Top 20)\n\n")
            f.write(f"| File | Found Hunks |\n")
            f.write(f"|------|-------------|\n")
            for file_path, count in sorted(files_with_found_hunks.items(), key=lambda x: -x[1])[:20]:
                f.write(f"| `{file_path}` | {count} |\n")
            f.write(f"\n")
        
        # List found hunks
        if found_hunks > 0:
            f.write(f"## Found Hunks ({found_hunks})\n\n")
            f.write(f"Hunks whose changes appear to be present in Linux kernel {kernel_version}:\n\n")
            f.write(f"| Patch File | File | Hunk | Lines | Match | Notes |\n")
            f.write(f"|------------|------|------|-------|-------|-------|\n")
            
            for patch_file in sorted(hunks_by_patch.keys()):
                for hunk in hunks_by_patch[patch_file]:
                    if hasattr(hunk, 'found') and hunk.found:
                        notes = getattr(hunk, 'notes', '')
                        f.write(f"| {hunk.patch_file} | `{hunk.file_path}` | #{hunk.hunk_number} | "
                               f"+{len(hunk.added_lines)}/-{len(hunk.removed_lines)} | "
                               f"✓ | {notes} |\n")
            f.write(f"\n")
        
        # List not found hunks (sample)
        not_found_hunks = [h for h in hunks if not (hasattr(h, 'found') and h.found)]
        if not_found_hunks:
            f.write(f"## Not Found Hunks (Sample - First 50)\n\n")
            f.write(f"| Patch File | File | Hunk | Lines | Notes |\n")
            f.write(f"|------------|------|------|-------|-------|\n")
            
            for hunk in not_found_hunks[:50]:
                notes = getattr(hunk, 'notes', 'Not found')
                f.write(f"| {hunk.patch_file} | `{hunk.file_path}` | #{hunk.hunk_number} | "
                       f"+{len(hunk.added_lines)}/-{len(hunk.removed_lines)} | {notes} |\n")
            
            if len(not_found_hunks) > 50:
                f.write(f"\n*... and {len(not_found_hunks) - 50} more hunks not found*\n")
            f.write(f"\n")
        
        # Summary by patch
        f.write(f"## Summary by Patch File\n\n")
        f.write(f"| Patch File | Total Hunks | Found | Not Found | Match % |\n")
        f.write(f"|------------|-------------|-------|-----------|----------|\n")
        
        for patch_file in sorted(hunks_by_patch.keys()):
            patch_hunks = hunks_by_patch[patch_file]
            total = len(patch_hunks)
            found = sum(1 for h in patch_hunks if hasattr(h, 'found') and h.found)
            not_found = total - found
            match_pct = (found * 100 // total) if total > 0 else 0
            
            f.write(f"| {patch_file} | {total} | {found} | {not_found} | {match_pct}% |\n")
        
        f.write(f"\n")
        f.write(f"## Methodology\n\n")
        f.write(f"This analysis breaks down each patch into individual hunks (chunks of changes) ")
        f.write(f"and checks if the added code appears in the corresponding file in Linux kernel {kernel_version}.\n\n")
        f.write(f"A hunk is considered \"found\" if at least 70% of its meaningful added lines ")
        f.write(f"(excluding empty lines and comments) are present in the kernel file.\n\n")
        f.write(f"**Note:** This is a content-based search and may not detect:\n")
        f.write(f"- Code that was modified during upstreaming\n")
        f.write(f"- Code in different files (refactored/moved)\n")
        f.write(f"- Functionally equivalent but differently written code\n")


def get_current_date():
    """Get current date as a string."""
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    parser = argparse.ArgumentParser(
        description="Compare patch hunks against Linux kernel mainline"
    )
    parser.add_argument(
        "patch_dir",
        help="Directory containing patch files"
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
        default="hunk_analysis_report.md",
        help="Output report file (default: hunk_analysis_report.md)"
    )
    parser.add_argument(
        "--max-patches",
        type=int,
        help="Maximum number of patches to analyze (for testing)"
    )
    
    args = parser.parse_args()
    
    # Validate patch directory
    if not os.path.isdir(args.patch_dir):
        print(f"Error: Patch directory not found: {args.patch_dir}", file=sys.stderr)
        return 1
    
    # Get all patch files
    print(f"Scanning for patches in {args.patch_dir}...")
    patch_files = []
    for root, dirs, files in os.walk(args.patch_dir):
        for file in files:
            if file.endswith('.patch'):
                patch_files.append(os.path.join(root, file))
    
    if not patch_files:
        print("No patch files found!", file=sys.stderr)
        return 1
    
    if args.max_patches:
        patch_files = patch_files[:args.max_patches]
    
    print(f"Found {len(patch_files)} patch files")
    
    # Parse all patches into hunks
    print(f"Parsing patches into hunks...")
    all_hunks = []
    for i, patch_file in enumerate(patch_files, 1):
        print(f"[{i}/{len(patch_files)}] Parsing {os.path.basename(patch_file)}...", end='\r')
        hunks = parse_patch_into_hunks(patch_file)
        all_hunks.extend(hunks)
    
    print()
    print(f"Extracted {len(all_hunks)} hunks from {len(patch_files)} patches")
    
    # Setup kernel repository
    print(f"\nSetting up Linux kernel {args.kernel_version}...")
    kernel_path = setup_kernel_repo(args.kernel_version, args.cache_dir)
    if not kernel_path:
        print("Failed to setup kernel repository", file=sys.stderr)
        return 1
    
    # Check each hunk
    print(f"\nChecking hunks against kernel {args.kernel_version}...")
    for i, hunk in enumerate(all_hunks, 1):
        print(f"[{i}/{len(all_hunks)}] Checking hunk {hunk.hunk_number} from {hunk.patch_file}...", end='\r')
        found, notes = check_hunk_in_kernel(hunk, kernel_path)
        hunk.found = found
        hunk.notes = notes
    
    print()
    
    # Generate report
    generate_hunk_report(all_hunks, args.output, args.kernel_version)
    
    # Print summary
    total = len(all_hunks)
    found = sum(1 for h in all_hunks if h.found)
    print(f"\n{'='*70}")
    print(f"Analysis Complete")
    print(f"{'='*70}")
    print(f"Total hunks analyzed: {total}")
    print(f"Hunks found in kernel: {found} ({found*100//total if total > 0 else 0}%)")
    print(f"Hunks not found: {total - found} ({(total-found)*100//total if total > 0 else 0}%)")
    print(f"\nDetailed report: {args.output}")
    print(f"{'='*70}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
