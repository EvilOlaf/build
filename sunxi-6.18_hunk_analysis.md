# Hunk-Level Analysis: sunxi-6.16 vs Linux Kernel 6.18

**Analysis Date:** 2025-12-07 04:18:38

## Summary

- **Total Hunks:** 1723
- **Found in Kernel:** 87 (5%)
- **Not Found:** 1636 (94%)
- **Patches Analyzed:** 444

## Files with Found Hunks (Top 20)

| File | Found Hunks |
|------|-------------|
| `drivers/gpu/drm/sun4i/sun8i_mixer.c` | 11 |
| `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | 6 |
| `arch/arm64/boot/dts/allwinner/sun50i-h6.dtsi` | 4 |
| `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | 4 |
| `drivers/net/ethernet/stmicro/stmmac/dwmac-sun8i.c` | 3 |
| `arch/arm/boot/dts/allwinner/sun8i-a83t.dtsi` | 3 |
| `drivers/media/i2c/ov5640.c` | 3 |
| `drivers/gpu/drm/sun4i/sun8i_mixer.h` | 3 |
| `drivers/power/supply/axp20x_battery.c` | 2 |
| `arch/arm/boot/dts/allwinner/sun8i-a83t-tbs-a711.dts` | 2 |
| `drivers/media/i2c/gc2145.c` | 2 |
| `drivers/usb/dwc3/core.c` | 2 |
| `drivers/usb/typec/tcpm/fusb302.c` | 2 |
| `drivers/usb/typec/tcpm/tcpm.c` | 2 |
| `arch/arm/boot/dts/allwinner/sunxi-h3-h5.dtsi` | 2 |
| `arch/arm64/boot/dts/allwinner/sun50i-h616-orangepi-zero.dtsi` | 2 |
| `include/sound/soc-dai.h` | 2 |
| `drivers/dma/sun6i-dma.c` | 1 |
| `arch/arm64/boot/dts/allwinner/sun50i-a64.dtsi` | 1 |
| `arch/arm/mach-sunxi/mc_smp.c` | 1 |

## Found Hunks (87)

Hunks whose changes appear to be present in Linux kernel 6.18:

| Patch File | File | Hunk | Lines | Match | Notes |
|------------|------|------|-------|-------|-------|
| ARM-dts-sun8i-a83t-Add-hdmi-sound-card.patch | `arch/arm/boot/dts/allwinner/sun8i-a83t.dtsi` | #2 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| ARM-dts-sun8i-a83t-Add-missing-GPU-trip-point.patch | `arch/arm/boot/dts/allwinner/sun8i-a83t.dtsi` | #1 | +9/-1 | ✓ | Found 4/5 lines (80%) |
| ARM-dts-sun8i-a83t-tbs-a711-Add-camera-sensors-HM5065-GC2145.patch | `arch/arm/boot/dts/allwinner/sun8i-a83t-tbs-a711.dts` | #5 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| ARM-dts-sun8i-a83t-tbs-a711-Add-camera-sensors-HM5065-GC2145.patch | `arch/arm/boot/dts/allwinner/sun8i-a83t-tbs-a711.dts` | #6 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| ARM-dts-sun8i-a83t-tbs-a711-Give-Linux-more-privileges-over-SCP.patch | `arch/arm/boot/dts/allwinner/sun8i-a83t.dtsi` | #2 | +3/-0 | ✓ | Found 3/3 lines (100%) |
| ARM-dts-sun8i-h3-orange-pi-one-Enable-all-gpio-header-UARTs.patch | `arch/arm/boot/dts/allwinner/sun8i-h3-orangepi-one.dts` | #2 | +3/-4 | ✓ | Found 3/3 lines (100%) |
| ARM-dts-sun8i-r40-Add-hdmi-sound-card.patch | `arch/arm/boot/dts/allwinner/sun8i-r40.dtsi` | #2 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| ARM-dts-sunxi-h3-h5-Add-hdmi-sound-card.patch | `arch/arm/boot/dts/allwinner/sunxi-h3-h5.dtsi` | #2 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| ARM-sunxi-sunxi_cpu0_hotplug_support_set-is-not-supported-on-A8.patch | `arch/arm/mach-sunxi/mc_smp.c` | #1 | +3/-1 | ✓ | Found 2/2 lines (100%) |
| LED-green_power_on-red_status_heartbeat-arch-arm64-boot-dts-all.patch | `arch/arm64/boot/dts/allwinner/sun50i-h616-orangepi-zero.dtsi` | #1 | +4/-4 | ✓ | Found 3/4 lines (75%) |
| Move-a-node-to-avoid-merge-conflict.patch | `arch/arm/boot/dts/allwinner/sunxi-h3-h5.dtsi` | #2 | +6/-0 | ✓ | Found 4/4 lines (100%) |
| Optimize-TSC2007-touchscreen-add-polling-method.patch | `drivers/input/touchscreen/tsc2007_core.c` | #4 | +59/-0 | ✓ | Found 22/31 lines (71%) |
| Revert-usb-dwc3-Abort-suspend-on-soft-disconnect-failure.patch | `drivers/usb/dwc3/core.c` | #2 | +1/-3 | ✓ | Found 1/1 lines (100%) |
| Revert-usb-dwc3-Abort-suspend-on-soft-disconnect-failure.patch | `drivers/usb/dwc3/core.c` | #3 | +1/-3 | ✓ | Found 1/1 lines (100%) |
| Revert-usb-typec-tcpm-unregister-existing-source-caps-before-re.patch | `drivers/usb/typec/tcpm/tcpm.c` | #1 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| Sound-for-H616-H618-Allwinner-SOCs.patch | `include/sound/soc-dai.h` | #4 | +9/-0 | ✓ | Found 5/5 lines (100%) |
| Sound-for-H616-H618-Allwinner-SOCs.patch | `include/sound/soc-dai.h` | #5 | +4/-0 | ✓ | Found 2/2 lines (100%) |
| arm-dts-sun7i-a20-olimex-som-204-evb-olinuxino-micro-decrease-d.patch | `arch/arm/boot/dts/allwinner/sun7i-a20-olimex-som204-evb.dts` | #2 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| arm-dts-sun7i-a20-olinuxino-lime2-enable-ldo3-always-on.patch | `arch/arm/boot/dts/allwinner/sun7i-a20-olinuxino-lime2.dts` | #1 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| arm-patch-call-flush_icache-ASAP-after-writing-new-instruction.patch | `arch/arm/kernel/patch.c` | #1 | +9/-4 | ✓ | Found 3/3 lines (100%) |
| arm64-dts-allwinner-a64-Add-hdmi-sound-card.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64.dtsi` | #2 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| arm64-dts-allwinner-h6-Add-hdmi-sound-card.patch | `arch/arm64/boot/dts/allwinner/sun50i-h6.dtsi` | #3 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| arm64-dts-sun50i-a64-pinephone-Enable-internal-HMIC-bias.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone-1.0.dts` | #1 | +4/-1 | ✓ | Found 2/2 lines (100%) |
| arm64-dts-sun50i-a64-sopine-baseboard-mmc1-status-okay.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64-sopine-baseboard.dts` | #1 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| arm64-dts-sun50i-h5-orangepi-prime-add-regulator.patch | `arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-prime.dts` | #1 | +8/-0 | ✓ | Found 5/6 lines (83%) |
| arm64-dts-sun50i-h6-Add-r_uart-uart2-3-pins.patch | `arch/arm64/boot/dts/allwinner/sun50i-h6.dtsi` | #1 | +11/-0 | ✓ | Found 9/9 lines (100%) |
| arm64-dts-sun50i-h6-Add-r_uart-uart2-3-pins.patch | `arch/arm64/boot/dts/allwinner/sun50i-h6.dtsi` | #2 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| arm64-dts-sun50i-h6-Add-r_uart-uart2-3-pins.patch | `arch/arm64/boot/dts/allwinner/sun50i-h6.dtsi` | #3 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| arm64-dts-sun50i-h6-pine-h64-add-wifi-rtl8723cs.patch | `arch/arm64/boot/dts/allwinner/sun50i-h6-pine-h64.dts` | #3 | +12/-1 | ✓ | Found 2/2 lines (100%) |
| arm64-dts-sun50i-h616-orangepi-zero2-Enable-GPU-mali.patch | `arch/arm64/boot/dts/allwinner/sun50i-h616-orangepi-zero2.dts` | #1 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| arm64-dts-sun50i-h616-orangepi-zero2-reg_usb1_vbus-status-ok.patch | `arch/arm64/boot/dts/allwinner/sun50i-h616-orangepi-zero.dtsi` | #1 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| arm64-dts-sun50i-h618-orangepi-zero3-Enable-GPU-mali.patch | `arch/arm64/boot/dts/allwinner/sun50i-h618-orangepi-zero3.dts` | #1 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| bluetooth-h5-Don-t-re-initialize-rtl8723cs-on-resume.patch | `drivers/bluetooth/hci_h5.c` | #1 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| dma-sun6i-dma-add-sun50i-h616-support.patch | `drivers/dma/sun6i-dma.c` | #1 | +22/-0 | ✓ | Found 15/16 lines (94%) |
| drm-sun4i-de2-Initialize-layer-fields-earlier.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #1 | +5/-0 | ✓ | Found 4/4 lines (100%) |
| drm-sun4i-de2-Initialize-layer-fields-earlier.patch | `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | #3 | +5/-0 | ✓ | Found 4/4 lines (100%) |
| drm-sun4i-de2-de3-add-mixer-version-enum.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.h` | #15 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de2-de3-refactor-mixer-initialisation.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #5 | +1/-28 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #1 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #2 | +2/-2 | ✓ | Found 2/2 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #3 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #4 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #5 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #6 | +2/-2 | ✓ | Found 2/2 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | #7 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | #8 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | #9 | +2/-3 | ✓ | Found 2/2 lines (100%) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #2 | +11/-3 | ✓ | Found 8/10 lines (80%) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #4 | +17/-0 | ✓ | Found 13/13 lines (100%) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #5 | +18/-6 | ✓ | Found 13/15 lines (87%) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #6 | +24/-0 | ✓ | Found 14/17 lines (82%) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #7 | +12/-0 | ✓ | Found 8/10 lines (80%) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #8 | +4/-0 | ✓ | Found 2/2 lines (100%) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.h` | #11 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.h` | #12 | +3/-0 | ✓ | Found 2/2 lines (100%) |
| drm-sun4i-de33-vi_scaler-add-Display-Engine-3.3-DE33-support.patch | `drivers/gpu/drm/sun4i/sun8i_ui_layer.c` | #1 | +15/-4 | ✓ | Found 10/13 lines (77%) |
| drv-gpu-drm-gem-dma-Export-with-handle-allocator.patch | `drivers/gpu/drm/drm_gem_dma_helper.c` | #1 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| drv-gpu-drm-sun4i-sun8i_mixer.c-add-h3-mixer1.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #1 | +8/-0 | ✓ | Found 5/6 lines (83%) |
| drv-nvmem-sunxi_sid-Support-SID-on-H616.patch | `drivers/nvmem/sunxi_sid.c` | #1 | +6/-0 | ✓ | Found 3/4 lines (75%) |
| drv-of-Device-Tree-Overlay-ConfigFS-interface.patch | `drivers/of/fdt_address.c` | #4 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| drv-spi-spi-sun4i.c-spi-bug-low-on-sck.patch | `drivers/spi/spi-sun4i.c` | #1 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| drv-staging-media-sunxi-cedrus-add-H616-variant.patch | `drivers/staging/media/sunxi/cedrus/cedrus.c` | #1 | +9/-0 | ✓ | Found 6/7 lines (86%) |
| dt-bindings-allwinner-add-H616-DE33-mixer-binding.patch | `Documentation/devicetree/bindings/display/allwinner,sun8i-a83t-de2-mixer.yaml` | #1 | +1/-1 | ✓ | Found 1/1 lines (100%) |
| enable-TV-Output-on-OrangePi-Zero-LTE.patch | `drivers/gpu/drm/sun4i/sun8i_mixer.c` | #31 | +3/-2 | ✓ | Found 3/3 lines (100%) |
| h616-add-keys.patch | `drivers/input/keyboard/sun4i-lradc-keys.c` | #4 | +6/-0 | ✓ | Found 3/4 lines (75%) |
| media-gc2145-Add-PIXEL_RATE-HBLANK-and-VBLANK-controls.patch | `drivers/media/i2c/gc2145.c` | #1 | +3/-0 | ✓ | Found 3/3 lines (100%) |
| media-gc2145-Galaxycore-camera-module-driver.patch | `drivers/media/i2c/Kconfig` | #1 | +10/-0 | ✓ | Found 8/8 lines (100%) |
| media-i2c-gc2145-Parse-and-register-properties.patch | `drivers/media/i2c/gc2145.c` | #1 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | `drivers/media/i2c/ov5640.c` | #1 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | `drivers/media/i2c/ov5640.c` | #2 | +7/-0 | ✓ | Found 5/5 lines (100%) |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | `drivers/media/i2c/ov5640.c` | #4 | +2/-21 | ✓ | Found 2/2 lines (100%) |
| media-ov5648-Fix-call-to-pm_runtime_set_suspended.patch | `drivers/media/i2c/ov5648.c` | #1 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| media-sun6i-csi-Add-multicamera-support-for-parallel-bus.patch | `drivers/media/platform/sunxi/sun6i-csi/sun6i_csi_bridge.c` | #1 | +3/-3 | ✓ | Found 3/3 lines (100%) |
| media-sun6i-csi-merge-sun6i_csi_formats-and-sun6i_csi_formats_m.patch | `drivers/media/platform/sunxi/sun6i-csi/sun6i_csi_capture.c` | #6 | +67/-0 | ✓ | Found 48/67 lines (72%) |
| net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch | `drivers/net/ethernet/stmicro/stmmac/dwmac-sun8i.c` | #1 | +4/-6 | ✓ | Found 4/4 lines (100%) |
| net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch | `drivers/net/ethernet/stmicro/stmmac/dwmac-sun8i.c` | #2 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch | `drivers/net/ethernet/stmicro/stmmac/dwmac-sun8i.c` | #3 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| pci-Workaround-ITS-timeouts-on-poweroff-reboot-on-Orange-Pi-5-P.patch | `drivers/pci/pcie/portdrv.c` | #1 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch | `drivers/power/supply/axp20x_battery.c` | #1 | +1/-0 | ✓ | Found 1/1 lines (100%) |
| power-supply-axp20x-battery-Support-POWER_SUPPLY_PROP_CHARGE_BE.patch | `drivers/power/supply/axp20x_battery.c` | #2 | +15/-0 | ✓ | Found 10/13 lines (77%) |
| sound-soc-sunxi-Provoke-the-early-load-of-sun8i-codec-analog.patch | `sound/soc/sunxi/Makefile` | #1 | +1/-2 | ✓ | Found 1/1 lines (100%) |
| usb-gadget-Fix-dangling-pointer-in-netdev-private-data.patch | `drivers/usb/gadget/function/f_eem.c` | #4 | +9/-14 | ✓ | Found 6/8 lines (75%) |
| usb-gadget-Fix-dangling-pointer-in-netdev-private-data.patch | `drivers/usb/gadget/function/f_subset.c` | #13 | +7/-6 | ✓ | Found 6/7 lines (86%) |
| usb-musb-sunxi-Avoid-enabling-host-side-code-on-SoCs-where-it-s.patch | `drivers/usb/musb/musb_core.c` | #1 | +10/-0 | ✓ | Found 2/2 lines (100%) |
| usb-typec-fusb302-Set-the-current-before-enabling-pullups.patch | `drivers/usb/typec/tcpm/fusb302.c` | #1 | +8/-0 | ✓ | Found 5/5 lines (100%) |
| usb-typec-fusb302-Update-VBUS-state-even-if-VBUS-interrupt-is-n.patch | `drivers/usb/typec/tcpm/fusb302.c` | #1 | +8/-7 | ✓ | Found 6/8 lines (75%) |
| usb-typec-tcpm-Unregister-altmodes-before-registering-new-ones.patch | `drivers/usb/typec/tcpm/tcpm.c` | #1 | +3/-1 | ✓ | Found 2/2 lines (100%) |

## Not Found Hunks (Sample - First 50)

| Patch File | File | Hunk | Lines | Notes |
|------------|------|------|-------|-------|
| media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch | `drivers/staging/media/sunxi/cedrus/cedrus_video.c` | #1 | +7/-0 | Only 2/5 lines found (40%) |
| media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch | `drivers/staging/media/sunxi/cedrus/cedrus_video.h` | #2 | +2/-1 | Only 0/2 lines found (0%) |
| media-Add-NV12-and-P010-AFBC-compressed-formats.patch | `drivers/media/v4l2-core/v4l2-ioctl.c` | #1 | +2/-0 | Only 0/2 lines found (0%) |
| media-Add-NV12-and-P010-AFBC-compressed-formats.patch | `include/uapi/linux/videodev2.h` | #2 | +4/-1 | Only 0/2 lines found (0%) |
| media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch | `drivers/staging/media/sunxi/cedrus/cedrus.h` | #1 | +11/-0 | Only 0/7 lines found (0%) |
| media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch | `drivers/staging/media/sunxi/cedrus/cedrus_h265.c` | #2 | +2/-1 | Only 0/2 lines found (0%) |
| media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch | `drivers/staging/media/sunxi/cedrus/cedrus_hw.c` | #3 | +12/-0 | Only 0/6 lines found (0%) |
| media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch | `drivers/staging/media/sunxi/cedrus/cedrus_hw.c` | #4 | +4/-0 | Only 1/3 lines found (33%) |
| media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch | `drivers/staging/media/sunxi/cedrus/cedrus_regs.h` | #5 | +6/-0 | Only 0/6 lines found (0%) |
| media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch | `drivers/staging/media/sunxi/cedrus/cedrus_video.c` | #6 | +16/-0 | Only 2/12 lines found (17%) |
| media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch | `drivers/staging/media/sunxi/cedrus/cedrus_video.c` | #7 | +20/-1 | Only 4/12 lines found (33%) |
| dma-sun6i-dma-add-sun50i-h616-support.patch | `drivers/dma/sun6i-dma.c` | #2 | +1/-1 | Only 0/1 lines found (0%) |
| media-cedrus-Increase-H6-clock-rate.patch | `drivers/staging/media/sunxi/cedrus/cedrus.c` | #1 | +1/-2 | Only 0/1 lines found (0%) |
| media-cedrus-Don-t-CPU-map-source-buffers.patch | `drivers/staging/media/sunxi/cedrus/cedrus_video.c` | #1 | +1/-1 | Only 0/1 lines found (0%) |
| net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch | `drivers/net/ethernet/stmicro/stmmac/dwmac-sun8i.c` | #4 | +4/-8 | Only 1/4 lines found (25%) |
| mmc-add-delay-after-power-class-selection.patch | `drivers/mmc/core/mmc.c` | #1 | +2/-0 | Only 0/1 lines found (0%) |
| mmc-add-delay-after-power-class-selection.patch | `drivers/mmc/core/mmc.c` | #2 | +2/-1 | Only 0/1 lines found (0%) |
| ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch | `arch/arm/boot/dts/allwinner/sun8i-a83t-tbs-a711.dts` | #1 | +1/-1 | Only 0/1 lines found (0%) |
| ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch | `arch/arm/boot/dts/allwinner/sun8i-a83t-tbs-a711.dts` | #2 | +11/-1 | Only 0/7 lines found (0%) |
| dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch | `Documentation/devicetree/bindings/media/i2c/hm5065.txt` | #1 | +49/-1 | File Documentation/devicetree/bindings/media/i2c/hm5065.txt not found in kernel |
| arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone.dtsi` | #1 | +6/-0 | Only 1/4 lines found (25%) |
| arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone.dtsi` | #2 | +1/-1 | Only 0/1 lines found (0%) |
| arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone.dtsi` | #3 | +17/-1 | Only 4/11 lines found (36%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #1 | +1/-0 | Only 0/1 lines found (0%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #2 | +32/-0 | Only 0/25 lines found (0%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #3 | +6/-0 | Only 1/5 lines found (20%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #4 | +2/-0 | Only 0/1 lines found (0%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #5 | +112/-0 | Only 28/77 lines found (36%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #6 | +3/-0 | Only 0/1 lines found (0%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #7 | +29/-0 | Only 7/18 lines found (39%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #8 | +35/-0 | Only 11/21 lines found (52%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #9 | +26/-0 | Only 8/20 lines found (40%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #10 | +6/-0 | Only 3/6 lines found (50%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #11 | +12/-0 | Only 3/11 lines found (27%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #12 | +14/-0 | Only 3/12 lines found (25%) |
| media-ov5640-Implement-autofocus.patch | `drivers/media/i2c/ov5640.c` | #13 | +1/-1 | Only 0/1 lines found (0%) |
| power-supply-axp20x-battery-Improve-probe-error-reporting.patch | `drivers/power/supply/axp20x_battery.c` | #1 | +5/-6 | Only 1/5 lines found (20%) |
| power-supply-axp20x-battery-Improve-probe-error-reporting.patch | `drivers/power/supply/axp20x_battery.c` | #2 | +7/-11 | Only 0/6 lines found (0%) |
| arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone.dtsi` | #1 | +1/-0 | Only 0/1 lines found (0%) |
| arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone.dtsi` | #2 | +1/-2 | Only 0/1 lines found (0%) |
| arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch | `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone-1.1.dts` | #1 | +2/-3 | Only 0/1 lines found (0%) |
| arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch | `arch/arm64/boot/dts/allwinner/sun50i-h5-emlid-neutis-n5-devboard.dts` | #1 | +8/-0 | Only 2/4 lines found (50%) |
| arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch | `arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-pc2.dts` | #2 | +4/-0 | Only 1/2 lines found (50%) |
| arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch | `arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-pc2.dts` | #3 | +4/-0 | Only 1/2 lines found (50%) |
| arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch | `arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-prime.dts` | #4 | +4/-0 | Only 1/2 lines found (50%) |
| arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch | `arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-prime.dts` | #5 | +4/-0 | Only 1/2 lines found (50%) |
| arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch | `arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-zero-plus2.dts` | #6 | +4/-0 | Only 1/2 lines found (50%) |
| arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch | `arch/arm64/boot/dts/allwinner/sun50i-h5-orangepi-zero-plus2.dts` | #7 | +4/-1 | Only 1/2 lines found (50%) |
| dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch | `Documentation/devicetree/bindings/input/gpio-vibrator.yaml` | #1 | +6/-2 | Only 1/5 lines found (20%) |
| dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch | `Documentation/devicetree/bindings/mfd/x-powers,ac100.yaml` | #1 | +28/-0 | Only 7/21 lines found (33%) |

*... and 1586 more hunks not found*

## Summary by Patch File

| Patch File | Total Hunks | Found | Not Found | Match % |
|------------|-------------|-------|-----------|----------|
| 2-arm64-dts-sun50i-Define-orientation-and-rotation-for-PinePhone-.patch | 1 | 0 | 1 | 0% |
| ARM-dts-axp813-Add-charger-LED.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun5i-Add-PocketBook-Touch-Lux-3-display-ctp-support.patch | 8 | 0 | 8 | 0% |
| ARM-dts-sun5i-Add-soc-handle.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun5i-a13-pocketbook-touch-lux-3-Add-RTC-clock-cells.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-a83t-Add-MBUS-node.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-a83t-Add-cedrus-video-codec-support-to-A83T-untes.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-a83t-Add-hdmi-sound-card.patch | 2 | 1 | 1 | 50% |
| ARM-dts-sun8i-a83t-Add-missing-GPU-trip-point.patch | 1 | 1 | 0 | 100% |
| ARM-dts-sun8i-a83t-Enable-hdmi-sound-card-on-boards-with-hdmi.patch | 4 | 0 | 4 | 0% |
| ARM-dts-sun8i-a83t-Improve-CPU-OPP-tables-go-up-to-1.8GHz.patch | 2 | 0 | 2 | 0% |
| ARM-dts-sun8i-a83t-Set-fifo-size-for-uarts.patch | 5 | 0 | 5 | 0% |
| ARM-dts-sun8i-a83t-tbs-a711-Add-PN544-NFC-support.patch | 3 | 0 | 3 | 0% |
| ARM-dts-sun8i-a83t-tbs-a711-Add-camera-sensors-HM5065-GC2145.patch | 6 | 2 | 4 | 33% |
| ARM-dts-sun8i-a83t-tbs-a711-Add-flash-led-support.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch | 2 | 0 | 2 | 0% |
| ARM-dts-sun8i-a83t-tbs-a711-Add-regulators-to-the-accelerometer.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-a83t-tbs-a711-Add-sound-support-via-AC100-codec.patch | 3 | 0 | 3 | 0% |
| ARM-dts-sun8i-a83t-tbs-a711-Add-support-for-the-vibrator-motor.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-a83t-tbs-a711-Enable-charging-LED.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-a83t-tbs-a711-Give-Linux-more-privileges-over-SCP.patch | 3 | 1 | 2 | 33% |
| ARM-dts-sun8i-a83t-tbs-a711-Increase-voltage-on-the-vibrator.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-h2-plus-bananapi-m2-zero-Enable-HDMI-audio.patch | 2 | 0 | 2 | 0% |
| ARM-dts-sun8i-h3-Enable-hdmi-sound-card-on-boards-with-hdmi.patch | 19 | 0 | 19 | 0% |
| ARM-dts-sun8i-h3-Use-my-own-more-aggressive-OPPs-on-H3.patch | 2 | 0 | 2 | 0% |
| ARM-dts-sun8i-h3-orange-pi-one-Enable-all-gpio-header-UARTs.patch | 2 | 1 | 1 | 50% |
| ARM-dts-sun8i-h3-orange-pi-pc-Increase-max-CPUX-voltage-to-1.4V.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-nanopiduo2-Use-key-0-as-power-button.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-nanopiduo2-enable-ethernet.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sun8i-r40-Add-hdmi-sound-card.patch | 2 | 1 | 1 | 50% |
| ARM-dts-sun8i-r40-bananapi-m2-ultra-Enable-HDMI-audio.patch | 2 | 0 | 2 | 0% |
| ARM-dts-sun8i-v40-bananapi-m2-berry-Enable-HDMI-audio.patch | 2 | 0 | 2 | 0% |
| ARM-dts-suni-a83t-Add-i2s0-pins.patch | 1 | 0 | 1 | 0% |
| ARM-dts-sunxi-Add-aliases-for-MMC.patch | 3 | 0 | 3 | 0% |
| ARM-dts-sunxi-a83t-Add-SCPI-protocol.patch | 2 | 0 | 2 | 0% |
| ARM-dts-sunxi-h3-h5-Add-SCPI-protocol.patch | 3 | 0 | 3 | 0% |
| ARM-dts-sunxi-h3-h5-Add-hdmi-sound-card.patch | 2 | 1 | 1 | 50% |
| ARM-sunxi-Add-experimental-suspend-to-memory-implementation-for.patch | 2 | 0 | 2 | 0% |
| ARM-sunxi-Use-SCPI-to-send-suspend-message-to-SCP-on-A83T.patch | 2 | 0 | 2 | 0% |
| ARM-sunxi-sunxi_cpu0_hotplug_support_set-is-not-supported-on-A8.patch | 1 | 1 | 0 | 100% |
| ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-EMAC1.patch | 1 | 0 | 1 | 0% |
| ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-HDMI.patch | 2 | 0 | 2 | 0% |
| ASOC-sun9i-hdmi-audio-Initial-implementation.patch | 3 | 0 | 3 | 0% |
| ASoC-AC200-Initial-driver.patch | 5 | 0 | 5 | 0% |
| ASoC-ec25-New-codec-driver-for-the-EC25-modem.patch | 4 | 0 | 4 | 0% |
| ASoC-simple-card-Allow-to-define-pins-for-aux-jack-devices.patch | 1 | 0 | 1 | 0% |
| ASoC-sun8i-codec-Add-debug-output-for-jack-detection.patch | 10 | 0 | 10 | 0% |
| ASoC-sun8i-codec-Allow-the-jack-type-to-be-set-via-device-tree.patch | 2 | 0 | 2 | 0% |
| ASoC-sun8i-codec-Set-jack_type-from-DT-in-probe.patch | 2 | 0 | 2 | 0% |
| ASoC-sun8i-codec-define-button-keycodes.patch | 1 | 0 | 1 | 0% |
| Add-BananaPi-BPI-M4-Zero-overlays.patch | 14 | 0 | 14 | 0% |
| Add-BananaPi-BPI-M4-Zero-pinctrl.patch | 2 | 0 | 2 | 0% |
| Add-FB_TFT-ST7796S-driver.patch | 3 | 0 | 3 | 0% |
| Add-HDMI-support-for-pcDuino-1-and-2-by-including-HDMI-and-DE-n.patch | 2 | 0 | 2 | 0% |
| Add-HDMI-support-for-pcDuino-3-by-including-HDMI-and-DE-nodes.patch | 2 | 0 | 2 | 0% |
| Add-dump_reg-and-sunxi-sysinfo-drivers.patch | 11 | 0 | 11 | 0% |
| Add-sunxi-addr-driver-Used-to-fix-uwe5622-bluetooth-MAC-address.patch | 6 | 0 | 6 | 0% |
| Add-support-for-my-private-Sapomat-device.patch | 1 | 0 | 1 | 0% |
| Add-wifi-nodes-for-Inovato-Quadra.patch | 1 | 0 | 1 | 0% |
| Add-ws2812-RGB-driver-for-allwinner-H616.patch | 3 | 0 | 3 | 0% |
| BigTreeTech-CB1-dts-i2c-gpio-mode-adjustment-and-ws2812-rgb_val.patch | 3 | 0 | 3 | 0% |
| Compile-the-pwm-overlay.patch | 1 | 0 | 1 | 0% |
| Correct-perf-interrupt-source-number-as-referenced-in-the-Allwi.patch | 1 | 0 | 1 | 0% |
| Defconfigs-for-all-my-devices.patch | 6 | 0 | 6 | 0% |
| Doc-dt-bindings-usb-add-binding-for-DWC3-controller-on-Allwinne.patch | 1 | 0 | 1 | 0% |
| Enable-DMA-support-for-the-Allwinner-A10-EMAC-which-already-exi.patch | 1 | 0 | 1 | 0% |
| Enable-creation-of-__symbols__-node.patch | 1 | 0 | 1 | 0% |
| Fix-broken-allwinner-sram-dependency-on-h616-h618.patch | 1 | 0 | 1 | 0% |
| Fix-ghost-touches-on-tsc2007-tft-screen.patch | 10 | 0 | 10 | 0% |
| Fix-include-uapi-spi-spidev-module.patch | 1 | 0 | 1 | 0% |
| Fix-intptr_t-typedef.patch | 1 | 0 | 1 | 0% |
| Input-axp20x-pek-allow-wakeup-after-shutdown.patch | 2 | 0 | 2 | 0% |
| LED-green_power_on-red_status_heartbeat-arch-arm64-boot-dts-all.patch | 1 | 1 | 0 | 100% |
| MAINTAINERS-Add-entry-for-Himax-HM5065.patch | 1 | 0 | 1 | 0% |
| Make-microbuttons-on-Orange-Pi-PC-and-PC-2-work-as-power-off-bu.patch | 2 | 0 | 2 | 0% |
| Makefile-CONFIG_SHELL-fix-for-builddeb-packaging.patch | 1 | 0 | 1 | 0% |
| Mark-some-slow-drivers-for-async-probe-with-PROBE_PREFER_ASYNCH.patch | 2 | 0 | 2 | 0% |
| Move-a-node-to-avoid-merge-conflict.patch | 6 | 1 | 5 | 16% |
| Move-sun50i-h6-pwm-settings-to-its-own-overlay.patch | 2 | 0 | 2 | 0% |
| Optimize-TSC2007-touchscreen-add-polling-method.patch | 7 | 1 | 6 | 14% |
| Revert-ASoC-soc-core-merge-snd_soc_unregister_component-and-snd.patch | 3 | 0 | 3 | 0% |
| Revert-Input-cyttsp4-remove-driver.patch | 10 | 0 | 10 | 0% |
| Revert-drm-sun4i-hdmi-switch-to-struct-drm_edid.patch | 1 | 0 | 1 | 0% |
| Revert-drm-sun4i-lvds-Invert-the-LVDS-polarity.patch | 1 | 0 | 1 | 0% |
| Revert-usb-dwc3-Abort-suspend-on-soft-disconnect-failure.patch | 5 | 2 | 3 | 40% |
| Revert-usb-typec-tcpm-unregister-existing-source-caps-before-re.patch | 2 | 1 | 1 | 50% |
| Sound-for-H616-H618-Allwinner-SOCs.patch | 23 | 2 | 21 | 8% |
| Temp_fix-mailbox-arch-arm64-boot-dts-allwinner-sun50i-a64-pinep.patch | 4 | 0 | 4 | 0% |
| add-dtb-overlay-for-zero2w.patch | 5 | 0 | 5 | 0% |
| add-initial-support-for-orangepi3-lts.patch | 1 | 0 | 1 | 0% |
| add-nodes-for-sunxi-info-sunxi-addr-and-sunxi-dump-reg.patch | 2 | 0 | 2 | 0% |
| arm-arm64-dts-Add-leds-axp20x-charger.patch | 4 | 0 | 4 | 0% |
| arm-dts-Add-sun8i-h2-plus-nanopi-duo-device.patch | 1 | 0 | 1 | 0% |
| arm-dts-Add-sun8i-h2-plus-sunvell-r69-device.patch | 1 | 0 | 1 | 0% |
| arm-dts-a10-cubiebord-a20-cubietruck-green-LED-mmc0-default-tri.patch | 2 | 0 | 2 | 0% |
| arm-dts-a20-orangepi-and-mini-fix-phy-mode-hdmi.patch | 4 | 0 | 4 | 0% |
| arm-dts-h3-nanopi-neo-Add-regulator-leds-mmc2.patch | 1 | 0 | 1 | 0% |
| arm-dts-h3-nanopi-neo-air-Add-regulator-camera-wifi-bluetooth-o.patch | 3 | 0 | 3 | 0% |
| arm-dts-h3-orangepi-2-Add-regulator-vdd-cpu.patch | 2 | 0 | 2 | 0% |
| arm-dts-overlay-Add-Overlays-for-sunxi.patch | 96 | 0 | 96 | 0% |
| arm-dts-overlay-sun8i-h3-cpu-clock-add-overclock.patch | 4 | 0 | 4 | 0% |
| arm-dts-sun5i-a13-olinuxino-Add-panel-lcd-olinuxino-4.3-needed-.patch | 5 | 0 | 5 | 0% |
| arm-dts-sun5i-a13-olinuxino-micro-add-panel-lcd-olinuxino-4.3.patch | 4 | 0 | 4 | 0% |
| arm-dts-sun7i-a20-Disable-OOB-IRQ-for-brcm-wifi-on-Cubietruck-a.patch | 2 | 0 | 2 | 0% |
| arm-dts-sun7i-a20-bananapro-add-AXP209-regulators.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun7i-a20-bananapro-add-hdmi-connector-de.patch | 5 | 0 | 5 | 0% |
| arm-dts-sun7i-a20-cubietruck-add-alias-uart2.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun7i-a20-olimex-som-204-evb-olinuxino-micro-decrease-d.patch | 3 | 1 | 2 | 33% |
| arm-dts-sun7i-a20-olinuxino-lime2-enable-audio-codec.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun7i-a20-olinuxino-lime2-enable-ldo3-always-on.patch | 1 | 1 | 0 | 100% |
| arm-dts-sun7i-a20-olinuxino-micro-emmc-Add-vqmmc-node.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun8i-h2-plus-orangepi-zero-fix-usb_otg-dr_mode.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun8i-h2-plus-orangepi-zero-fix-xradio-interrupt.patch | 2 | 0 | 2 | 0% |
| arm-dts-sun8i-h3-add-thermal-zones.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun8i-h3-bananapi-m2-plus-add-wifi_pwrseq.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun8i-h3-nanopi-add-leds-pio-pins.patch | 3 | 0 | 3 | 0% |
| arm-dts-sun8i-h3-orangepi-pc-plus-add-wifi_pwrseq.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun8i-h3-reduce-opp-microvolt-to-prevent-not-supported-.patch | 2 | 0 | 2 | 0% |
| arm-dts-sun8i-r40-add-clk_out_a-fix-bananam2ultra.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun8i-r40-bananapi-m2-ultra-add-codec-analog.patch | 2 | 0 | 2 | 0% |
| arm-dts-sun8i-v3s-s3-pinecube-enable-sound-codec.patch | 2 | 0 | 2 | 0% |
| arm-dts-sun9i-a80-add-thermal-sensor.patch | 1 | 0 | 1 | 0% |
| arm-dts-sun9i-a80-add-thermal-zone.patch | 1 | 0 | 1 | 0% |
| arm-dts-sunxi-h3-h5.dtsi-add-i2s0-i2s1-pins.patch | 1 | 0 | 1 | 0% |
| arm-dts-sunxi-h3-h5.dtsi-force-mmc0-bus-width.patch | 1 | 0 | 1 | 0% |
| arm-patch-call-flush_icache-ASAP-after-writing-new-instruction.patch | 1 | 1 | 0 | 100% |
| arm64-allwinner-Add-sun50i-h618-bananapi-m4-berry-support.patch | 2 | 0 | 2 | 0% |
| arm64-allwinner-dts-a64-enable-K101-IM2BYL02-panel-for-PineTab.patch | 1 | 0 | 1 | 0% |
| arm64-dts-Add-sun50i-h5-nanopi-k1-plus-device.patch | 1 | 0 | 1 | 0% |
| arm64-dts-Add-sun50i-h5-nanopi-m1-plus2-device.patch | 1 | 0 | 1 | 0% |
| arm64-dts-Add-sun50i-h5-nanopi-neo-core2-device.patch | 1 | 0 | 1 | 0% |
| arm64-dts-Add-sun50i-h5-nanopi-neo2-v1.1-device.patch | 1 | 0 | 1 | 0% |
| arm64-dts-FIXME-a64-olinuxino-add-regulator-audio-mmc.patch | 5 | 0 | 5 | 0% |
| arm64-dts-add-sun50i-h618-cpu-dvfs.dtsi.patch | 5 | 0 | 5 | 0% |
| arm64-dts-allwinner-Add-axp313a.dtsi.patch | 1 | 0 | 1 | 0% |
| arm64-dts-allwinner-Enforce-consistent-MMC-numbering.patch | 3 | 0 | 3 | 0% |
| arm64-dts-allwinner-a64-Add-hdmi-sound-card.patch | 2 | 1 | 1 | 50% |
| arm64-dts-allwinner-a64-Enable-hdmi-sound-card-on-boards-with-h.patch | 14 | 0 | 14 | 0% |
| arm64-dts-allwinner-a64-Fix-LRADC-compatible.patch | 1 | 0 | 1 | 0% |
| arm64-dts-allwinner-a64-pinetab-add-front-camera.patch | 4 | 0 | 4 | 0% |
| arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch | 7 | 0 | 7 | 0% |
| arm64-dts-allwinner-h6-Add-AC200-EPHY-nodes.patch | 6 | 0 | 6 | 0% |
| arm64-dts-allwinner-h6-Add-hdmi-sound-card.patch | 3 | 1 | 2 | 33% |
| arm64-dts-allwinner-h6-Enable-hdmi-sound-card-on-boards-with-hd.patch | 8 | 0 | 8 | 0% |
| arm64-dts-allwinner-h6-add-AC200-codec-nodes.patch | 4 | 0 | 4 | 0% |
| arm64-dts-allwinner-h6-enable-AC200-codec.patch | 7 | 0 | 7 | 0% |
| arm64-dts-allwinner-h6-tanix-enable-Ethernet.patch | 5 | 0 | 5 | 0% |
| arm64-dts-allwinner-h616-orangepi-zero2-Enable-expansion-board-.patch | 2 | 0 | 2 | 0% |
| arm64-dts-allwinner-orange-pi-3-Enable-ethernet.patch | 4 | 0 | 4 | 0% |
| arm64-dts-allwinner-overlay-Add-Overlays-for-sunxi64.patch | 48 | 0 | 48 | 0% |
| arm64-dts-allwinner-sun50i-h6-Fix-H6-emmc.patch | 1 | 0 | 1 | 0% |
| arm64-dts-allwinner-sun50i-h616-Add-VPU-node.patch | 2 | 0 | 2 | 0% |
| arm64-dts-h616-8-Add-overlays-i2c-pwm-uart.patch | 25 | 0 | 25 | 0% |
| arm64-dts-h616-add-hdmi-support-for-zero2-and-zero3.patch | 9 | 0 | 9 | 0% |
| arm64-dts-h616-add-wifi-support-for-orange-pi-zero-2-and-zero3.patch | 2 | 0 | 2 | 0% |
| arm64-dts-nanopi-a64-set-right-phy-mode-to-rgmii-id.patch | 1 | 0 | 1 | 0% |
| arm64-dts-overlay-sun50i-a64-pine64-7inch-lcd.patch | 4 | 0 | 4 | 0% |
| arm64-dts-overlay-sun50i-h5-add-gpio-regulator-overclock.patch | 5 | 0 | 5 | 0% |
| arm64-dts-rk3399-Add-dmc_opp_table.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50-a64-pinephone-Define-jack-pins-in-DT.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-Define-orientation-and-rotation-for-PinePhone-.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-Set-fifo-size-for-uarts.patch | 5 | 0 | 5 | 0% |
| arm64-dts-sun50i-a64-force-mmc0-bus-width.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-olinuxino-1Ge16GW-Disable-clock-phase-and-.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-olinuxino-1Ge16GW-enable-bluetooth.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-olinuxino-add-boards.patch | 5 | 0 | 5 | 0% |
| arm64-dts-sun50i-a64-olinuxino-emmc-enable-bluetooth.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-orangepi-win-add-aliase-ethernet1.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pine64-add-spi0.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pine64-enable-wifi-mmc1.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-Type-C-support-for-all-PP-va.patch | 11 | 0 | 11 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-detailed-OCV-to-capactiy-con.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-front-back-cameras.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-interrupt-pin-for-WiFi.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-modem-power-manager.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-power-supply-to-stk3311.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-reboot-mode-driver.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-supply-for-i2c-bus-to-anx768.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-support-for-Bluetooth-audio.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-support-for-Pinephone-1.2-be.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-support-for-Pinephone-keyboa.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-a64-pinephone-Bump-I2C-frequency-to-400kHz.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-a64-pinephone-Don-t-make-lradc-keys-a-wakeup-s.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinephone-Enable-Pinephone-Keyboard-power-.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinephone-Enable-internal-HMIC-bias.patch | 1 | 1 | 0 | 100% |
| arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinephone-Power-off-the-touch-controller-i.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinephone-Set-minimum-backlight-duty-cycle.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-a64-pinephone-Shorten-post-power-on-delay-on-m.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-a64-pinephone-Workaround-broken-HDMI-HPD-signa.patch | 6 | 0 | 6 | 0% |
| arm64-dts-sun50i-a64-pinetab-Add-accelerometer.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinetab-Name-sound-card-PineTab.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-pinetab-enable-RTL8723CS-bluetooth.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-sopine-baseboard-enable-Bluetooth.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-a64-sopine-baseboard-mmc1-status-okay.patch | 1 | 1 | 0 | 100% |
| arm64-dts-sun50i-a64.dtsi-adjust-thermal-trip-points.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h313-x96q-lpddr3.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-h5-Add-missing-GPU-trip-point.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h5-Use-my-own-more-aggressive-OPPs-on-H5.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h5-add-cpu-opp-refs.patch | 9 | 0 | 9 | 0% |
| arm64-dts-sun50i-h5-add-termal-zones.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h5-enable-power-button-for-orangepi-prime.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h5-nanopi-neo2-add-regulator-led-triger.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-h5-nanopi-r1s-h5-add-rtl8153-support.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-h5-orangepi-pc2-add-spi-flash.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h5-orangepi-prime-add-regulator.patch | 4 | 1 | 3 | 25% |
| arm64-dts-sun50i-h5-orangepi-prime-add-rtl8723cs.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-h5-orangepi-zero-plus-add-regulator.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-h6-Add-r_uart-uart2-3-pins.patch | 6 | 3 | 3 | 50% |
| arm64-dts-sun50i-h6-orangepi-3-add-r_uart-aliase.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h6-orangepi-3-delete-node-spi0.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h6-orangepi-add-cpu-opp-refs.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-h6-orangepi-enable-higher-clock-regulator-max-.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h6-orangepi-lite2-spi0-usb3phy-dwc3-enable.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-h6-pine-h64-add-dwc3-usb3phy.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-h6-pine-h64-add-wifi-rtl8723cs.patch | 3 | 1 | 2 | 33% |
| arm64-dts-sun50i-h6.dtsi-add-pinctrl-pins-for-spi.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-h6.dtsi-improve-thermals.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-h616-add-pwm-nodes-support.patch | 2 | 0 | 2 | 0% |
| arm64-dts-sun50i-h616-bigtreetech-cb1-sd-emmc.patch | 12 | 0 | 12 | 0% |
| arm64-dts-sun50i-h616-orangepi-zero2-Enable-GPU-mali.patch | 1 | 1 | 0 | 100% |
| arm64-dts-sun50i-h616-orangepi-zero2-reg_usb1_vbus-status-ok.patch | 1 | 1 | 0 | 100% |
| arm64-dts-sun50i-h616-x96-mate-T95-eth-sd-card-hack.patch | 4 | 0 | 4 | 0% |
| arm64-dts-sun50i-h616-x96-mate-add-hdmi.patch | 3 | 0 | 3 | 0% |
| arm64-dts-sun50i-h616.dtsi-reserved-memory-512K-for-BL31.patch | 1 | 0 | 1 | 0% |
| arm64-dts-sun50i-h618-orangepi-zero2w-Add-missing-nodes.patch | 9 | 0 | 9 | 0% |
| arm64-dts-sun50i-h618-orangepi-zero3-Enable-GPU-mali.patch | 1 | 1 | 0 | 100% |
| arm64-sun50i-h616-Add-i2c-2-3-4-uart-2-5-pins.patch | 2 | 0 | 2 | 0% |
| arm64-xor-Select-32regs-without-benchmark-to-speed-up-boot.patch | 1 | 0 | 1 | 0% |
| bluetooth-bcm-Restore-drive_rts_on_open-true-behavior-on-bcm207.patch | 1 | 0 | 1 | 0% |
| bluetooth-h5-Don-t-re-initialize-rtl8723cs-on-resume.patch | 1 | 1 | 0 | 100% |
| cb1-overlay.patch | 12 | 0 | 12 | 0% |
| clk-gate-add-support-for-regmap-based-gates.patch | 15 | 0 | 15 | 0% |
| clk-sunxi-ng-Don-t-use-CPU-PLL-gating-and-CPUX-reparenting-to-H.patch | 2 | 0 | 2 | 0% |
| clk-sunxi-ng-Export-CLK_DRAM-for-devfreq.patch | 3 | 0 | 3 | 0% |
| clk-sunxi-ng-Mark-TWD-clocks-as-critical.patch | 3 | 0 | 3 | 0% |
| clk-sunxi-ng-Set-maximum-P-and-M-factors-to-1-for-H3-pll-cpux-c.patch | 1 | 0 | 1 | 0% |
| clk-sunxi-ng-a64-Increase-PLL_AUDIO-base-frequency.patch | 3 | 0 | 3 | 0% |
| clk-sunxi-ng-sun50i-a64-Switch-parent-of-MIPI-DSI-to-periph0-1x.patch | 2 | 0 | 2 | 0% |
| cpufreq-sun50i-Show-detected-CPU-bin-for-easier-debugging.patch | 1 | 0 | 1 | 0% |
| dma-sun6i-dma-add-sun50i-h616-support.patch | 2 | 1 | 1 | 50% |
| driver-allwinner-h618-emac.patch | 16 | 0 | 16 | 0% |
| drivers-devfreq-sun8i-a33-mbus-disable-autorefresh.patch | 1 | 0 | 1 | 0% |
| drivers-pwm-Add-pwm-sunxi-enhance-driver-for-h616.patch | 4 | 0 | 4 | 0% |
| drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch | 9 | 0 | 9 | 0% |
| drm-bridge-dw-hdmi-Report-HDMI-hotplug-events.patch | 2 | 0 | 2 | 0% |
| drm-panel-st7703-Fix-xbd599-timings-to-make-refresh-rate-exactl.patch | 1 | 0 | 1 | 0% |
| drm-sun4i-Implement-gamma-correction.patch | 6 | 0 | 6 | 0% |
| drm-sun4i-Report-page-flip-after-vsync-is-complete-not-in-the-m.patch | 8 | 0 | 8 | 0% |
| drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch | 40 | 0 | 40 | 0% |
| drm-sun4i-add-sun50i-h616-hdmi-phy-support.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-de2-Initialize-layer-fields-earlier.patch | 4 | 2 | 2 | 50% |
| drm-sun4i-de2-de3-Change-CSC-argument.patch | 10 | 0 | 10 | 0% |
| drm-sun4i-de2-de3-Merge-CSC-functions-into-one.patch | 5 | 0 | 5 | 0% |
| drm-sun4i-de2-de3-add-generic-blender-register-reference-functi.patch | 1 | 0 | 1 | 0% |
| drm-sun4i-de2-de3-add-mixer-version-enum.patch | 23 | 1 | 22 | 4% |
| drm-sun4i-de2-de3-call-csc-setup-also-for-UI-layer.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-de2-de3-refactor-mixer-initialisation.patch | 5 | 1 | 4 | 20% |
| drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch | 9 | 9 | 0 | 100% |
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
| drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch | 13 | 8 | 5 | 61% |
| drm-sun4i-de33-vi_scaler-add-Display-Engine-3.3-DE33-support.patch | 3 | 1 | 2 | 33% |
| drm-sun4i-support-YUV-formats-in-VI-scaler.patch | 3 | 0 | 3 | 0% |
| drm-sun4i-tcon-Support-keeping-dclk-rate-upon-ancestor-clock-ch.patch | 9 | 0 | 9 | 0% |
| drm-sun4i-vi_scaler-refactor-vi_scaler-enablement.patch | 5 | 0 | 5 | 0% |
| drv-clocksource-arm_arch_timer-fix-a64-timejump.patch | 1 | 0 | 1 | 0% |
| drv-gpu-drm-gem-dma-Export-with-handle-allocator.patch | 3 | 1 | 2 | 33% |
| drv-gpu-drm-panel-simple-Add-compability-olinuxino-lcd.patch | 4 | 0 | 4 | 0% |
| drv-gpu-drm-sun4i-Add-GEM-allocator.patch | 4 | 0 | 4 | 0% |
| drv-gpu-drm-sun4i-Add-HDMI-audio-sun4i-hdmi-encoder.patch | 11 | 0 | 11 | 0% |
| drv-gpu-drm-sun4i-sun8i_mixer.c-add-h3-mixer1.patch | 2 | 1 | 1 | 50% |
| drv-iio-adc-axp20x_adc-arm64-dts-axp803-hwmon-enable-thermal.patch | 10 | 0 | 10 | 0% |
| drv-input-touchscreen-sun4i-ts-Enable-parsing.patch | 4 | 0 | 4 | 0% |
| drv-media-dvb-frontends-si2168-fix-cmd-timeout.patch | 1 | 0 | 1 | 0% |
| drv-mfd-axp20x-add-sysfs-interface.patch | 4 | 0 | 4 | 0% |
| drv-mmc-host-sunxi-mmc-Disable-DDR52-mode-on-all-A20-based-boar.patch | 1 | 0 | 1 | 0% |
| drv-mmc-host-sunxi-mmc-add-h5-emmc-compatible.patch | 2 | 0 | 2 | 0% |
| drv-mtd-nand-raw-nand_ids.c-add-H27UBG8T2BTR-BC-nand.patch | 1 | 0 | 1 | 0% |
| drv-net-stmmac-dwmac-sun8i-second-EMAC-clock-register.patch | 3 | 0 | 3 | 0% |
| drv-nvmem-sunxi_sid-Support-SID-on-H616.patch | 2 | 1 | 1 | 50% |
| drv-of-Device-Tree-Overlay-ConfigFS-interface.patch | 4 | 1 | 3 | 25% |
| drv-phy-sun4i-usb-Allow-reset-line-to-be-shared.patch | 1 | 0 | 1 | 0% |
| drv-pinctrl-pinctrl-sun50i-a64-disable_strict_mode.patch | 1 | 0 | 1 | 0% |
| drv-pinctrl-sunxi-pinctrl-sun50i-h6.c-GPIO-disable_strict_mode.patch | 1 | 0 | 1 | 0% |
| drv-soc-sunxi-sram-Add-SRAM-C1-H616-handling.patch | 2 | 0 | 2 | 0% |
| drv-spi-spi-sun4i.c-spi-bug-low-on-sck.patch | 2 | 1 | 1 | 50% |
| drv-spi-spidev-Add-armbian-spi-dev-compatible.patch | 2 | 0 | 2 | 0% |
| drv-staging-media-sunxi-cedrus-add-H616-variant.patch | 2 | 1 | 1 | 50% |
| drv-staging-rtl8723bs-AP-bugfix.patch | 1 | 0 | 1 | 0% |
| drv-usb-gadget-composite-rename-gadget-serial-console-manufactu.patch | 1 | 0 | 1 | 0% |
| dt-bindings-allwinner-add-H616-DE33-bus-binding.patch | 1 | 0 | 1 | 0% |
| dt-bindings-allwinner-add-H616-DE33-mixer-binding.patch | 1 | 1 | 0 | 100% |
| dt-bindings-axp20x-adc-allow-to-use-TS-pin-as-GPADC.patch | 1 | 0 | 1 | 0% |
| dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch | 1 | 0 | 1 | 0% |
| dt-bindings-leds-Add-a-binding-for-AXP813-charger-led.patch | 1 | 0 | 1 | 0% |
| dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch | 1 | 0 | 1 | 0% |
| dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch | 2 | 0 | 2 | 0% |
| dt-bindings-sound-Add-jack-type-property-to-sun8i-a33-codec.patch | 1 | 0 | 1 | 0% |
| enable-TV-Output-on-OrangePi-Zero-LTE.patch | 32 | 1 | 31 | 3% |
| firmware-arm_scpi-Support-unidirectional-mailbox-channels.patch | 6 | 0 | 6 | 0% |
| firmware-scpi-Add-support-for-sending-a-SCPI_CMD_SET_SYS_PWR_ST.patch | 6 | 0 | 6 | 0% |
| fix-cpu-opp-table-sun8i-a83t.patch | 2 | 0 | 2 | 0% |
| gnss-ubx-Send-soft-powerdown-message-on-suspend.patch | 1 | 0 | 1 | 0% |
| h616-add-keys.patch | 5 | 1 | 4 | 20% |
| hm5065-yaml-bindings-wip.patch | 1 | 0 | 1 | 0% |
| i2c-mv64xxx-Don-t-make-a-fuss-when-pinctrl-recovery-state-is-no.patch | 1 | 0 | 1 | 0% |
| iio-adc-axp20x_adc-allow-to-set-TS-pin-to-GPADC-mode.patch | 2 | 0 | 2 | 0% |
| iio-adc-sun4i-gpadc-iio-Allow-to-use-sun5i-a13-gpadc-iio-from-D.patch | 3 | 0 | 3 | 0% |
| iio-st_sensors-Don-t-report-error-when-the-device-is-not-presen.patch | 1 | 0 | 1 | 0% |
| include-uapi-drm_fourcc-add-ARM-tiled-format-modifier.patch | 1 | 0 | 1 | 0% |
| input-cyttsp4-Clear-the-ids-buffer-in-a-saner-way.patch | 1 | 0 | 1 | 0% |
| input-cyttsp4-De-obfuscate-MT-signals-setup-platform-data.patch | 8 | 0 | 8 | 0% |
| input-cyttsp4-De-obfuscate-platform-data-for-keys.patch | 4 | 0 | 4 | 0% |
| input-cyttsp4-ENOSYS-error-is-ok-when-powering-up.patch | 1 | 0 | 1 | 0% |
| input-cyttsp4-Faster-recovery-from-failed-wakeup-HACK.patch | 1 | 0 | 1 | 0% |
| input-cyttsp4-Fix-compile-issue.patch | 1 | 0 | 1 | 0% |
| input-cyttsp4-Fix-probe-oops.patch | 1 | 0 | 1 | 0% |
| input-cyttsp4-Fix-warnings.patch | 3 | 0 | 3 | 0% |
| input-cyttsp4-Make-the-driver-not-hog-the-system-s-workqueue.patch | 8 | 0 | 8 | 0% |
| input-cyttsp4-Port-the-driver-to-use-device-properties.patch | 26 | 0 | 26 | 0% |
| input-cyttsp4-Port-to-6.16.patch | 1 | 0 | 1 | 0% |
| input-cyttsp4-Remove-unused-enable_vkeys.patch | 1 | 0 | 1 | 0% |
| input-cyttsp4-Remove-useless-indirection-with-driver-platform-d.patch | 34 | 0 | 34 | 0% |
| input-cyttsp4-Restart-on-wakeup-wakeup-by-I2C-read-doesn-t-work.patch | 9 | 0 | 9 | 0% |
| input-cyttsp4-Use-i2c-spi-names-directly-in-the-driver.patch | 3 | 0 | 3 | 0% |
| input-gpio-vibra-Allow-to-use-vcc-supply-alone-to-control-the-v.patch | 3 | 0 | 3 | 0% |
| leds-axp20x-Support-charger-LED-on-AXP20x-like-PMICs.patch | 5 | 0 | 5 | 0% |
| mailbox-Allow-to-run-mailbox-while-timekeeping-is-suspended.patch | 2 | 0 | 2 | 0% |
| media-Add-NV12-and-P010-AFBC-compressed-formats.patch | 2 | 0 | 2 | 0% |
| media-cedrus-Don-t-CPU-map-source-buffers.patch | 1 | 0 | 1 | 0% |
| media-cedrus-Fix-failure-to-clean-up-hardware-on-probe-failure.patch | 2 | 0 | 2 | 0% |
| media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch | 7 | 0 | 7 | 0% |
| media-cedrus-Increase-H6-clock-rate.patch | 1 | 0 | 1 | 0% |
| media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch | 2 | 0 | 2 | 0% |
| media-gc2145-Add-PIXEL_RATE-HBLANK-and-VBLANK-controls.patch | 8 | 1 | 7 | 12% |
| media-gc2145-Added-BGGR-bayer-mode.patch | 1 | 0 | 1 | 0% |
| media-gc2145-Disable-debug-output.patch | 2 | 0 | 2 | 0% |
| media-gc2145-Galaxycore-camera-module-driver.patch | 3 | 1 | 2 | 33% |
| media-gc2145-fix-white-balance-colors.patch | 3 | 0 | 3 | 0% |
| media-gc2145-implement-system-suspend.patch | 2 | 0 | 2 | 0% |
| media-hm5065-Add-subdev-driver-for-Himax-HM5065-camera-sensor.patch | 3 | 0 | 3 | 0% |
| media-i2c-gc2145-Move-upstream-driver-out-of-the-way.patch | 2 | 0 | 2 | 0% |
| media-i2c-gc2145-Parse-and-register-properties.patch | 2 | 1 | 1 | 50% |
| media-ov5640-Add-read-only-property-for-vblank.patch | 1 | 0 | 1 | 0% |
| media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch | 5 | 3 | 2 | 60% |
| media-ov5640-Experiment-Try-to-disable-denoising-sharpening.patch | 2 | 0 | 2 | 0% |
| media-ov5640-Fix-focus-commands-blocking-until-complete.patch | 4 | 0 | 4 | 0% |
| media-ov5640-Implement-autofocus.patch | 13 | 0 | 13 | 0% |
| media-ov5640-Improve-error-reporting.patch | 2 | 0 | 2 | 0% |
| media-ov5640-Improve-firmware-load-time.patch | 7 | 0 | 7 | 0% |
| media-ov5640-Sleep-after-poweroff-to-ensure-next-poweron-is-not.patch | 1 | 0 | 1 | 0% |
| media-ov5640-set-default-ae-target-lower.patch | 1 | 0 | 1 | 0% |
| media-ov5640-use-pm_runtime_force_suspend-resume-for-system-sus.patch | 1 | 0 | 1 | 0% |
| media-ov5648-Fix-call-to-pm_runtime_set_suspended.patch | 1 | 1 | 0 | 100% |
| media-sun6i-csi-Add-multicamera-support-for-parallel-bus.patch | 10 | 1 | 9 | 10% |
| media-sun6i-csi-add-V4L2_CAP_IO_MC-capability.patch | 2 | 0 | 2 | 0% |
| media-sun6i-csi-capture-Use-subdev-operation-to-access-bridge-f.patch | 5 | 0 | 5 | 0% |
| media-sun6i-csi-implement-vidioc_enum_framesizes.patch | 2 | 0 | 2 | 0% |
| media-sun6i-csi-merge-sun6i_csi_formats-and-sun6i_csi_formats_m.patch | 8 | 1 | 7 | 12% |
| media-sun6i-csi-subdev-Use-subdev-active-state-to-store-active-.patch | 16 | 0 | 16 | 0% |
| mfd-Add-support-for-X-Powers-AC200-EPHY-syscon.patch | 3 | 0 | 3 | 0% |
| mfd-Add-support-for-X-Powers-AC200.patch | 3 | 0 | 3 | 0% |
| mfd-axp20x-Add-battery-IRQ-resources.patch | 7 | 0 | 7 | 0% |
| misc-modem-power-Power-manager-for-modems.patch | 3 | 0 | 3 | 0% |
| mmc-add-delay-after-power-class-selection.patch | 2 | 0 | 2 | 0% |
| mmc-host-sunxi-mmc-Fix-H6-emmc.patch | 3 | 0 | 3 | 0% |
| mmc-sunxi-mmc-Remove-runtime-PM.patch | 8 | 0 | 8 | 0% |
| mtd-spi-nor-Add-Alliance-memory-support.patch | 4 | 0 | 4 | 0% |
| mtd-spi-nor-Add-vdd-regulator-support.patch | 1 | 0 | 1 | 0% |
| net-phy-Add-support-for-AC200-EPHY.patch | 3 | 0 | 3 | 0% |
| net-stmmac-sun8i-Add-support-for-enabling-a-regulator-for-PHY-I.patch | 6 | 0 | 6 | 0% |
| net-stmmac-sun8i-Rename-PHY-regulator-variable-to-regulator_phy.patch | 6 | 0 | 6 | 0% |
| net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch | 4 | 3 | 1 | 75% |
| net-usb-r8152-add-LED-configuration-from-OF.patch | 5 | 0 | 5 | 0% |
| nfc-pn544-Add-support-for-VBAT-PVDD-regulators.patch | 8 | 0 | 8 | 0% |
| nvmem-sunxi_sid-add-sunxi_get_soc_chipid-sunxi_get_serial.patch | 2 | 0 | 2 | 0% |
| of-property-fw_devlink-Support-allwinner-sram-links.patch | 2 | 0 | 2 | 0% |
| opp-core-Avoid-confusing-error-when-no-regulator-is-defined-in-.patch | 1 | 0 | 1 | 0% |
| pci-Workaround-ITS-timeouts-on-poweroff-reboot-on-Orange-Pi-5-P.patch | 1 | 1 | 0 | 100% |
| phy-allwinner-sun4i-usb-Add-support-for-usb_role_switch.patch | 10 | 0 | 10 | 0% |
| power-axp20x_battery-Allow-to-set-target-voltage-to-4.35V.patch | 1 | 0 | 1 | 0% |
| power-axp803-Add-interrupts-for-low-battery-power-condition.patch | 2 | 0 | 2 | 0% |
| power-supply-Add-support-for-USB_BC_ENABLED-and-USB_DCP_INPUT_C.patch | 2 | 0 | 2 | 0% |
| power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch | 5 | 1 | 4 | 20% |
| power-supply-axp20x-battery-Enable-poweron-by-RTC-alarm.patch | 1 | 0 | 1 | 0% |
| power-supply-axp20x-battery-Improve-probe-error-reporting.patch | 2 | 0 | 2 | 0% |
| power-supply-axp20x-battery-Support-POWER_SUPPLY_PROP_CHARGE_BE.patch | 5 | 1 | 4 | 20% |
| power-supply-axp20x-usb-power-Add-missing-interrupts.patch | 3 | 0 | 3 | 0% |
| power-supply-axp20x-usb-power-Change-Vbus-hold-voltage-to-4.5V.patch | 1 | 0 | 1 | 0% |
| power-supply-axp20x_battery-Add-support-for-reporting-OCV.patch | 3 | 0 | 3 | 0% |
| power-supply-axp20x_battery-Fix-charging-done-detection.patch | 2 | 0 | 2 | 0% |
| power-supply-axp20x_battery-Monitor-battery-health.patch | 6 | 0 | 6 | 0% |
| power-supply-axp20x_battery-Send-uevents-for-status-changes.patch | 10 | 0 | 10 | 0% |
| power-supply-axp20x_battery-Setup-thermal-regulation-experiment.patch | 1 | 0 | 1 | 0% |
| regulator-Add-simple-driver-for-enabling-a-regulator-from-users.patch | 3 | 0 | 3 | 0% |
| regulator-axp20x-Add-support-for-vin-supply-for-drivevbus.patch | 1 | 0 | 1 | 0% |
| regulator-axp20x-Enable-over-temperature-protection-and-16s-res.patch | 2 | 0 | 2 | 0% |
| regulator-axp20x-Turn-N_VBUSEN-to-input-on-x-powers-sense-vbus-.patch | 2 | 0 | 2 | 0% |
| regulator-tp65185-Add-hwmon-device-for-reading-temperature.patch | 11 | 0 | 11 | 0% |
| regulator-tp65185x-Add-tp65185x-eInk-panel-regulator-driver.patch | 3 | 0 | 3 | 0% |
| rtc-Print-which-error-caused-RTC-read-failure.patch | 1 | 0 | 1 | 0% |
| rtc-sun6i-Allow-RTC-wakeup-after-shutdown.patch | 5 | 0 | 5 | 0% |
| scripts-add-overlay-compilation-support.patch | 4 | 0 | 4 | 0% |
| sound-soc-ac100-codec-Support-analog-part-of-X-Powers-AC100-cod.patch | 5 | 0 | 5 | 0% |
| sound-soc-sun8i-codec-Add-support-for-digital-part-of-the-AC100.patch | 15 | 0 | 15 | 0% |
| sound-soc-sunxi-Provoke-the-early-load-of-sun8i-codec-analog.patch | 1 | 1 | 0 | 100% |
| sound-soc-sunxi-sun4i-codec-adcis-select-capture-source.patch | 7 | 0 | 7 | 0% |
| sound-soc-sunxi-sun8i-codec-analog-enable-sound.patch | 1 | 0 | 1 | 0% |
| sun50i-h616-Add-the-missing-digital-audio-node.patch | 2 | 0 | 2 | 0% |
| sunxi-Use-dev_err_probe-to-handle-EPROBE_DEFER-errors.patch | 9 | 0 | 9 | 0% |
| thermal-sun8i-Be-loud-when-probe-fails.patch | 5 | 0 | 5 | 0% |
| usb-gadget-Fix-dangling-pointer-in-netdev-private-data.patch | 18 | 2 | 16 | 11% |
| usb-musb-sunxi-Avoid-enabling-host-side-code-on-SoCs-where-it-s.patch | 4 | 1 | 3 | 25% |
| usb-serial-option-add-reset_resume-callback-for-WWAN-devices.patch | 1 | 0 | 1 | 0% |
| usb-typec-altmodes-displayport-Respect-DP_CAP_RECEPTACLE-bit.patch | 2 | 0 | 2 | 0% |
| usb-typec-anx7688-Add-driver-for-ANX7688-USB-C-HDMI-bridge.patch | 4 | 0 | 4 | 0% |
| usb-typec-fusb302-Add-OF-extcon-support.patch | 1 | 0 | 1 | 0% |
| usb-typec-fusb302-Clear-interrupts-before-we-start-toggling.patch | 2 | 0 | 2 | 0% |
| usb-typec-fusb302-Extend-debugging-interface-with-driver-state-.patch | 2 | 0 | 2 | 0% |
| usb-typec-fusb302-Fix-register-definitions.patch | 2 | 0 | 2 | 0% |
| usb-typec-fusb302-More-useful-of-logging-status-on-interrupt.patch | 5 | 0 | 5 | 0% |
| usb-typec-fusb302-Retry-reading-of-CC-pins-status-if-activity-i.patch | 3 | 0 | 3 | 0% |
| usb-typec-fusb302-Set-the-current-before-enabling-pullups.patch | 2 | 1 | 1 | 50% |
| usb-typec-fusb302-Slightly-increase-wait-time-for-BC1.2-result.patch | 1 | 0 | 1 | 0% |
| usb-typec-fusb302-Update-VBUS-state-even-if-VBUS-interrupt-is-n.patch | 1 | 1 | 0 | 100% |
| usb-typec-tcpm-Fix-PD-devices-capabilities-registration.patch | 3 | 0 | 3 | 0% |
| usb-typec-tcpm-Improve-logs.patch | 4 | 0 | 4 | 0% |
| usb-typec-tcpm-Unregister-altmodes-before-registering-new-ones.patch | 1 | 1 | 0 | 100% |
| usb-typec-typec-extcon-Add-typec-extcon-bridge-driver.patch | 3 | 0 | 3 | 0% |
| usb-typec-typec-extcon-Allow-to-force-reset-on-each-mux-change.patch | 2 | 0 | 2 | 0% |
| usb-typec-typec-extcon-Enable-debugging-for-now.patch | 1 | 0 | 1 | 0% |
| video-fbdev-eInk-display-driver-for-A13-based-PocketBooks.patch | 5 | 0 | 5 | 0% |
| video-pwm_bl-Allow-to-change-lth_brightness-via-sysfs.patch | 3 | 0 | 3 | 0% |

## Methodology

This analysis breaks down each patch into individual hunks (chunks of changes) and checks if the added code appears in the corresponding file in Linux kernel 6.18.

A hunk is considered "found" if at least 70% of its meaningful added lines (excluding empty lines and comments) are present in the kernel file.

**Note:** This is a content-based search and may not detect:
- Code that was modified during upstreaming
- Code in different files (refactored/moved)
- Functionally equivalent but differently written code
