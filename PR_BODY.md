# Rewrite kernel patches

### What this PR does
- Regenerates and **synchronizes kernel patches** for `odroidn2` on the **edge** branch.
- Runs `./compile.sh rewrite-kernel-patches` which updates patch series based on current kernel sources.

### How it was produced

This PR is produced from [this](/armbian/build/tree/main/.github/workflows/maintenance-rewrite-kernel-patches.yml) GHA script.

- Board: `odroidn2`
- Branch: `edge`

### Review tips
- Verify that patch reordering and refactors are intentional.
- Check for newly added or removed patches.

### Files changed

| File | + | - | Δ |
|---|---:|---:|---:|
| patch/kernel/archive/meson64-6.19/jethome-0001-Fix-meson64-add-gpio-irq-patch-from-https-lkml.org-l.patch | 1 | 1 | 0 |

**Files:** 1  •  **Lines:** +1 / -1  (Δ 0)

