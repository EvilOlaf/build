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
    patch_dir: str  # Directory where the patch is located (e.g., patches.megous)
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
    
    # Extract directory from patch file path
    patch_dir = os.path.basename(os.path.dirname(patch_file))
    if not patch_dir or patch_dir == 'archive':
        # Handle edge cases
        patch_dir = "unknown"
    
    return Hunk(
        patch_file=os.path.basename(patch_file),
        patch_dir=patch_dir,
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
    """
    Check if a hunk's changes are present in the kernel with context validation.
    
    This function checks if the hunk would apply (i.e., the lines are NOT already there),
    or if the hunk is already applied (lines are there with correct context).
    Since the patchset applies cleanly to 6.18, we expect hunks to NOT be found.
    """
    if not hunk.file_path:
        return False, "No file path"
    
    # Check if the file exists in the kernel
    kernel_file = os.path.join(kernel_path, hunk.file_path)
    if not os.path.exists(kernel_file):
        return False, f"File {hunk.file_path} not found in kernel"
    
    try:
        with open(kernel_file, 'r', encoding='utf-8', errors='ignore') as f:
            kernel_lines = f.readlines()
    except Exception as e:
        return False, f"Error reading kernel file: {e}"
    
    # Strategy 1: Check if the hunk would apply cleanly (reverse check)
    # If patch adds lines, those lines should NOT be in the file at the expected location
    # If we find context lines but not the added lines, the patch still needs to be applied
    
    # Strategy 2: Check if the patch is already applied
    # Look for sequences that match the "after" state (context + added lines)
    
    # Build the "after" state - what the file should look like after the patch
    after_pattern = []
    for line in hunk.lines:
        if line.startswith('+'):
            after_pattern.append(line[1:])  # Added line
        elif line.startswith(' '):
            after_pattern.append(line[1:])  # Context line
        # Skip removed lines (they shouldn't be in the "after" state)
    
    # Build the "before" state - what the file should look like before the patch
    before_pattern = []
    for line in hunk.lines:
        if line.startswith('-'):
            before_pattern.append(line[1:])  # Removed line
        elif line.startswith(' '):
            before_pattern.append(line[1:])  # Context line
        # Skip added lines (they shouldn't be in the "before" state)
    
    # Check if we can find the "after" pattern (patch already applied)
    if after_pattern and len(after_pattern) >= 3:  # Need at least 3 lines for meaningful match
        if find_pattern_in_lines(after_pattern, kernel_lines):
            return True, "Patch appears to be already applied (found after-state with context)"
    
    # Check if we can find the "before" pattern (patch not yet applied)
    if before_pattern and len(before_pattern) >= 3:
        if find_pattern_in_lines(before_pattern, kernel_lines):
            return False, "Patch not applied (found before-state, patch still needed)"
    
    # If we have very few context lines, fall back to simpler check
    if len(hunk.context_lines) < 2:
        # For hunks with minimal context, check if added lines exist anywhere
        # But this is unreliable, so mark as uncertain
        if hunk.added_lines:
            found = any(line.strip() in ''.join(kernel_lines) for line in hunk.added_lines if line.strip())
            if found:
                return True, "Added lines found (uncertain - minimal context)"
        return False, "Insufficient context for reliable check"
    
    return False, "Could not determine patch state reliably"


def find_pattern_in_lines(pattern: List[str], lines: List[str]) -> bool:
    """
    Find a pattern of consecutive lines in a list of lines.
    Returns True if the pattern is found as a consecutive sequence.
    """
    if not pattern or not lines:
        return False
    
    pattern_len = len(pattern)
    
    # Try to find the pattern starting at each position in lines
    for i in range(len(lines) - pattern_len + 1):
        # Check if pattern matches at position i
        match = True
        for j, pattern_line in enumerate(pattern):
            # Compare with some tolerance for whitespace
            if lines[i + j].strip() != pattern_line.strip():
                match = False
                break
        
        if match:
            return True
    
    return False


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


def generate_hunk_report(hunks: List[Hunk], output_file: str, kernel_version: str, 
                         enabled_count: int = None, disabled_count: int = None):
    """Generate a detailed report of hunk analysis."""
    
    total_hunks = len(hunks)
    found_hunks = sum(1 for h in hunks if hasattr(h, 'found') and h.found)
    
    # Group by patch file
    hunks_by_patch = {}
    for hunk in hunks:
        if hunk.patch_file not in hunks_by_patch:
            hunks_by_patch[hunk.patch_file] = []
        hunks_by_patch[hunk.patch_file].append(hunk)
    
    # Group by directory
    hunks_by_dir = {}
    patches_by_dir = {}
    for hunk in hunks:
        if hunk.patch_dir not in hunks_by_dir:
            hunks_by_dir[hunk.patch_dir] = []
            patches_by_dir[hunk.patch_dir] = set()
        hunks_by_dir[hunk.patch_dir].append(hunk)
        patches_by_dir[hunk.patch_dir].add(hunk.patch_file)
    
    with open(output_file, 'w') as f:
        f.write(f"# Hunk-Level Analysis: sunxi vs Linux Kernel {kernel_version}\n\n")
        f.write(f"**Analysis Date:** {get_current_date()}\n\n")
        
        f.write(f"## Summary\n\n")
        f.write(f"- **Total Hunks:** {total_hunks}\n")
        f.write(f"- **Found in Kernel:** {found_hunks} ({found_hunks*100//total_hunks if total_hunks > 0 else 0}%)\n")
        f.write(f"- **Not Found:** {total_hunks - found_hunks} ({(total_hunks-found_hunks)*100//total_hunks if total_hunks > 0 else 0}%)\n")
        f.write(f"- **Patches Analyzed:** {len(hunks_by_patch)}\n")
        if enabled_count is not None and disabled_count is not None:
            f.write(f"- **Patches Enabled:** {enabled_count}\n")
            f.write(f"- **Patches Disabled:** {disabled_count}\n")
        f.write(f"\n")
        
        # Statistics by directory
        f.write(f"## Patches by Directory\n\n")
        f.write(f"| Directory | Patches | Hunks | Found | Not Found | Found % |\n")
        f.write(f"|-----------|---------|-------|-------|-----------|----------|\n")
        for dir_name in sorted(hunks_by_dir.keys()):
            dir_hunks = hunks_by_dir[dir_name]
            dir_patches = len(patches_by_dir[dir_name])
            dir_total = len(dir_hunks)
            dir_found = sum(1 for h in dir_hunks if hasattr(h, 'found') and h.found)
            dir_not_found = dir_total - dir_found
            dir_found_pct = (dir_found * 100 // dir_total) if dir_total > 0 else 0
            f.write(f"| {dir_name} | {dir_patches} | {dir_total} | {dir_found} | {dir_not_found} | {dir_found_pct}% |\n")
        f.write(f"\n")
        
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
        f.write(f"and checks if the hunks are already applied in Linux kernel {kernel_version}.\n\n")
        f.write(f"**Context-Based Matching:**\n")
        f.write(f"- Each hunk includes context lines (unchanged lines) and added/removed lines\n")
        f.write(f"- The tool builds the expected \"after\" state (context + added lines)\n")
        f.write(f"- If this pattern is found as a consecutive sequence in the kernel file, the hunk is considered \"found\"\n")
        f.write(f"- This ensures that lines are found in the correct location with proper context\n\n")
        f.write(f"**Disabled Patches:**\n")
        if disabled_count and disabled_count > 0:
            f.write(f"- {disabled_count} patches were disabled in series.conf (marked with '-' prefix)\n")
            f.write(f"- Only {enabled_count} enabled patches were analyzed\n\n")
        else:
            f.write(f"- All patches in the directory were analyzed\n\n")
        f.write(f"**Expected Result:**\n")
        f.write(f"- If the patchset applies cleanly to kernel {kernel_version}, most hunks should NOT be found\n")
        f.write(f"- Found hunks indicate changes that are already in the mainline kernel\n")
        f.write(f"- Disabled patches are excluded from analysis\n\n")
        f.write(f"**Limitations:**\n")
        f.write(f"- Cannot detect code that was modified during upstreaming\n")
        f.write(f"- Cannot detect code in different files (refactored/moved)\n")
        f.write(f"- Cannot detect functionally equivalent but differently written code\n")
        f.write(f"- Requires at least 3 lines of context for reliable matching\n")


def parse_series_conf(patch_dir: str) -> set:
    """
    Parse series.conf file to get list of enabled patches.
    Patches prefixed with '-' are disabled and should be excluded.
    Returns a set of enabled patch filenames (without directory path).
    """
    series_conf = os.path.join(patch_dir, "series.conf")
    
    if not os.path.exists(series_conf):
        print(f"Warning: series.conf not found in {patch_dir}")
        return None
    
    enabled_patches = set()
    disabled_patches = set()
    
    try:
        with open(series_conf, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # Skip comments and empty lines
                if not line or line.startswith('#'):
                    continue
                
                # Check if patch is disabled
                if line.startswith('-'):
                    # Disabled patch
                    patch_path = line[1:].strip()
                    # Extract just the filename
                    patch_file = os.path.basename(patch_path)
                    disabled_patches.add(patch_file)
                else:
                    # Enabled patch
                    patch_path = line.strip()
                    # Extract just the filename
                    patch_file = os.path.basename(patch_path)
                    enabled_patches.add(patch_file)
    
    except Exception as e:
        print(f"Warning: Error parsing series.conf: {e}")
        return None
    
    if disabled_patches:
        print(f"Found {len(disabled_patches)} disabled patches in series.conf")
    
    return enabled_patches, disabled_patches


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
    parser.add_argument(
        "--only-disabled",
        action="store_true",
        help="Analyze only disabled patches (those marked with '-' in series.conf)"
    )
    
    args = parser.parse_args()
    
    # Validate patch directory
    if not os.path.isdir(args.patch_dir):
        print(f"Error: Patch directory not found: {args.patch_dir}", file=sys.stderr)
        return 1
    
    # Parse series.conf to get enabled/disabled patches
    series_result = parse_series_conf(args.patch_dir)
    if series_result:
        enabled_patches, disabled_patches = series_result
        print(f"Series.conf: {len(enabled_patches)} enabled, {len(disabled_patches)} disabled patches")
    else:
        enabled_patches = None
        disabled_patches = set()
    
    # Determine which patches to analyze based on --only-disabled flag
    if args.only_disabled:
        print(f"\n** Analyzing ONLY DISABLED patches **\n")
        target_patches = disabled_patches
    else:
        target_patches = enabled_patches
    
    # Get all patch files
    print(f"Scanning for patches in {args.patch_dir}...")
    patch_files = []
    all_patch_files = []
    for root, dirs, files in os.walk(args.patch_dir):
        for file in files:
            if file.endswith('.patch'):
                full_path = os.path.join(root, file)
                all_patch_files.append(full_path)
                
                # Filter based on series.conf if available
                if args.only_disabled:
                    # Only include disabled patches
                    if disabled_patches and file in disabled_patches:
                        patch_files.append(full_path)
                elif enabled_patches is not None:
                    if file in enabled_patches:
                        patch_files.append(full_path)
                    elif file in disabled_patches:
                        continue  # Skip disabled patches
                    else:
                        # Patch not in series.conf - include it with warning
                        print(f"Warning: {file} not found in series.conf, including it")
                        patch_files.append(full_path)
                else:
                    # No series.conf, include all patches
                    patch_files.append(full_path)
    
    if not patch_files:
        print("No patch files found!", file=sys.stderr)
        return 1
    
    if args.max_patches:
        patch_files = patch_files[:args.max_patches]
    
    total_patches = len(all_patch_files)
    if args.only_disabled:
        analyzed_count = len(patch_files)
        print(f"Found {total_patches} total patch files ({analyzed_count} disabled patches being analyzed)")
        enabled_count = 0
        disabled_count = analyzed_count
    else:
        enabled_count = len(patch_files)
        disabled_count = total_patches - enabled_count
        print(f"Found {total_patches} total patch files ({enabled_count} enabled, {disabled_count} disabled)")
    
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
    generate_hunk_report(all_hunks, args.output, args.kernel_version, 
                        enabled_count, disabled_count)
    
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
