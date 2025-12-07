# Comparison: sunxi-6.16 vs sunxi-6.18 Patchsets (Against Linux Kernel 6.18)

**Analysis Date:** 2025-12-07

## Overview

This document compares two patchsets from the Armbian build repository:
1. **sunxi-6.16** - Original patchset (archived)
2. **sunxi-6.18** - Cleaned-up patchset (current)

Both patchsets were analyzed against Linux kernel 6.18 to determine which patches/hunks are present in mainline.

## Summary Statistics

| Metric | sunxi-6.16 | sunxi-6.18 | Change |
|--------|------------|------------|--------|
| **Total Patches** | 444 | 444 | Same |
| **Total Hunks** | 1,739 | 1,723 | -16 (-0.9%) |
| **Hunks Found in Kernel 6.18** | 87 (5.0%) | 87 (5.0%) | Same |
| **Hunks Not Found** | 1,652 (95.0%) | 1,636 (95.0%) | -16 |
| **Unique Commit IDs** | 372 | 3 | -369 |
| **Unique Files Modified** | 598 | 596 | -2 |

## Key Findings

### Patch Distribution (Identical)

Both patchsets have the same distribution by directory:

| Directory | Count | Percentage |
|-----------|-------|------------|
| patches.megous | 236 | 53.2% |
| patches.armbian | 176 | 39.6% |
| patches.drm | 26 | 5.9% |
| patches.media | 6 | 1.4% |

### Subsystem Distribution

| Subsystem | sunxi-6.16 | sunxi-6.18 | Change |
|-----------|------------|------------|--------|
| arch | 207 | 208 | +1 |
| drivers | 201 | 199 | -2 |
| sound | 13 | 14 | +1 |
| Documentation | 10 | 10 | - |
| include | 9 | 9 | - |
| other | 3 | 2 | -1 |
| scripts | 1 | 2 | +1 |

### Commit IDs

**sunxi-6.16:**
- 372 unique commit IDs
- Mix of upstream commits and vendor patches
- Many patches retain original commit hashes

**sunxi-6.18:**
- Only 3 unique commit IDs:
  - `0000000000000000000000000000000000000000` (most patches)
  - `2a8a9e3104ce70230ca67a39fd406d84662e77b2`
  - `2ce741f43a65732bd9078046c272743d06a41701`
- This indicates the patchset was "cleaned up" - patches were rebased/recreated

## Hunk-Level Analysis Results

### Found Hunks (87 in both patchsets)

The same 87 hunks were found in kernel 6.18 for both patchsets, indicating:
- The cleanup preserved the actual code changes
- The found hunks represent genuine upstream contributions
- Both patchsets target the same functionality

### Top Files with Found Hunks (Identical)

| Rank | File | Found Hunks |
|------|------|-------------|
| 1 | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | 11 |
| 2 | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | 6 |
| 3 | `arch/arm64/boot/dts/allwinner/sun50i-h6.dtsi` | 4 |
| 4 | `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | 4 |
| 5 | `drivers/net/ethernet/stmicro/stmmac/dwmac-sun8i.c` | 3 |

### Categories of Found Code

Both patchsets show the same distribution of found code:
- **Display (DRM) drivers:** ~30 hunks (Display Engine 3.3 support)
- **Device tree updates:** ~25 hunks (A83T, H6, H616 boards)
- **USB/TypeC fixes:** ~10 hunks (DWC3, TCPM)
- **Sound/power/network:** ~22 hunks (Various improvements)

## What Changed Between Versions?

### 1. Commit History Cleanup
- **sunxi-6.16:** Preserved original commit IDs from various sources
- **sunxi-6.18:** Rebased to remove upstream commit references
- **Impact:** Easier to track which patches are custom vs. upstream

### 2. Minimal Code Changes
- Only 16 fewer hunks in sunxi-6.18 (0.9% reduction)
- Same number of patches (444)
- Nearly identical file modifications (596 vs 598 files)
- **Impact:** The cleanup was primarily metadata, not functional changes

### 3. Identical Mainline Status
- Same 87 hunks (5%) found in kernel 6.18
- Same 95% not in mainline
- Same files modified
- **Impact:** Both patchsets have identical relationship to mainline

## Interpretation

### The "Cleanup" Consisted Of:
1. **Rebasing patches** - Removed original commit IDs
2. **Minor consolidation** - Combined or split a few patches (16 fewer hunks)
3. **Metadata updates** - Updated patch headers
4. **No functional changes** - Same code, same mainline status

### Why Clean Up?

Advantages of sunxi-6.18 (cleaned-up version):
- **Clearer provenance:** Patches marked with `000000...` are clearly custom
- **Easier rebasing:** No conflicts with upstream commit IDs
- **Simpler tracking:** Easier to identify which patches need upstreaming
- **Better maintenance:** Cleaner history for ongoing development

## Recommendations

### For Users
- **Use sunxi-6.18** - It's the cleaned-up, maintained version
- Both versions have identical functionality
- sunxi-6.18 is easier to work with for custom patches

### For Developers
- **Focus upstreaming efforts** on the 95% not in mainline
- **Prioritize:** Display drivers, device trees, USB fixes (the found 5%)
- **Document:** The 3 non-zero commit IDs in sunxi-6.18 may be reference patches

### For Upstreaming
Key areas that could be upstreamed (not currently in 6.18):
1. Additional Display Engine 3.3 (DE33) features
2. Board-specific device tree overlays
3. Armbian-specific hardware enablement
4. PinePhone-specific improvements
5. H616/H618 SoC support enhancements

## Conclusion

The sunxi-6.18 patchset is a **metadata cleanup** of sunxi-6.16 with:
- **Same functional content** (444 patches, 95% not in mainline)
- **Cleaner history** (rebased, removed upstream commit IDs)
- **Identical code** (same 87 hunks found in kernel 6.18)
- **Better maintainability** (easier to track custom vs. upstream patches)

Both patchsets confirm that **95% of Armbian's sunxi patches are custom/vendor-specific** modifications not present in mainline Linux kernel 6.18.

---

## Generated Files

### sunxi-6.16 Analysis
- `sunxi-6.16_vs_kernel-6.18_analysis.md` - Patch metadata
- `sunxi-6.16_hunk_analysis.md` - Hunk-level comparison
- `sunxi-6.16_commit_ids.txt` - 372 unique commit IDs

### sunxi-6.18 Analysis  
- `sunxi-6.18_vs_kernel-6.18_analysis.md` - Patch metadata
- `sunxi-6.18_hunk_analysis.md` - Hunk-level comparison
- `sunxi-6.18_commit_ids.txt` - 3 unique commit IDs

### Comparison
- `SUNXI_6.16_VS_6.18_COMPARISON.md` - This document
