# Sunxi 6.16 Patch Analysis for Linux Kernel 6.18

This directory contains an analysis of patches from `patch/kernel/archive/sunxi-6.16` to determine if they are present in the mainline Linux kernel 6.18.

## Overview

The sunxi-6.16 patch directory contains **444 patches** that were applied to the Allwinner (sunxi) platform kernel version 6.16. This analysis helps identify which of these patches may have been merged into the mainline Linux kernel 6.18.

## Generated Files

1. **sunxi-6.16_vs_kernel-6.18_analysis.md** - Comprehensive analysis report
   - Summary statistics
   - Patches organized by subsystem
   - Patches organized by directory (patches.armbian, patches.megous, etc.)
   - Most frequently modified files
   - Complete patch listing with metadata
   - Instructions for manual verification

2. **sunxi-6.16_commit_ids.txt** - List of unique commit IDs extracted from patches
   - 372 unique commit IDs
   - One commit ID per line
   - Useful for bulk checking against the kernel repository

3. **tools/check_sunxi_patches_in_kernel.sh** - Automated verification script
   - Checks first 20 patches by commit ID
   - Can be extended to check all patches
   - Clones Linux kernel from GitHub if needed
   - Provides summary of found/not found patches

4. **tools/analyze_patches.py** - Python analysis tool
   - Parses patch files and extracts metadata
   - Generates detailed reports
   - Can be reused for other patch directories

## Key Findings

### Summary Statistics

- **Total Patches**: 444
- **Patches with Commit IDs**: 444 (100%)
- **Unique Subsystems**: 7
- **Unique Files Modified**: 598

### Patches by Subsystem

| Subsystem | Count |
|-----------|-------|
| arch | 207 (46.6%) |
| drivers | 201 (45.3%) |
| sound | 13 (2.9%) |
| Documentation | 10 (2.3%) |
| include | 9 (2.0%) |
| other | 3 (0.7%) |
| scripts | 1 (0.2%) |

### Patches by Source Directory

| Directory | Count |
|-----------|-------|
| patches.megous | 236 (53.2%) |
| patches.armbian | 176 (39.6%) |
| patches.drm | 26 (5.9%) |
| patches.media | 6 (1.4%) |

## How to Verify Patches in Mainline

### Method 1: Automated Check Using the Script

```bash
# Run the automated check script
cd /home/runner/work/build/build
./tools/check_sunxi_patches_in_kernel.sh
```

This script will:
1. Clone Linux kernel 6.18 from GitHub (if not already present)
2. Check the first 20 patches by their commit IDs
3. Report which patches are found or not found

### Method 2: Manual Check Using Git

```bash
# Clone the Linux kernel 6.18
git clone --depth=1 --branch v6.18 https://github.com/torvalds/linux.git
cd linux

# Check if a specific commit exists
git cat-file -t <commit-id>

# Search for a patch by subject
git log --all --grep "patch subject line" --oneline

# Check commits that modified a specific file
git log --all --oneline -- path/to/file
```

### Method 3: Use GitHub Web Interface

1. Go to https://github.com/torvalds/linux
2. Use the search bar to search for:
   - Commit IDs (from sunxi-6.16_commit_ids.txt)
   - Patch subjects
   - Modified file paths
3. Filter by the v6.18 tag to see if the commit is in that release

### Method 4: Bulk Check Using GitHub API

You can use the GitHub API to check multiple commits:

```bash
# Check if a commit exists in the repository
curl -s "https://api.github.com/repos/torvalds/linux/commits/<commit-id>" | jq -r '.sha'
```

## Using the Analysis Tool

The `analyze_patches.py` tool can be used to analyze other patch directories:

```bash
# Basic usage
python3 tools/analyze_patches.py <patch_directory> --kernel-version 6.18

# Generate both report and check script
python3 tools/analyze_patches.py <patch_directory> \
    --kernel-version 6.18 \
    --output my_analysis.md \
    --generate-script my_check_script.sh

# Examples:
python3 tools/analyze_patches.py patch/kernel/archive/sunxi-6.12 --kernel-version 6.18
python3 tools/analyze_patches.py patch/kernel/archive/rockchip64-6.18 --kernel-version 6.18
```

## Most Frequently Modified Files

The top files modified by multiple patches (indicating areas of active development):

1. **arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone.dtsi** (19 patches)
2. **drivers/input/touchscreen/cyttsp4_core.c** (14 patches)
3. **arch/arm64/boot/dts/allwinner/sun50i-h616.dtsi** (13 patches)
4. **arch/arm64/boot/dts/allwinner/Makefile** (12 patches)
5. **drivers/power/supply/axp20x_battery.c** (11 patches)

These files are likely to have significant differences from mainline and may require special attention when upgrading kernels.

## Important Notes

1. **Commit IDs May Not Match**: The commit IDs in the patches come from the original source tree (vendor kernel, developer tree, etc.) and may not exist in the mainline kernel.

2. **Patches May Be Modified**: When patches are merged upstream, they often undergo review and modification, so they may not match exactly.

3. **Patches May Be Split or Combined**: A single patch here might be split into multiple commits upstream, or multiple patches might be combined.

4. **Some Patches Are Vendor-Specific**: Many patches in sunxi-6.16 are specific to Armbian or other distributions and may never be merged upstream.

5. **Zero Commit IDs**: Patches with commit ID `000000000000...` are locally created patches without an upstream source.

## Next Steps

1. Review the detailed report in `sunxi-6.16_vs_kernel-6.18_analysis.md`
2. Run `tools/check_sunxi_patches_in_kernel.sh` to check the first batch of patches
3. For patches not found, manually search using GitHub or git.kernel.org
4. Document which patches are critical for your use case
5. Consider upstreaming important patches that aren't in mainline

## Additional Resources

- **Linux Kernel GitHub Mirror**: https://github.com/torvalds/linux
- **Linux Kernel Git (Official)**: https://git.kernel.org/
- **Allwinner (sunxi) Wiki**: https://linux-sunxi.org/
- **Armbian Documentation**: https://docs.armbian.com/

## Files in This Analysis

```
.
├── sunxi-6.16_vs_kernel-6.18_analysis.md    # Detailed analysis report
├── sunxi-6.16_commit_ids.txt                # List of commit IDs
├── SUNXI_PATCH_ANALYSIS_README.md           # This file
└── tools/
    ├── analyze_patches.py                    # Patch analysis tool
    ├── check_sunxi_patches_in_kernel.sh     # Automated verification script
    └── check_patches_in_mainline.py         # Advanced checking tool (requires kernel clone)
```

---

**Generated**: 2025-12-06  
**Analyzed Patch Directory**: patch/kernel/archive/sunxi-6.16  
**Target Kernel Version**: Linux 6.18  
**Total Patches**: 444
