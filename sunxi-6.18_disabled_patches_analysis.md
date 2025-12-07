# Hunk-Level Analysis: sunxi vs Linux Kernel 6.18

**Analysis Date:** 2025-12-07 04:48:05

## Summary

- **Total Hunks:** 296
- **Found in Kernel:** 11 (3%)
- **Not Found:** 285 (96%)
- **Patches Analyzed:** 43
- **Patches Enabled:** 0
- **Patches Disabled:** 43

## Patches by Directory

| Directory | Patches | Hunks | Found | Not Found | Found % |
|-----------|---------|-------|-------|-----------|----------|
| patches.armbian | 6 | 61 | 0 | 61 | 0% |
| patches.drm | 26 | 141 | 11 | 130 | 7% |
| patches.megous | 11 | 94 | 0 | 94 | 0% |

## Files with Found Hunks (Top 20)

| File | Found Hunks |
|------|-------------|
| `drivers/gpu/drm/sun4i/sun8i_mixer.c` | 4 |
| `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | 4 |
| `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | 3 |

## Found Hunks (11)

Hunks whose changes appear to be present in Linux kernel 6.18:

| Patch File | File | Hunk | Lines | Match | Notes |
|------------|------|------|-------|-------|-------|
| drm-sun4i-de2-de3-refactor-mixer-initialisation.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #2 | +0/-2 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #1 | +1/-0 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #3 | +1/-0 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #4 | +1/-0 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #5 | +1/-0 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #6 | +2/-2 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | #7 | +1/-0 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | #8 | +1/-0 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | #9 | +2/-3 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #4 | +17/-0 | ✓ | Patch appears to be already applied (found after-state with context) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #8 | +4/-0 | ✓ | Patch appears to be already applied (found after-state with context) |

## Not Found Hunks (Sample - First 50)

| Patch File | File | Hunk | Lines | Notes |
|------------|------|------|-------|-------|
| clk-sunxi-ng-sun50i-a64-Switch-parent-of-MIPI-DSI-to-periph0-1x.patch | `drivers/clk/sunxi-ng/ccu-sun50i-a64.c` | #1 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| clk-sunxi-ng-sun50i-a64-Switch-parent-of-MIPI-DSI-to-periph0-1x.patch | `drivers/clk/sunxi-ng/ccu-sun50i-a64.c` | #2 | +8/-2 | Could not determine patch state reliably |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | `drivers/media/i2c/ov5640.c` | #1 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | `drivers/media/i2c/ov5640.c` | #2 | +7/-0 | Patch not applied (found before-state, patch still needed) |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | `drivers/media/i2c/ov5640.c` | #3 | +0/-22 | Patch not applied (found before-state, patch still needed) |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | `drivers/media/i2c/ov5640.c` | #4 | +2/-21 | Could not determine patch state reliably |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | `drivers/media/i2c/ov5640.c` | #5 | +2/-1 | Could not determine patch state reliably |
| video-pwm_bl-Allow-to-change-lth_brightness-via-sysfs.patch | `drivers/video/backlight/pwm_bl.c` | #1 | +55/-0 | Patch not applied (found before-state, patch still needed) |
| video-pwm_bl-Allow-to-change-lth_brightness-via-sysfs.patch | `drivers/video/backlight/pwm_bl.c` | #2 | +1/-0 | Could not determine patch state reliably |
| video-pwm_bl-Allow-to-change-lth_brightness-via-sysfs.patch | `drivers/video/backlight/pwm_bl.c` | #3 | +14/-3 | Could not determine patch state reliably |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #1 | +1/-0 | Could not determine patch state reliably |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #2 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #3 | +6/-0 | Patch not applied (found before-state, patch still needed) |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #4 | +1/-1 | Patch not applied (found before-state, patch still needed) |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #5 | +1/-1 | Patch not applied (found before-state, patch still needed) |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #6 | +19/-0 | Patch not applied (found before-state, patch still needed) |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #7 | +25/-2 | Patch not applied (found before-state, patch still needed) |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #8 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | `drivers/gpu/drm/bridge/synopsys/dw-hdmi.c` | #9 | +2/-1 | Could not determine patch state reliably |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/clk/sunxi-ng/ccu-sun50i-a64.c` | #1 | +3/-1 | Could not determine patch state reliably |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/drm_fbdev_ttm.c` | #2 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/drm_fbdev_ttm.c` | #3 | +13/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/panel/panel-sitronix-st7703.c` | #4 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/panel/panel-sitronix-st7703.c` | #5 | +5/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/panel/panel-sitronix-st7703.c` | #6 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/panel/panel-sitronix-st7703.c` | #7 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/panel/panel-sitronix-st7703.c` | #8 | +7/-0 | Could not determine patch state reliably |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun4i_tcon.c` | #9 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun4i_tcon.c` | #10 | +7/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun4i_tcon.c` | #11 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun4i_tcon.c` | #12 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun4i_tcon.c` | #13 | +3/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun4i_tcon.c` | #14 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun4i_tcon.c` | #15 | +7/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun4i_tcon.h` | #16 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun6i_mipi_dsi.c` | #17 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun6i_mipi_dsi.c` | #18 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun6i_mipi_dsi.c` | #19 | +4/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun6i_mipi_dsi.c` | #20 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun6i_mipi_dsi.c` | #21 | +6/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun6i_mipi_dsi.h` | #22 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #23 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #24 | +2/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #25 | +27/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #26 | +1/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #27 | +5/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #28 | +3/-0 | Patch not applied (found before-state, patch still needed) |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #29 | +1/-0 | Could not determine patch state reliably |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #30 | +1/-0 | Could not determine patch state reliably |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #31 | +2/-0 | Could not determine patch state reliably |

*... and 235 more hunks not found*

## Summary by Patch File

| Patch File | Total Hunks | Found | Not Found | Match % |
|------------|-------------|-------|-----------|----------|
| Add-sunxi-addr-driver-Used-to-fix-uwe5622-bluetooth-MAC-address.patch | 6 | 0 | 6 | 0% |
| Fix-ghost-touches-on-tsc2007-tft-screen.patch | 10 | 0 | 10 | 0% |
| Optimize-TSC2007-touchscreen-add-polling-method.patch | 7 | 0 | 7 | 0% |
| clk-sunxi-ng-sun50i-a64-Switch-parent-of-MIPI-DSI-to-periph0-1x.patch | 2 | 0 | 2 | 0% |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | 9 | 0 | 9 | 0% |
| drm-bridge-dw-hdmi-Report-HDMI-hotplug-events.patch | 2 | 0 | 2 | 0% |
| drm-sun4i-Report-page-flip-after-vsync-is-complete-not-in-the-m.patch | 8 | 0 | 8 | 0% |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | 40 | 0 | 40 | 0% |
| drm-sun4i-add-sun50i-h616-hdmi-phy-support.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-de2-Initialize-layer-fields-earlier.patch | 4 | 0 | 4 | 0% |
| drm-sun4i-de2-de3-Change-CSC-argument.patch | 10 | 0 | 10 | 0% |
| drm-sun4i-de2-de3-Merge-CSC-functions-into-one.patch | 5 | 0 | 5 | 0% |
| drm-sun4i-de2-de3-add-generic-blender-register-reference-functi.patch | 1 | 0 | 1 | 0% |
| drm-sun4i-de2-de3-add-mixer-version-enum.patch | 23 | 0 | 23 | 0% |
| drm-sun4i-de2-de3-call-csc-setup-also-for-UI-layer.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-de2-de3-refactor-mixer-initialisation.patch | 5 | 1 | 4 | 20% |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | 9 | 8 | 1 | 88% |
| drm-sun4i-de3-Add-YUV-formatter-module.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-de3-Implement-AFBC-support.patch | 15 | 0 | 15 | 0% |
| drm-sun4i-de3-add-YUV-support-to-the-DE3-mixer.patch | 5 | 0 | 5 | 0% |
| drm-sun4i-de3-add-YUV-support-to-the-TCON.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-de3-add-YUV-support-to-the-color-space-correction-mod.patch | 4 | 0 | 4 | 0% |
| drm-sun4i-de3-add-format-enumeration-function-to-engine.patch | 2 | 0 | 2 | 0% |
| drm-sun4i-de3-add-formatter-flag-to-mixer-config.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-de3-pass-engine-reference-to-ccsc-setup-function.patch | 2 | 0 | 2 | 0% |
| drm-sun4i-de33-csc-add-Display-Engine-3.3-DE33-support.patch | 4 | 0 | 4 | 0% |
| drm-sun4i-de33-fmt-add-Display-Engine-3.3-DE33-support.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | 13 | 2 | 11 | 15% |
| drm-sun4i-de33-vi_scaler-add-Display-Engine-3.3-DE33-support.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-support-YUV-formats-in-VI-scaler.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-vi_scaler-refactor-vi_scaler-enablement.patch | 5 | 0 | 5 | 0% |
| drv-mfd-axp20x-add-sysfs-interface.patch | 4 | 0 | 4 | 0% |
| drv-spi-spidev-Add-armbian-spi-dev-compatible.patch | 2 | 0 | 2 | 0% |
| dt-bindings-allwinner-add-H616-DE33-bus-binding.patch | 1 | 0 | 1 | 0% |
| dt-bindings-allwinner-add-H616-DE33-mixer-binding.patch | 1 | 0 | 1 | 0% |
| enable-TV-Output-on-OrangePi-Zero-LTE.patch | 32 | 0 | 32 | 0% |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | 5 | 0 | 5 | 0% |
| media-ov5640-Improve-error-reporting.patch | 2 | 0 | 2 | 0% |
| media-sun6i-csi-implement-vidioc_enum_framesizes.patch | 2 | 0 | 2 | 0% |
| misc-modem-power-Power-manager-for-modems.patch | 3 | 0 | 3 | 0% |
| mmc-sunxi-mmc-Remove-runtime-PM.patch | 8 | 0 | 8 | 0% |
| usb-gadget-Fix-dangling-pointer-in-netdev-private-data.patch | 18 | 0 | 18 | 0% |
| video-pwm_bl-Allow-to-change-lth_brightness-via-sysfs.patch | 3 | 0 | 3 | 0% |

## Methodology

This analysis breaks down each patch into individual hunks (chunks of changes) and checks if the hunks are already applied in Linux kernel 6.18.

**Context-Based Matching:**
- Each hunk includes context lines (unchanged lines) and added/removed lines
- The tool builds the expected "after" state (context + added lines)
- If this pattern is found as a consecutive sequence in the kernel file, the hunk is considered "found"
- This ensures that lines are found in the correct location with proper context

**Disabled Patches:**
- 43 patches were disabled in series.conf (marked with '-' prefix)
- Only 0 enabled patches were analyzed

**Expected Result:**
- If the patchset applies cleanly to kernel 6.18, most hunks should NOT be found
- Found hunks indicate changes that are already in the mainline kernel
- Disabled patches are excluded from analysis

**Limitations:**
- Cannot detect code that was modified during upstreaming
- Cannot detect code in different files (refactored/moved)
- Cannot detect functionally equivalent but differently written code
- Requires at least 3 lines of context for reliable matching
