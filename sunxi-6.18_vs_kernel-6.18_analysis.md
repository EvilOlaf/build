# Patch Analysis Report: sunxi-6.16 vs Linux Kernel 6.18

**Patch Directory:** `patch/kernel/archive/sunxi-6.18`

**Analysis Date:** 2025-12-07 04:17:42

## Summary

- **Total Patches Analyzed:** 444
- **Patches with Commit IDs:** 444
- **Unique Files Modified:** 596

## Patches by Subsystem

| Subsystem | Count |
|-----------|-------|
| arch | 208 |
| drivers | 199 |
| sound | 14 |
| Documentation | 10 |
| include | 9 |
| other | 2 |
| scripts | 2 |

## Patches by Directory

| Directory | Count |
|-----------|-------|
| patches.megous | 236 |
| patches.armbian | 176 |
| patches.drm | 26 |
| patches.media | 6 |

## Most Frequently Modified Files (Top 20)

These files are modified by multiple patches and might indicate areas of active development:

| File | Patches |
|------|--------|
| `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone.dtsi` | 19 |
| `drivers/input/touchscreen/cyttsp4_core.c` | 14 |
| `arch/arm64/boot/dts/allwinner/sun50i-h616.dtsi` | 13 |
| `drivers/power/supply/axp20x_battery.c` | 11 |
| `arch/arm/boot/dts/allwinner/sun8i-a83t.dtsi` | 11 |
| `drivers/media/i2c/ov5640.c` | 10 |
| `arch/arm64/boot/dts/allwinner/sun50i-h6.dtsi` | 10 |
| `arch/arm64/boot/dts/allwinner/overlay/Makefile` | 10 |
| `arch/arm/boot/dts/allwinner/sun8i-a83t-tbs-a711.dts` | 9 |
| `drivers/gpu/drm/sun4i/sun8i_mixer.c` | 9 |
| `drivers/usb/typec/tcpm/fusb302.c` | 8 |
| `drivers/media/i2c/gc2145.c` | 7 |
| `include/linux/platform_data/cyttsp4.h` | 7 |
| `arch/arm64/boot/dts/allwinner/sun50i-h616-orangepi-zero.dtsi` | 7 |
| `drivers/gpu/drm/sun4i/sun8i_csc.c` | 7 |
| `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | 7 |
| `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone-1.1.dts` | 6 |
| `arch/arm64/boot/dts/allwinner/sun50i-h6-orangepi-3.dts` | 6 |
| `arch/arm/boot/dts/allwinner/sunxi-h3-h5.dtsi` | 6 |
| `arch/arm/boot/dts/allwinner/sun8i-h3.dtsi` | 6 |

## Detailed Patch List

Complete list of all patches, organized by directory:

### patches.armbian (176 patches)

| # | Patch File | Subject | Commit ID | Files Changed |
|---|------------|---------|-----------|---------------|
| 1 | `ARM-dts-sun8i-nanopiduo2-Use-key-0-as-power-button.patch` | ARM: dts: sun8i: nanopiduo2: Use key-0 as power bu... | `000000000000` | sun8i-h3-nanopi-duo2.dts |
| 2 | `ARM-dts-sun8i-nanopiduo2-enable-ethernet.patch` | ARM: dts: sun8i: nanopiduo2: enable ethernet | `000000000000` | sun8i-h3-nanopi-duo2.dts |
| 3 | `ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-EMAC1.patch` | ARM64: dts: sun50i-h616: BigTreeTech CB1: Enable E... | `000000000000` | sun50i-h616-bigtreetech-cb1.dtsi |
| 4 | `ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-HDMI.patch` | ARM64: dts: sun50i-h616: BigTreeTech CB1: Enable H... | `000000000000` | sun50i-h616-bigtreetech-cb1.dtsi |
| 5 | `ASoC-AC200-Initial-driver.patch` | ASoC: AC200: Initial driver | `000000000000` | ac200.c, Makefile (+1) |
| 6 | `Add-BananaPi-BPI-M4-Zero-overlays.patch` | Add BananaPi BPI-M4-Zero overlays | `000000000000` | sun50i-h616-bananapi-m4-pi-15-16-rts-cts-uart4.dtso, sun50i-h616-bananapi-m4-pi-5-6-i2c0.dtso (+12) |
| 7 | `Add-BananaPi-BPI-M4-Zero-pinctrl.patch` | Add BananaPi BPI-M4-Zero pinctrl | `000000000000` | sun50i-h616.dtsi |
| 8 | `Add-FB_TFT-ST7796S-driver.patch` | Add: FB_TFT ST7796S driver | `000000000000` | Makefile, fb_st7796s.c (+1) |
| 9 | `Add-HDMI-support-for-pcDuino-1-and-2-by-including-HDMI-and-DE-n.patch` | Add HDMI support for pcDuino 1 and 2 by including ... | `000000000000` | sun4i-a10-pcduino.dts |
| 10 | `Add-HDMI-support-for-pcDuino-3-by-including-HDMI-and-DE-nodes.patch` | Add HDMI support for pcDuino 3 by including HDMI a... | `000000000000` | sun7i-a20-pcduino3.dts |
| 11 | `Add-dump_reg-and-sunxi-sysinfo-drivers.patch` | Add dump_reg and sunxi-sysinfo drivers | `000000000000` | Makefile, Makefile (+8) |
| 12 | `Add-sunxi-addr-driver-Used-to-fix-uwe5622-bluetooth-MAC-address.patch` | Add sunxi-addr driver - Used to fix uwe5622 blueto... | `000000000000` | sha256.c, Makefile (+4) |
| 13 | `Add-wifi-nodes-for-Inovato-Quadra.patch` | Add wifi nodes for Inovato Quadra | `000000000000` | sun50i-h6-inovato-quadra.dts |
| 14 | `Add-ws2812-RGB-driver-for-allwinner-H616.patch` | Add: ws2812 RGB driver for allwinner H616 | `000000000000` | Kconfig, leds-ws2812.c (+1) |
| 15 | `BigTreeTech-CB1-dts-i2c-gpio-mode-adjustment-and-ws2812-rgb_val.patch` | BigTreeTech CB1: dts: i2c gpio mode adjustment and... | `000000000000` | sun50i-h616-bigtreetech-cb1.dtsi, sun50i-h616-bigtreetech-cb1-sd.dts (+1) |
| 16 | `Compile-the-pwm-overlay.patch` | Compile the pwm overlay | `000000000000` | Makefile |
| 17 | `Correct-perf-interrupt-source-number-as-referenced-in-the-Allwi.patch` | Correct perf interrupt source number as referenced... | `000000000000` | sun4i-a10.dtsi |
| 18 | `Doc-dt-bindings-usb-add-binding-for-DWC3-controller-on-Allwinne.patch` | Doc:dt-bindings:usb: add binding for DWC3 controll... | `000000000000` | allwinner,dwc3.txt |
| 19 | `Enable-DMA-support-for-the-Allwinner-A10-EMAC-which-already-exi.patch` | Enable DMA support for the Allwinner A10 EMAC, whi... | `000000000000` | sun4i-a10.dtsi |
| 20 | `Enable-creation-of-__symbols__-node.patch` | Enable creation of __symbols__ node | `000000000000` | Makefile.dtbs |
| 21 | `Fix-ghost-touches-on-tsc2007-tft-screen.patch` | Fix ghost touches on tsc2007 tft screen | `000000000000` | sun50i-h616-bigtreetech-cb1.dtsi, tsc2007_core.c (+2) |
| 22 | `Fix-include-uapi-spi-spidev-module.patch` | Fix include uapi spi spidev module | `000000000000` | spidev.c |
| 23 | `Input-axp20x-pek-allow-wakeup-after-shutdown.patch` | Input: axp20x-pek - allow wakeup after shutdown | `000000000000` | axp20x-pek.c |
| 24 | `LED-green_power_on-red_status_heartbeat-arch-arm64-boot-dts-all.patch` | LED-green_power_on-red_status_heartbeat | `000000000000` | sun50i-h616-orangepi-zero.dtsi |
| 25 | `Makefile-CONFIG_SHELL-fix-for-builddeb-packaging.patch` | Makefile: CONFIG_SHELL fix for builddeb packaging | `000000000000` | Makefile |
| 26 | `Move-sun50i-h6-pwm-settings-to-its-own-overlay.patch` | Move sun50i-h6-pwm settings to its own overlay | `000000000000` | sun50i-h6-pwm.dtso, sun50i-h6-fixup.scr-cmd |
| 27 | `Optimize-TSC2007-touchscreen-add-polling-method.patch` | Optimize: TSC2007 touchscreen add polling method | `000000000000` | tsc2007_core.c, tsc2007.h |
| 28 | `Revert-drm-sun4i-hdmi-switch-to-struct-drm_edid.patch` | Revert "drm/sun4i: hdmi: switch to struct drm_edid... | `000000000000` | sun4i_hdmi_enc.c |
| 29 | `Sound-for-H616-H618-Allwinner-SOCs.patch` | Sound for H616, H618 Allwinner SOCs | `000000000000` | Kconfig, Kconfig (+18) |
| 30 | `Temp_fix-mailbox-arch-arm64-boot-dts-allwinner-sun50i-a64-pinep.patch` | Temp_fix mailbox | `000000000000` | sun50i-a64-pinephone.dtsi |
| 31 | `add-dtb-overlay-for-zero2w.patch` | add dtb overlay for zero2w | `000000000000` | sun50i-h616-i2c0-pi.dtso, sun50i-h616-i2c1-pi.dtso (+3) |
| 32 | `add-initial-support-for-orangepi3-lts.patch` | add initial support for orangepi3-lts | `000000000000` | sun50i-h6-orangepi-3-lts.dts |
| 33 | `add-nodes-for-sunxi-info-sunxi-addr-and-sunxi-dump-reg.patch` | add nodes for sunxi-info, sunxi-addr and sunxi-dum... | `000000000000` | sun50i-h616.dtsi, sun50i-h6.dtsi |
| 34 | `arm-arm64-dts-Add-leds-axp20x-charger.patch` | arm:arm64:dts: Add leds axp20x charger | `000000000000` | axp209.dtsi, axp22x.dtsi (+2) |
| 35 | `arm-dts-Add-sun8i-h2-plus-nanopi-duo-device.patch` | arm:dts: Add sun8i-h2-plus-nanopi-duo device | `000000000000` | sun8i-h2-plus-nanopi-duo.dts |
| 36 | `arm-dts-Add-sun8i-h2-plus-sunvell-r69-device.patch` | arm:dts: Add sun8i-h2-plus-sunvell-r69 device | `000000000000` | sun8i-h2-plus-sunvell-r69.dts |
| 37 | `arm-dts-a10-cubiebord-a20-cubietruck-green-LED-mmc0-default-tri.patch` | arm:dts: a10-cubiebord a20-cubietruck green LED mm... | `000000000000` | sun4i-a10-cubieboard.dts, sun7i-a20-cubietruck.dts |
| 38 | `arm-dts-a20-orangepi-and-mini-fix-phy-mode-hdmi.patch` | arm:dts: a20-orangepi and mini fix phy-mode, hdmi | `000000000000` | sun7i-a20-orangepi.dts, sun7i-a20-orangepi-mini.dts |
| 39 | `arm-dts-h3-nanopi-neo-Add-regulator-leds-mmc2.patch` | arm:dts: h3-nanopi-neo Add regulator, leds, mmc2 | `000000000000` | sun8i-h3-nanopi-neo.dts |
| 40 | `arm-dts-h3-nanopi-neo-air-Add-regulator-camera-wifi-bluetooth-o.patch` | arm:dts: h3-nanopi-neo-air Add regulator camera wi... | `000000000000` | sun8i-h3-nanopi-neo-air.dts |
| 41 | `arm-dts-h3-orangepi-2-Add-regulator-vdd-cpu.patch` | arm:dts: h3-orangepi-2 Add regulator vdd cpu | `000000000000` | sun8i-h3-orangepi-2.dts |
| 42 | `arm-dts-overlay-Add-Overlays-for-sunxi.patch` | arm:dts:overlay Add Overlays for sunxi | `000000000000` | sun8i-r40-uart7.dtso, sun8i-h3-i2c2.dtso (+94) |
| 43 | `arm-dts-overlay-sun8i-h3-cpu-clock-add-overclock.patch` | arm:dts:overlay: sun8i-h3-cpu-clock add overclock | `000000000000` | Makefile, sun8i-h3-cpu-clock-1.2GHz-1.3v.dtso (+2) |
| 44 | `arm-dts-sun5i-a13-olinuxino-Add-panel-lcd-olinuxino-4.3-needed-.patch` | arm:dts:sun5i-a13-olinuxino Add panel lcd-olinuxin... | `000000000000` | sun5i-a13-olinuxino.dts |
| 45 | `arm-dts-sun5i-a13-olinuxino-micro-add-panel-lcd-olinuxino-4.3.patch` | arm:dts:sun5i-a13-olinuxino-micro add panel lcd-ol... | `000000000000` | sun5i-a13-olinuxino-micro.dts |
| 46 | `arm-dts-sun7i-a20-Disable-OOB-IRQ-for-brcm-wifi-on-Cubietruck-a.patch` | arm:dts:sun7i-a20 Disable OOB IRQ for brcm-wifi on... | `000000000000` | sun7i-a20-bananapro.dts, sun7i-a20-cubietruck.dts |
| 47 | `arm-dts-sun7i-a20-bananapro-add-AXP209-regulators.patch` | arm: dts: sun7i-a20-bananapro: add AXP209 regulato... | `000000000000` | sun7i-a20-bananapro.dts |
| 48 | `arm-dts-sun7i-a20-bananapro-add-hdmi-connector-de.patch` | arm:dts: sun7i-a20-bananapro add hdmi-connector, d... | `000000000000` | sun7i-a20-bananapro.dts |
| 49 | `arm-dts-sun7i-a20-cubietruck-add-alias-uart2.patch` | arm:dts: sun7i-a20-cubietruck add alias uart2 | `000000000000` | sun7i-a20-cubietruck.dts |
| 50 | `arm-dts-sun7i-a20-olimex-som-204-evb-olinuxino-micro-decrease-d.patch` | arm:dts:sun7i-a20: olimex-som(204)-evb,olinuxino-m... | `000000000000` | sun7i-a20-olimex-som-evb.dts, sun7i-a20-olimex-som204-evb.dts (+1) |
| 51 | `arm-dts-sun7i-a20-olinuxino-lime2-enable-audio-codec.patch` | arm:dts:sun7i-a20-olinuxino-lime2 enable audio cod... | `000000000000` | sun7i-a20-olinuxino-lime2.dts |
| 52 | `arm-dts-sun7i-a20-olinuxino-lime2-enable-ldo3-always-on.patch` | arm:dts:sun7i-a20-olinuxino-lime2 enable ldo3 alwa... | `000000000000` | sun7i-a20-olinuxino-lime2.dts |
| 53 | `arm-dts-sun7i-a20-olinuxino-micro-emmc-Add-vqmmc-node.patch` | arm:dts:sun7i-a20-olinuxino-micro-emmc Add vqmmc n... | `000000000000` | sun7i-a20-olinuxino-micro-emmc.dts |
| 54 | `arm-dts-sun8i-h2-plus-orangepi-zero-fix-usb_otg-dr_mode.patch` | arm: dts: sun8i-h2-plus-orangepi-zero: fix usb_otg... | `000000000000` | sun8i-h2-plus-orangepi-zero.dts |
| 55 | `arm-dts-sun8i-h2-plus-orangepi-zero-fix-xradio-interrupt.patch` | arm:dts: sun8i-h2-plus-orangepi-zero fix xradio in... | `000000000000` | sun8i-h2-plus-orangepi-zero.dts |
| 56 | `arm-dts-sun8i-h3-add-thermal-zones.patch` | arm:dts:sun8i-h3 add thermal zones | `000000000000` | sun8i-h3.dtsi |
| 57 | `arm-dts-sun8i-h3-bananapi-m2-plus-add-wifi_pwrseq.patch` | arm:dts:sun8i-h3-bananapi-m2-plus add wifi_pwrseq | `000000000000` | sun8i-h3-bananapi-m2-plus.dts |
| 58 | `arm-dts-sun8i-h3-nanopi-add-leds-pio-pins.patch` | arm:dts: sun8i-h3-nanopi add leds pio pins | `000000000000` | sun8i-h3-nanopi.dtsi |
| 59 | `arm-dts-sun8i-h3-orangepi-pc-plus-add-wifi_pwrseq.patch` | arm:dts: sun8i-h3-orangepi-pc-plus add wifi_pwrseq | `000000000000` | sun8i-h3-orangepi-pc-plus.dts |
| 60 | `arm-dts-sun8i-h3-reduce-opp-microvolt-to-prevent-not-supported-.patch` | arm: dts: sun8i: h3: reduce opp-microvolt to preve... | `000000000000` | sun8i-h3.dtsi |
| 61 | `arm-dts-sun8i-r40-add-clk_out_a-fix-bananam2ultra.patch` | arm:dts: sun8i-r40 add clk_out_a fix bananam2ultra | `000000000000` | sun8i-r40.dtsi |
| 62 | `arm-dts-sun8i-r40-bananapi-m2-ultra-add-codec-analog.patch` | arm:dts: sun8i-r40 bananapi-m2-ultra add codec ana... | `000000000000` | sun8i-r40.dtsi, sun8i-r40-bananapi-m2-ultra.dts |
| 63 | `arm-dts-sun8i-v3s-s3-pinecube-enable-sound-codec.patch` | arm:dts: sun8i-v3s/s3-pinecube enable sound codec | `000000000000` | sun8i-s3-pinecube.dts, sun8i-v3s.dtsi |
| 64 | `arm-dts-sun9i-a80-add-thermal-sensor.patch` | arm:dts: sun9i-a80 add thermal sensor | `000000000000` | sun9i-a80.dtsi |
| 65 | `arm-dts-sun9i-a80-add-thermal-zone.patch` | arm:dts: sun9i-a80 add thermal zone | `000000000000` | sun9i-a80.dtsi |
| 66 | `arm-dts-sunxi-h3-h5.dtsi-add-i2s0-i2s1-pins.patch` | arm:dts:sunxi-h3-h5.dtsi add i2s0 i2s1 pins | `000000000000` | sunxi-h3-h5.dtsi |
| 67 | `arm-dts-sunxi-h3-h5.dtsi-force-mmc0-bus-width.patch` | arm:dts: sunxi-h3-h5.dtsi force mmc0 bus-width | `000000000000` | sunxi-h3-h5.dtsi |
| 68 | `arm-patch-call-flush_icache-ASAP-after-writing-new-instruction.patch` | arm/patch: call flush_icache ASAP after writing ne... | `000000000000` | patch.c |
| 69 | `arm64-allwinner-Add-sun50i-h618-bananapi-m4-berry-support.patch` | arm64: allwinner: Add sun50i-h618-bananapi-m4-berr... | `000000000000` | sun50i-h616.dtsi, sun50i-h618-bananapi-m4-berry.dts |
| 70 | `arm64-dts-Add-sun50i-h5-nanopi-k1-plus-device.patch` | arm64:dts: Add sun50i-h5-nanopi-k1-plus device | `000000000000` | sun50i-h5-nanopi-k1-plus.dts |
| 71 | `arm64-dts-Add-sun50i-h5-nanopi-m1-plus2-device.patch` | arm64:dts: Add sun50i-h5-nanopi-m1-plus2 device | `000000000000` | sun50i-h5-nanopi-m1-plus2.dts |
| 72 | `arm64-dts-Add-sun50i-h5-nanopi-neo-core2-device.patch` | arm64:dts: Add sun50i-h5-nanopi-neo-core2 device | `000000000000` | sun50i-h5-nanopi-neo-core2.dts |
| 73 | `arm64-dts-Add-sun50i-h5-nanopi-neo2-v1.1-device.patch` | arm64:dts: Add sun50i-h5-nanopi-neo2-v1.1 device | `000000000000` | sun50i-h5-nanopi-neo2-v1.1.dts |
| 74 | `arm64-dts-FIXME-a64-olinuxino-add-regulator-audio-mmc.patch` | arm64:dts: FIXME: a64-olinuxino add regulator audi... | `000000000000` | sun50i-a64-olinuxino.dts |
| 75 | `arm64-dts-add-sun50i-h618-cpu-dvfs.dtsi.patch` | arm64: dts: add sun50i-h618-cpu-dvfs.dtsi | `000000000000` | sun50i-h618-orangepi-zero3.dts, sun50i-h616-orangepi-zero.dtsi (+2) |
| 76 | `arm64-dts-allwinner-Add-axp313a.dtsi.patch` | arm64: dts: allwinner: Add axp313a.dtsi | `000000000000` | axp313a.dtsi |
| 77 | `arm64-dts-allwinner-h6-Add-AC200-EPHY-nodes.patch` | arm64: dts: allwinner: h6: Add AC200 EPHY nodes | `000000000000` | sun50i-h6.dtsi |
| 78 | `arm64-dts-allwinner-h6-add-AC200-codec-nodes.patch` | arm64: dts: allwinner: h6: add AC200 codec nodes | `000000000000` | sun50i-h6.dtsi |
| 79 | `arm64-dts-allwinner-h6-enable-AC200-codec.patch` | arm64: dts: allwinner: h6: enable AC200 codec | `000000000000` | sun50i-h6-orangepi-3.dts, sun50i-h6-tanix-tx6-mini.dts (+1) |
| 80 | `arm64-dts-allwinner-h6-tanix-enable-Ethernet.patch` | arm64: dts: allwinner: h6: tanix: enable Ethernet | `000000000000` | sun50i-h6-tanix.dtsi |
| 81 | `arm64-dts-allwinner-h616-orangepi-zero2-Enable-expansion-board-.patch` | arm64: dts: allwinner: h616 orangepi zero2: Enable... | `000000000000` | sun50i-h616-orangepi-zero.dtsi |
| 82 | `arm64-dts-allwinner-overlay-Add-Overlays-for-sunxi64.patch` | arm64:dts:allwinner:overlay: Add Overlays for sunx... | `000000000000` | sun50i-h6-spi-add-cs1.dtso, sun50i-h5-usbhost1.dtso (+46) |
| 83 | `arm64-dts-allwinner-sun50i-h6-Fix-H6-emmc.patch` | arm64: dts/allwinner/sun50i-h6: Fix H6 emmc | `000000000000` | sun50i-h6.dtsi |
| 84 | `arm64-dts-allwinner-sun50i-h616-Add-VPU-node.patch` | arm64:dts:allwinner: sun50i-h616 Add VPU node | `000000000000` | sun50i-h616.dtsi |
| 85 | `arm64-dts-h616-8-Add-overlays-i2c-pwm-uart.patch` | arm64: dts: h616(8): Add overlays i2c, pwm, uart | `000000000000` | sun50i-h616-i2c3-pg.dtso, sun50i-h616-pwm2-ph2.dtso (+23) |
| 86 | `arm64-dts-h616-add-hdmi-support-for-zero2-and-zero3.patch` | arm64: dts: h616: add hdmi support for zero2 and z... | `000000000000` | sun50i-h616.dtsi, sun50i-h616-orangepi-zero.dtsi (+1) |
| 87 | `arm64-dts-h616-add-wifi-support-for-orange-pi-zero-2-and-zero3.patch` | arm64: dts: h616: add wifi support for orange pi z... | `000000000000` | sun50i-h616-orangepi-zero.dtsi |
| 88 | `arm64-dts-nanopi-a64-set-right-phy-mode-to-rgmii-id.patch` | arm64:dts: nanopi-a64 set right phy-mode to rgmii-... | `000000000000` | sun50i-a64-nanopi-a64.dts |
| 89 | `arm64-dts-overlay-sun50i-a64-pine64-7inch-lcd.patch` | arm64:dts:overlay: sun50i-a64-pine64-7inch-lcd | `000000000000` | README.sun50i-a64-overlays, sun50i-a64-pine64-7inch-lcd.dtso (+1) |
| 90 | `arm64-dts-overlay-sun50i-h5-add-gpio-regulator-overclock.patch` | arm64:dts:overlay sun50i-h5 add gpio regulator ove... | `000000000000` | sun50i-h5-cpu-clock-1.0GHz-1.1v.dtso, sun50i-h5-cpu-clock-1.3GHz-1.3v.dtso (+3) |
| 91 | `arm64-dts-sun50i-a64-force-mmc0-bus-width.patch` | arm64:dts: sun50i-a64 force mmc0 bus-width | `000000000000` | sun50i-a64.dtsi |
| 92 | `arm64-dts-sun50i-a64-olinuxino-1Ge16GW-Disable-clock-phase-and-.patch` | arm64:dts:sun50i-a64-olinuxino-1Ge16GW Disable clo... | `000000000000` | sun50i-a64-olinuxino-1Ge16GW.dts |
| 93 | `arm64-dts-sun50i-a64-olinuxino-1Ge16GW-enable-bluetooth.patch` | arm64:dts: sun50i-a64-olinuxino-1Ge16GW: enable bl... | `000000000000` | sun50i-a64-olinuxino-1Ge16GW.dts |
| 94 | `arm64-dts-sun50i-a64-olinuxino-add-boards.patch` | arm64:dts:sun50i-a64-olinuxino add boards | `000000000000` | sun50i-a64-olinuxino-1Ge4GW.dts, sun50i-a64-olinuxino-1Gs16M.dts (+3) |
| 95 | `arm64-dts-sun50i-a64-olinuxino-emmc-enable-bluetooth.patch` | arm64:dts: sun50i-a64-olinuxino-emmc: enable bluet... | `000000000000` | sun50i-a64-olinuxino-emmc.dts |
| 96 | `arm64-dts-sun50i-a64-orangepi-win-add-aliase-ethernet1.patch` | arm64:dts: sun50i-a64-orangepi-win add aliase ethe... | `000000000000` | sun50i-a64-orangepi-win.dts |
| 97 | `arm64-dts-sun50i-a64-pine64-add-spi0.patch` | arm64:dts: sun50i-a64-pine64 add spi0 | `000000000000` | sun50i-a64-pine64.dts |
| 98 | `arm64-dts-sun50i-a64-pine64-enable-wifi-mmc1.patch` | arm64:dts: sun50i-a64-pine64 enable wifi mmc1 | `000000000000` | sun50i-a64-pine64.dts |
| 99 | `arm64-dts-sun50i-a64-sopine-baseboard-enable-Bluetooth.patch` | arm64:dts: sun50i-a64-sopine-baseboard enable Blue... | `000000000000` | sun50i-a64-sopine-baseboard.dts |
| 100 | `arm64-dts-sun50i-a64-sopine-baseboard-mmc1-status-okay.patch` | arm64:dts: sun50i-a64-sopine-baseboard: mmc1: stat... | `000000000000` | sun50i-a64-sopine-baseboard.dts |
| 101 | `arm64-dts-sun50i-a64.dtsi-adjust-thermal-trip-points.patch` | arm64:dts:sun50i-a64.dtsi adjust thermal trip poin... | `000000000000` | sun50i-a64.dtsi |
| 102 | `arm64-dts-sun50i-h313-x96q-lpddr3.patch` | arm64: dts: sun50i-h313-x96q-lpddr3 | `000000000000` | sun50i-h313-x96q-lpddr3.dts, sun50i-h313-cpu-opp.dtsi |
| 103 | `arm64-dts-sun50i-h5-add-cpu-opp-refs.patch` | arm64:dts:sun50i-h5 add cpu opp refs | `000000000000` | sun50i-h5-nanopi-neo2.dts, sun50i-h5-nanopi-neo-plus2.dts (+6) |
| 104 | `arm64-dts-sun50i-h5-add-termal-zones.patch` | arm64:dts:sun50i-h5 add termal zones | `000000000000` | sun50i-h5.dtsi |
| 105 | `arm64-dts-sun50i-h5-enable-power-button-for-orangepi-prime.patch` | arm64: dts: sun50i: h5: enable power button for or... | `000000000000` | sun50i-h5-orangepi-prime.dts |
| 106 | `arm64-dts-sun50i-h5-nanopi-neo2-add-regulator-led-triger.patch` | arm64:dts: sun50i-h5-nanopi-neo2 add regulator, le... | `000000000000` | sun50i-h5-nanopi-neo2.dts |
| 107 | `arm64-dts-sun50i-h5-nanopi-r1s-h5-add-rtl8153-support.patch` | arm64: dts: sun50i-h5-nanopi-r1s-h5: add rtl8153 s... | `000000000000` | sun50i-h5-nanopi-r1s-h5.dts |
| 108 | `arm64-dts-sun50i-h5-orangepi-pc2-add-spi-flash.patch` | arm64:dts: sun50i-h5-orangepi-pc2 add spi flash | `000000000000` | sun50i-h5-orangepi-pc2.dts |
| 109 | `arm64-dts-sun50i-h5-orangepi-prime-add-regulator.patch` | arm64:dts: sun50i-h5-orangepi-prime add regulator | `000000000000` | sun50i-h5-orangepi-prime.dts |
| 110 | `arm64-dts-sun50i-h5-orangepi-prime-add-rtl8723cs.patch` | arm64:dts: sun50i-h5-orangepi-prime add rtl8723cs | `000000000000` | sun50i-h5-orangepi-prime.dts |
| 111 | `arm64-dts-sun50i-h5-orangepi-zero-plus-add-regulator.patch` | arm64:dts: sun50i-h5-orangepi-zero-plus add regula... | `000000000000` | sun50i-h5-orangepi-zero-plus.dts |
| 112 | `arm64-dts-sun50i-h6-Add-r_uart-uart2-3-pins.patch` | arm64:dts: sun50i-h6 Add r_uart uart2-3 pins | `000000000000` | sun50i-h6.dtsi |
| 113 | `arm64-dts-sun50i-h6-orangepi-3-add-r_uart-aliase.patch` | arm64:dts: sun50i-h6-orangepi-3 add r_uart aliase | `000000000000` | sun50i-h6-orangepi-3.dts |
| 114 | `arm64-dts-sun50i-h6-orangepi-3-delete-node-spi0.patch` | arm64:dts: sun50i-h6-orangepi-3 delete-node &spi0 | `000000000000` | sun50i-h6-orangepi-3.dts |
| 115 | `arm64-dts-sun50i-h6-orangepi-add-cpu-opp-refs.patch` | arm64:dts: sun50i-h6-orangepi add cpu opp refs | `000000000000` | sun50i-h6-orangepi.dtsi |
| 116 | `arm64-dts-sun50i-h6-orangepi-enable-higher-clock-regulator-max-.patch` | arm64:dts: sun50i-h6-orangepi enable higher clock | `000000000000` | sun50i-h6-orangepi.dtsi |
| 117 | `arm64-dts-sun50i-h6-orangepi-lite2-spi0-usb3phy-dwc3-enable.patch` | arm64:dts: sun50i-h6-orangepi-lite2 spi0, usb3phy,... | `000000000000` | sun50i-h6-orangepi-lite2.dts |
| 118 | `arm64-dts-sun50i-h6-pine-h64-add-dwc3-usb3phy.patch` | arm64:dts: sun50i-h6-pine-h64 add dwc3 usb3phy | `000000000000` | sun50i-h6-pine-h64.dts |
| 119 | `arm64-dts-sun50i-h6-pine-h64-add-wifi-rtl8723cs.patch` | arm64:dts: sun50i-h6-pine-h64 add wifi rtl8723cs | `000000000000` | sun50i-h6-pine-h64.dts |
| 120 | `arm64-dts-sun50i-h6.dtsi-add-pinctrl-pins-for-spi.patch` | arm64:dts: sun50i-h6.dtsi add pinctrl pins for spi | `000000000000` | sun50i-h6.dtsi |
| 121 | `arm64-dts-sun50i-h6.dtsi-improve-thermals.patch` | arm64:dts: sun50i-h6.dtsi improve thermals | `000000000000` | sun50i-h6.dtsi |
| 122 | `arm64-dts-sun50i-h616-add-pwm-nodes-support.patch` | arm64: dts: sun50i-h616: add pwm nodes support | `000000000000` | sun50i-h616.dtsi |
| 123 | `arm64-dts-sun50i-h616-bigtreetech-cb1-sd-emmc.patch` | arm64: dts: sun50i-h616-bigtreetech-cb1(sd, emmc) | `000000000000` | sun50i-h616-bigtreetech-cb1.dtsi, sun50i-h616-bigtreetech-cb1-sd.dts (+1) |
| 124 | `arm64-dts-sun50i-h616-orangepi-zero2-Enable-GPU-mali.patch` | arm64:dts: sun50i-h616-orangepi-zero2 Enable GPU m... | `000000000000` | sun50i-h616-orangepi-zero2.dts |
| 125 | `arm64-dts-sun50i-h616-orangepi-zero2-reg_usb1_vbus-status-ok.patch` | arm64: dts: sun50i-h616-orangepi-zero2: reg_usb1_v... | `000000000000` | sun50i-h616-orangepi-zero.dtsi |
| 126 | `arm64-dts-sun50i-h616-x96-mate-T95-eth-sd-card-hack.patch` | arm64:dts: sun50i-h616-x96-mate T95 eth & sd card ... | `000000000000` | sun50i-h616.dtsi, sun50i-h616-x96-mate.dts |
| 127 | `arm64-dts-sun50i-h616-x96-mate-add-hdmi.patch` | arm64:dts: sun50i-h616-x96-mate add hdmi | `000000000000` | sun50i-h616-x96-mate.dts |
| 128 | `arm64-dts-sun50i-h616.dtsi-reserved-memory-512K-for-BL31.patch` | arm64: dts: sun50i-h616.dtsi: reserved memory 512K... | `000000000000` | sun50i-h616.dtsi |
| 129 | `arm64-dts-sun50i-h618-orangepi-zero2w-Add-missing-nodes.patch` | arm64: dts: sun50i-h618-orangepi-zero2w: Add missi... | `000000000000` | sun50i-h616.dtsi, sun50i-h618-orangepi-zero2w.dts |
| 130 | `arm64-dts-sun50i-h618-orangepi-zero3-Enable-GPU-mali.patch` | arm64:dts: sun50i-h618-orangepi-zero3 Enable GPU m... | `000000000000` | sun50i-h618-orangepi-zero3.dts |
| 131 | `arm64-sun50i-h616-Add-i2c-2-3-4-uart-2-5-pins.patch` | arm64: sun50i-h616: Add i2c(2,3,4), uart(2,5) pins | `000000000000` | sun50i-h616.dtsi |
| 132 | `cb1-overlay.patch` | cb1-overlay | `000000000000` | sun50i-h616-fixup.scr-cmd, sun50i-h616-spidev1_0.dtso (+10) |
| 133 | `clk-gate-add-support-for-regmap-based-gates.patch` | clk: gate: add support for regmap based gates | `000000000000` | clk-gate.c, clk-provider.h |
| 134 | `driver-allwinner-h618-emac.patch` | driver: allwinner h618 emac | `000000000000` | Kconfig, Makefile (+12) |
| 135 | `drivers-devfreq-sun8i-a33-mbus-disable-autorefresh.patch` | drivers: devfreq: sun8i-a33-mbus: disable autorefr... | `000000000000` | sun8i-a33-mbus.c |
| 136 | `drivers-pwm-Add-pwm-sunxi-enhance-driver-for-h616.patch` | drivers: pwm: Add pwm-sunxi-enhance driver for h61... | `000000000000` | Makefile, pwm-sunxi-enhance.h (+2) |
| 137 | `drv-clocksource-arm_arch_timer-fix-a64-timejump.patch` | drv:clocksource:arm_arch_timer fix a64 timejump | `000000000000` | arm_arch_timer.c |
| 138 | `drv-gpu-drm-gem-dma-Export-with-handle-allocator.patch` | drv:gpu:drm: gem: dma: Export with handle allocato... | `000000000000` | drm_gem_dma_helper.h, drm_gem_dma_helper.c |
| 139 | `drv-gpu-drm-panel-simple-Add-compability-olinuxino-lcd.patch` | drv:gpu:drm: panel-simple Add compability olinuxin... | `000000000000` | panel-simple.c |
| 140 | `drv-gpu-drm-sun4i-Add-GEM-allocator.patch` | drv:gpu:drm:sun4i: Add GEM allocator | `000000000000` | sun4i_drm.h, sun4i_drv.c |
| 141 | `drv-gpu-drm-sun4i-Add-HDMI-audio-sun4i-hdmi-encoder.patch` | drv:gpu:drm:sun4i: Add HDMI audio sun4i-hdmi encod... | `000000000000` | sun4i_hdmi.h, sun4i_hdmi_enc.c (+3) |
| 142 | `drv-gpu-drm-sun4i-sun8i_mixer.c-add-h3-mixer1.patch` | drv:gpu:drm:sun4i:sun8i_mixer.c add h3 mixer1 | `000000000000` | sun8i_mixer.c |
| 143 | `drv-iio-adc-axp20x_adc-arm64-dts-axp803-hwmon-enable-thermal.patch` | drv:iio:adc:axp20x_adc arm64:dts:axp803 hwmon enab... | `000000000000` | axp803.dtsi, axp20x_adc.c |
| 144 | `drv-input-touchscreen-sun4i-ts-Enable-parsing.patch` | drv:input:touchscreen:sun4i-ts Enable parsing | `000000000000` | sun4i-ts.c |
| 145 | `drv-media-dvb-frontends-si2168-fix-cmd-timeout.patch` | drv:media:dvb-frontends:si2168: fix cmd timeout | `000000000000` | si2168.c |
| 146 | `drv-mfd-axp20x-add-sysfs-interface.patch` | drv:mfd:axp20x add sysfs interface | `2a8a9e3104ce` | axp20x.c |
| 147 | `drv-mmc-host-sunxi-mmc-Disable-DDR52-mode-on-all-A20-based-boar.patch` | drv:mmc:host:sunxi-mmc Disable DDR52 mode on all A... | `000000000000` | sunxi-mmc.c |
| 148 | `drv-mmc-host-sunxi-mmc-add-h5-emmc-compatible.patch` | drv:mmc:host:sunxi-mmc: add h5 emmc compatible | `000000000000` | sunxi-mmc.c |
| 149 | `drv-mtd-nand-raw-nand_ids.c-add-H27UBG8T2BTR-BC-nand.patch` | drv:mtd:nand:raw:nand_ids.c add H27UBG8T2BTR-BC na... | `000000000000` | nand_ids.c |
| 150 | `drv-net-stmmac-dwmac-sun8i-second-EMAC-clock-register.patch` | drv:net:stmmac:dwmac-sun8i: second EMAC clock regi... | `000000000000` | dwmac-sun8i.c |
| 151 | `drv-nvmem-sunxi_sid-Support-SID-on-H616.patch` | drv:nvmem:sunxi_sid: Support SID on H616 | `000000000000` | sunxi_sid.c |
| 152 | `drv-of-Device-Tree-Overlay-ConfigFS-interface.patch` | drv:of: Device Tree Overlay ConfigFS interface | `000000000000` | Makefile, configfs.c (+2) |
| 153 | `drv-phy-sun4i-usb-Allow-reset-line-to-be-shared.patch` | drv:phy: sun4i-usb: Allow reset line to be shared | `000000000000` | phy-sun4i-usb.c |
| 154 | `drv-pinctrl-pinctrl-sun50i-a64-disable_strict_mode.patch` | drv:pinctrl: pinctrl-sun50i-a64 disable_strict_mod... | `000000000000` | pinctrl-sun50i-a64.c |
| 155 | `drv-pinctrl-sunxi-pinctrl-sun50i-h6.c-GPIO-disable_strict_mode.patch` | drv:pinctrl:sunxi:pinctrl-sun50i-h6.c GPIO disable... | `000000000000` | pinctrl-sun50i-h6.c |
| 156 | `drv-soc-sunxi-sram-Add-SRAM-C1-H616-handling.patch` | drv:soc: sunxi: sram: Add SRAM C1 H616 handling | `000000000000` | sunxi_sram.c |
| 157 | `drv-spi-spi-sun4i.c-spi-bug-low-on-sck.patch` | drv:spi:spi-sun4i.c spi bug low on sck | `000000000000` | spi-sun4i.c |
| 158 | `drv-spi-spidev-Add-armbian-spi-dev-compatible.patch` | drv:spi:spidev Add armbian spi-dev compatible | `000000000000` | spidev.c |
| 159 | `drv-staging-media-sunxi-cedrus-add-H616-variant.patch` | drv:staging:media:sunxi:cedrus: add H616 variant | `000000000000` | cedrus.c |
| 160 | `drv-staging-rtl8723bs-AP-bugfix.patch` | drv:staging:rtl8723bs: AP bugfix | `000000000000` | ioctl_cfg80211.c |
| 161 | `drv-usb-gadget-composite-rename-gadget-serial-console-manufactu.patch` | drv:usb:gadget:composite rename gadget serial cons... | `000000000000` | composite.c |
| 162 | `enable-TV-Output-on-OrangePi-Zero-LTE.patch` | enable TV Output on OrangePi Zero LTE | `000000000000` | sun8i_mixer.c, sun8i-h2-plus-orangepi-zero.dts (+14) |
| 163 | `fix-cpu-opp-table-sun8i-a83t.patch` | fix: cpu opp table sun8i-a83t | `000000000000` | sun8i-a83t.dtsi |
| 164 | `h616-add-keys.patch` | h616: add keys | `000000000000` | sun50i-h616-keys.dtso, sun4i-lradc-keys.c (+2) |
| 165 | `include-uapi-drm_fourcc-add-ARM-tiled-format-modifier.patch` | include:uapi:drm_fourcc: add ARM tiled format modi... | `000000000000` | drm_fourcc.h |
| 166 | `mfd-Add-support-for-X-Powers-AC200-EPHY-syscon.patch` | mfd: Add support for X-Powers AC200 EPHY syscon | `000000000000` | Kconfig, Makefile (+1) |
| 167 | `mfd-Add-support-for-X-Powers-AC200.patch` | mfd: Add support for X-Powers AC200 | `000000000000` | ac200.c, Kconfig (+1) |
| 168 | `mmc-host-sunxi-mmc-Fix-H6-emmc.patch` | mmc/host/sunxi-mmc: Fix H6 emmc | `000000000000` | sunxi-mmc.c |
| 169 | `net-phy-Add-support-for-AC200-EPHY.patch` | net: phy: Add support for AC200 EPHY | `000000000000` | Kconfig, ac200-phy.c (+1) |
| 170 | `net-usb-r8152-add-LED-configuration-from-OF.patch` | net: usb: r8152: add LED configuration from OF | `000000000000` | r8152.c |
| 171 | `nvmem-sunxi_sid-add-sunxi_get_soc_chipid-sunxi_get_serial.patch` | nvmem: sunxi_sid: add sunxi_get_soc_chipid, sunxi_... | `000000000000` | sunxi_sid.c |
| 172 | `scripts-add-overlay-compilation-support.patch` | scripts: add overlay compilation support | `000000000000` | Makefile.dtbinst, .gitignore (+1) |
| 173 | `sound-soc-sunxi-Provoke-the-early-load-of-sun8i-codec-analog.patch` | sound:soc:sunxi: Provoke the early load of sun8i-c... | `000000000000` | Makefile |
| 174 | `sound-soc-sunxi-sun4i-codec-adcis-select-capture-source.patch` | sound:soc:sunxi:sun4i-codec adcis select capture s... | `000000000000` | sun4i-codec.c |
| 175 | `sound-soc-sunxi-sun8i-codec-analog-enable-sound.patch` | sound:soc:sunxi:sun8i-codec-analog enable sound | `000000000000` | sun8i-codec-analog.c |
| 176 | `sun50i-h616-Add-the-missing-digital-audio-node.patch` | sun50i-h616: Add the missing digital audio node | `000000000000` | sun50i-h616.dtsi, sun50i-h618-bananapi-m4-berry.dts |

### patches.drm (26 patches)

| # | Patch File | Subject | Commit ID | Files Changed |
|---|------------|---------|-----------|---------------|
| 1 | `drm-sun4i-Report-page-flip-after-vsync-is-complete-not-in-the-m.patch` | drm: sun4i: Report page flip after vsync is comple... | `000000000000` | sun4i_tcon.c, sun4i_tcon.h |
| 2 | `drm-sun4i-add-sun50i-h616-hdmi-phy-support.patch` | drm: sun4i: add sun50i-h616-hdmi-phy support | `000000000000` | sun8i_hdmi_phy.c |
| 3 | `drm-sun4i-de2-Initialize-layer-fields-earlier.patch` | drm: sun4i: de2: Initialize layer fields earlier | `000000000000` | sun8i_vi_layer.c, sun8i_ui_layer.c |
| 4 | `drm-sun4i-de2-de3-Change-CSC-argument.patch` | drm: sun4i: de2/de3: Change CSC argument | `000000000000` | sun8i_vi_layer.c, sun8i_csc.h (+1) |
| 5 | `drm-sun4i-de2-de3-Merge-CSC-functions-into-one.patch` | drm: sun4i: de2/de3: Merge CSC functions into one | `000000000000` | sun8i_vi_layer.c, sun8i_csc.h (+1) |
| 6 | `drm-sun4i-de2-de3-add-generic-blender-register-reference-functi.patch` | drm: sun4i: de2/de3: add generic blender register ... | `000000000000` | sun8i_mixer.h |
| 7 | `drm-sun4i-de2-de3-add-mixer-version-enum.patch` | drm: sun4i: de2/de3: add mixer version enum | `000000000000` | sun8i_vi_scaler.c, sun8i_mixer.h (+4) |
| 8 | `drm-sun4i-de2-de3-call-csc-setup-also-for-UI-layer.patch` | drm: sun4i: de2/de3: call csc setup also for UI la... | `000000000000` | sun8i_csc.c, sun8i_ui_layer.c |
| 9 | `drm-sun4i-de2-de3-refactor-mixer-initialisation.patch` | drm: sun4i: de2/de3: refactor mixer initialisation | `000000000000` | sun8i_mixer.c |
| 10 | `drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch` | drm: sun4i: de2/de3: use generic register referenc... | `000000000000` | sun8i_vi_layer.c, sun8i_mixer.c (+1) |
| 11 | `drm-sun4i-de3-Add-YUV-formatter-module.patch` | drm: sun4i: de3: Add YUV formatter module | `000000000000` | sun50i_fmt.h, Makefile (+1) |
| 12 | `drm-sun4i-de3-Implement-AFBC-support.patch` | drm: sun4i: de3: Implement AFBC support | `000000000000` | sun50i_afbc.c, sun50i_afbc.h (+2) |
| 13 | `drm-sun4i-de3-add-YUV-support-to-the-DE3-mixer.patch` | drm: sun4i: de3: add YUV support to the DE3 mixer | `000000000000` | sun8i_mixer.c, sunxi_engine.h |
| 14 | `drm-sun4i-de3-add-YUV-support-to-the-TCON.patch` | drm: sun4i: de3: add YUV support to the TCON | `000000000000` | sun4i_tcon.c |
| 15 | `drm-sun4i-de3-add-YUV-support-to-the-color-space-correction-mod.patch` | drm: sun4i: de3: add YUV support to the color spac... | `000000000000` | sun8i_csc.c |
| 16 | `drm-sun4i-de3-add-format-enumeration-function-to-engine.patch` | drm: sun4i: de3: add format enumeration function t... | `000000000000` | sunxi_engine.h |
| 17 | `drm-sun4i-de3-add-formatter-flag-to-mixer-config.patch` | drm: sun4i: de3: add formatter flag to mixer confi... | `000000000000` | sun8i_mixer.c, sun8i_mixer.h |
| 18 | `drm-sun4i-de3-pass-engine-reference-to-ccsc-setup-function.patch` | drm: sun4i: de3: pass engine reference to ccsc set... | `000000000000` | sun8i_csc.c |
| 19 | `drm-sun4i-de33-csc-add-Display-Engine-3.3-DE33-support.patch` | drm: sun4i: de33: csc: add Display Engine 3.3 (DE3... | `000000000000` | sun8i_csc.h, sun8i_csc.c |
| 20 | `drm-sun4i-de33-fmt-add-Display-Engine-3.3-DE33-support.patch` | drm: sun4i: de33: fmt: add Display Engine 3.3 (DE3... | `000000000000` | sun50i_fmt.h, sun50i_fmt.c |
| 21 | `drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch` | drm: sun4i: de33: mixer: add Display Engine 3.3 (D... | `000000000000` | sun8i_mixer.c, sun8i_mixer.h |
| 22 | `drm-sun4i-de33-vi_scaler-add-Display-Engine-3.3-DE33-support.patch` | drm: sun4i: de33: vi_scaler: add Display Engine 3.... | `000000000000` | sun8i_vi_scaler.c, sun8i_ui_layer.c |
| 23 | `drm-sun4i-support-YUV-formats-in-VI-scaler.patch` | drm: sun4i: support YUV formats in VI scaler | `000000000000` | sun8i_vi_scaler.c |
| 24 | `drm-sun4i-vi_scaler-refactor-vi_scaler-enablement.patch` | drm: sun4i: vi_scaler refactor vi_scaler enablemen... | `000000000000` | sun8i_vi_layer.c, sun8i_vi_scaler.c (+1) |
| 25 | `dt-bindings-allwinner-add-H616-DE33-bus-binding.patch` | dt-bindings: allwinner: add H616 DE33 bus binding | `000000000000` | allwinner,sun50i-a64-de2.yaml |
| 26 | `dt-bindings-allwinner-add-H616-DE33-mixer-binding.patch` | dt-bindings: allwinner: add H616 DE33 mixer bindin... | `000000000000` | allwinner,sun8i-a83t-de2-mixer.yaml |

### patches.media (6 patches)

| # | Patch File | Subject | Commit ID | Files Changed |
|---|------------|---------|-----------|---------------|
| 1 | `dma-sun6i-dma-add-sun50i-h616-support.patch` | dma: sun6i-dma: add sun50i-h616 support | `000000000000` | sun6i-dma.c |
| 2 | `media-Add-NV12-and-P010-AFBC-compressed-formats.patch` | media: Add NV12 and P010 AFBC compressed formats | `000000000000` | videodev2.h, v4l2-ioctl.c |
| 3 | `media-cedrus-Don-t-CPU-map-source-buffers.patch` | media: cedrus: Don't CPU map source buffers | `000000000000` | cedrus_video.c |
| 4 | `media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch` | media: cedrus: Implement AFBC YUV420 formats for H... | `000000000000` | cedrus_hw.c, cedrus_regs.h (+3) |
| 5 | `media-cedrus-Increase-H6-clock-rate.patch` | media: cedrus: Increase H6 clock rate | `000000000000` | cedrus.c |
| 6 | `media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch` | media: cedrus: add format filtering based on depth... | `000000000000` | cedrus_video.h, cedrus_video.c |

### patches.megous (236 patches)

| # | Patch File | Subject | Commit ID | Files Changed |
|---|------------|---------|-----------|---------------|
| 1 | `2-arm64-dts-sun50i-Define-orientation-and-rotation-for-PinePhone-.patch` | arm64: dts: sun50i: Define orientation and rotatio... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 2 | `ARM-dts-axp813-Add-charger-LED.patch` | ARM: dts: axp813: Add charger LED | `000000000000` | axp81x.dtsi |
| 3 | `ARM-dts-sun5i-Add-PocketBook-Touch-Lux-3-display-ctp-support.patch` | ARM: dts: sun5i: Add PocketBook Touch Lux 3 displa... | `000000000000` | sun5i-a13-pocketbook-touch-lux-3.dts |
| 4 | `ARM-dts-sun5i-Add-soc-handle.patch` | ARM: dts: sun5i: Add soc handle | `000000000000` | sun5i.dtsi |
| 5 | `ARM-dts-sun5i-a13-pocketbook-touch-lux-3-Add-RTC-clock-cells.patch` | ARM: dts: sun5i-a13-pocketbook-touch-lux-3: Add RT... | `000000000000` | sun5i-a13-pocketbook-touch-lux-3.dts |
| 6 | `ARM-dts-sun8i-a83t-Add-MBUS-node.patch` | ARM: dts: sun8i: a83t: Add MBUS node | `000000000000` | sun8i-a83t.dtsi |
| 7 | `ARM-dts-sun8i-a83t-Add-cedrus-video-codec-support-to-A83T-untes.patch` | ARM: dts: sun8i-a83t: Add cedrus video codec suppo... | `000000000000` | sun8i-a83t.dtsi |
| 8 | `ARM-dts-sun8i-a83t-Add-hdmi-sound-card.patch` | ARM: dts: sun8i: a83t: Add hdmi sound card | `000000000000` | sun8i-a83t.dtsi |
| 9 | `ARM-dts-sun8i-a83t-Add-missing-GPU-trip-point.patch` | ARM: dts: sun8i-a83t: Add missing GPU trip point | `000000000000` | sun8i-a83t.dtsi |
| 10 | `ARM-dts-sun8i-a83t-Enable-hdmi-sound-card-on-boards-with-hdmi.patch` | ARM: dts: sun8i: a83t: Enable hdmi sound card on b... | `000000000000` | sun8i-a83t-cubietruck-plus.dts, sun8i-a83t-bananapi-m3.dts |
| 11 | `ARM-dts-sun8i-a83t-Improve-CPU-OPP-tables-go-up-to-1.8GHz.patch` | ARM: dts: sun8i-a83t: Improve CPU OPP tables (go u... | `000000000000` | sun8i-a83t.dtsi |
| 12 | `ARM-dts-sun8i-a83t-Set-fifo-size-for-uarts.patch` | ARM: dts: sun8i-a83t: Set fifo-size for uarts | `000000000000` | sun8i-a83t.dtsi |
| 13 | `ARM-dts-sun8i-a83t-tbs-a711-Add-PN544-NFC-support.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add PN544 NFC suppo... | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 14 | `ARM-dts-sun8i-a83t-tbs-a711-Add-camera-sensors-HM5065-GC2145.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add camera sensors ... | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 15 | `ARM-dts-sun8i-a83t-tbs-a711-Add-flash-led-support.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add flash led suppo... | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 16 | `ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add powerup/down su... | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 17 | `ARM-dts-sun8i-a83t-tbs-a711-Add-regulators-to-the-accelerometer.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add regulators to t... | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 18 | `ARM-dts-sun8i-a83t-tbs-a711-Add-sound-support-via-AC100-codec.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add sound support v... | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 19 | `ARM-dts-sun8i-a83t-tbs-a711-Add-support-for-the-vibrator-motor.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add support for the... | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 20 | `ARM-dts-sun8i-a83t-tbs-a711-Enable-charging-LED.patch` | ARM: dts: sun8i-a83t-tbs-a711: Enable charging LED | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 21 | `ARM-dts-sun8i-a83t-tbs-a711-Give-Linux-more-privileges-over-SCP.patch` | ARM: dts: sun8i-a83t-tbs-a711: Give Linux more pri... | `000000000000` | sun8i-a83t.dtsi |
| 22 | `ARM-dts-sun8i-a83t-tbs-a711-Increase-voltage-on-the-vibrator.patch` | ARM: dts: sun8i-a83t-tbs-a711: Increase voltage on... | `000000000000` | sun8i-a83t-tbs-a711.dts |
| 23 | `ARM-dts-sun8i-h2-plus-bananapi-m2-zero-Enable-HDMI-audio.patch` | ARM: dts: sun8i: h2-plus: bananapi-m2-zero: Enable... | `000000000000` | sun8i-h2-plus-bananapi-m2-zero.dts |
| 24 | `ARM-dts-sun8i-h3-Enable-hdmi-sound-card-on-boards-with-hdmi.patch` | ARM: dts: sun8i: h3: Enable hdmi sound card on boa... | `000000000000` | sun8i-h3-orangepi-zero-plus2.dts, sun8i-h3-nanopi-m1.dts (+8) |
| 25 | `ARM-dts-sun8i-h3-Use-my-own-more-aggressive-OPPs-on-H3.patch` | ARM: dts: sun8i-h3: Use my own more aggressive OPP... | `000000000000` | sun8i-h3.dtsi |
| 26 | `ARM-dts-sun8i-h3-orange-pi-one-Enable-all-gpio-header-UARTs.patch` | ARM: dts: sun8i-h3-orange-pi-one: Enable all gpio ... | `000000000000` | sun8i-h3-orangepi-one.dts |
| 27 | `ARM-dts-sun8i-h3-orange-pi-pc-Increase-max-CPUX-voltage-to-1.4V.patch` | ARM: dts: sun8i-h3-orange-pi-pc: Increase max CPUX... | `000000000000` | sun8i-h3-orangepi-pc.dts |
| 28 | `ARM-dts-sun8i-r40-Add-hdmi-sound-card.patch` | ARM: dts: sun8i: r40: Add hdmi sound card | `000000000000` | sun8i-r40.dtsi |
| 29 | `ARM-dts-sun8i-r40-bananapi-m2-ultra-Enable-HDMI-audio.patch` | ARM: dts: sun8i: r40: bananapi-m2-ultra: Enable HD... | `000000000000` | sun8i-r40-bananapi-m2-ultra.dts |
| 30 | `ARM-dts-sun8i-v40-bananapi-m2-berry-Enable-HDMI-audio.patch` | ARM: dts: sun8i: v40: bananapi-m2-berry: Enable HD... | `000000000000` | sun8i-v40-bananapi-m2-berry.dts |
| 31 | `ARM-dts-suni-a83t-Add-i2s0-pins.patch` | ARM: dts: suni-a83t: Add i2s0 pins | `000000000000` | sun8i-a83t.dtsi |
| 32 | `ARM-dts-sunxi-Add-aliases-for-MMC.patch` | ARM: dts: sunxi: Add aliases for MMC | `000000000000` | sun8i-a83t.dtsi, sun5i.dtsi (+1) |
| 33 | `ARM-dts-sunxi-a83t-Add-SCPI-protocol.patch` | ARM: dts: sunxi: a83t: Add SCPI protocol | `000000000000` | sun8i-a83t.dtsi |
| 34 | `ARM-dts-sunxi-h3-h5-Add-SCPI-protocol.patch` | ARM: dts: sunxi: h3/h5: Add SCPI protocol | `000000000000` | sun50i-h5.dtsi, sunxi-h3-h5.dtsi (+1) |
| 35 | `ARM-dts-sunxi-h3-h5-Add-hdmi-sound-card.patch` | ARM: dts: sunxi: h3/h5: Add hdmi sound card | `000000000000` | sunxi-h3-h5.dtsi |
| 36 | `ARM-sunxi-Add-experimental-suspend-to-memory-implementation-for.patch` | ARM: sunxi: Add experimental suspend to memory imp... | `000000000000` | sunxi.c |
| 37 | `ARM-sunxi-Use-SCPI-to-send-suspend-message-to-SCP-on-A83T.patch` | ARM: sunxi: Use SCPI to send suspend message to SC... | `000000000000` | sunxi.c |
| 38 | `ARM-sunxi-sunxi_cpu0_hotplug_support_set-is-not-supported-on-A8.patch` | ARM: sunxi: sunxi_cpu0_hotplug_support_set is not ... | `000000000000` | mc_smp.c |
| 39 | `ASOC-sun9i-hdmi-audio-Initial-implementation.patch` | ASOC: sun9i-hdmi-audio: Initial implementation | `000000000000` | sun9i-hdmi-audio.c, Kconfig (+1) |
| 40 | `ASoC-ec25-New-codec-driver-for-the-EC25-modem.patch` | ASoC: ec25: New codec driver for the EC25 modem | `000000000000` | ec25.c, Makefile (+1) |
| 41 | `ASoC-simple-card-Allow-to-define-pins-for-aux-jack-devices.patch` | ASoC: simple-card: Allow to define pins for aux ja... | `000000000000` | simple-card-utils.c |
| 42 | `ASoC-sun8i-codec-Add-debug-output-for-jack-detection.patch` | ASoC: sun8i-codec: Add debug output for jack detec... | `000000000000` | sun8i-codec.c |
| 43 | `ASoC-sun8i-codec-Allow-the-jack-type-to-be-set-via-device-tree.patch` | ASoC: sun8i-codec: Allow the jack type to be set v... | `000000000000` | sun8i-codec.c |
| 44 | `ASoC-sun8i-codec-Set-jack_type-from-DT-in-probe.patch` | ASoC: sun8i-codec: Set jack_type from DT in probe | `000000000000` | sun8i-codec.c |
| 45 | `ASoC-sun8i-codec-define-button-keycodes.patch` | ASoC: sun8i-codec: define button keycodes | `000000000000` | sun8i-codec.c |
| 46 | `Add-support-for-my-private-Sapomat-device.patch` | Add support for my private Sapomat device | `000000000000` | sun8i-h3-orangepi-pc-sapomat.dts |
| 47 | `Defconfigs-for-all-my-devices.patch` | Defconfigs for all my devices | `000000000000` | pocketbook_touch_lux_3_defconfig, orangepi_defconfig (+4) |
| 48 | `Fix-broken-allwinner-sram-dependency-on-h616-h618.patch` | Fix broken allwinner,sram dependency on h616, h618 | `000000000000` | property.c |
| 49 | `Fix-intptr_t-typedef.patch` | Fix intptr_t typedef | `000000000000` | types.h |
| 50 | `MAINTAINERS-Add-entry-for-Himax-HM5065.patch` | MAINTAINERS: Add entry for Himax HM5065 | `2ce741f43a65` | MAINTAINERS |
| 51 | `Make-microbuttons-on-Orange-Pi-PC-and-PC-2-work-as-power-off-bu.patch` | Make microbuttons on Orange Pi PC and PC 2 work as... | `000000000000` | sun50i-h5-orangepi-pc2.dts, sun8i-h3-orangepi-one.dts |
| 52 | `Mark-some-slow-drivers-for-async-probe-with-PROBE_PREFER_ASYNCH.patch` | Mark some slow drivers for async probe with PROBE_... | `000000000000` | i2c.c, bma180.c |
| 53 | `Move-a-node-to-avoid-merge-conflict.patch` | Move a node to avoid merge conflict | `000000000000` | sun50i-h6.dtsi, sun50i-h6-orangepi-3.dts (+1) |
| 54 | `Revert-ASoC-soc-core-merge-snd_soc_unregister_component-and-snd.patch` | Revert "ASoC: soc-core: merge snd_soc_unregister_c... | `000000000000` | soc-core.c, soc.h |
| 55 | `Revert-Input-cyttsp4-remove-driver.patch` | Revert "Input: cyttsp4 - remove driver" | `000000000000` | cyttsp4_spi.c, cyttsp4_core.c (+8) |
| 56 | `Revert-drm-sun4i-lvds-Invert-the-LVDS-polarity.patch` | Revert "drm/sun4i: lvds: Invert the LVDS polarity" | `000000000000` | sun4i_tcon.c |
| 57 | `Revert-usb-dwc3-Abort-suspend-on-soft-disconnect-failure.patch` | Revert "usb: dwc3: Abort suspend on soft disconnec... | `000000000000` | core.c, gadget.c |
| 58 | `Revert-usb-typec-tcpm-unregister-existing-source-caps-before-re.patch` | Revert "usb: typec: tcpm: unregister existing sour... | `000000000000` | tcpm.c |
| 59 | `arm64-allwinner-dts-a64-enable-K101-IM2BYL02-panel-for-PineTab.patch` | arm64: allwinner: dts: a64: enable K101-IM2BYL02 p... | `000000000000` | sun50i-a64-pinetab.dts |
| 60 | `arm64-dts-allwinner-Enforce-consistent-MMC-numbering.patch` | arm64: dts: allwinner: Enforce consistent MMC numb... | `000000000000` | sun50i-h5.dtsi, sun50i-a64.dtsi (+1) |
| 61 | `arm64-dts-allwinner-a64-Add-hdmi-sound-card.patch` | arm64: dts: allwinner: a64: Add hdmi sound card | `000000000000` | sun50i-a64.dtsi |
| 62 | `arm64-dts-allwinner-a64-Enable-hdmi-sound-card-on-boards-with-h.patch` | arm64: dts: allwinner: a64: Enable hdmi sound card... | `000000000000` | sun50i-a64-bananapi-m64.dts, sun50i-a64-nanopi-a64.dts (+5) |
| 63 | `arm64-dts-allwinner-a64-Fix-LRADC-compatible.patch` | arm64: dts: allwinner: a64: Fix LRADC compatible | `000000000000` | sun50i-a64.dtsi |
| 64 | `arm64-dts-allwinner-a64-pinetab-add-front-camera.patch` | arm64: dts: allwinner: a64: pinetab: add front cam... | `000000000000` | sun50i-a64-pinetab.dts |
| 65 | `arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch` | arm64: dts: allwinner: h5: Enable hdmi sound card ... | `000000000000` | sun50i-h5-emlid-neutis-n5-devboard.dts, sun50i-h5-orangepi-prime.dts (+2) |
| 66 | `arm64-dts-allwinner-h6-Add-hdmi-sound-card.patch` | arm64: dts: allwinner: h6: Add hdmi sound card | `000000000000` | sun50i-h6.dtsi |
| 67 | `arm64-dts-allwinner-h6-Enable-hdmi-sound-card-on-boards-with-hd.patch` | arm64: dts: allwinner: h6: Enable hdmi sound card ... | `000000000000` | sun50i-h6-beelink-gs1.dts, sun50i-h6-orangepi-3.dts (+2) |
| 68 | `arm64-dts-allwinner-orange-pi-3-Enable-ethernet.patch` | arm64: dts: allwinner: orange-pi-3: Enable etherne... | `000000000000` | sun50i-h6-orangepi-3.dts |
| 69 | `arm64-dts-rk3399-Add-dmc_opp_table.patch` | arm64: dts: rk3399: Add dmc_opp_table | `000000000000` | rk3399.dtsi |
| 70 | `arm64-dts-sun50-a64-pinephone-Define-jack-pins-in-DT.patch` | arm64: dts: sun50-a64-pinephone: Define jack pins ... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 71 | `arm64-dts-sun50i-Define-orientation-and-rotation-for-PinePhone-.patch` | arm64: dts: sun50i: Define orientation and rotatio... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 72 | `arm64-dts-sun50i-a64-Set-fifo-size-for-uarts.patch` | arm64: dts: sun50i-a64: Set fifo-size for uarts | `000000000000` | sun50i-a64.dtsi |
| 73 | `arm64-dts-sun50i-a64-pinephone-Add-Type-C-support-for-all-PP-va.patch` | arm64: dts: sun50i-a64-pinephone: Add Type-C suppo... | `000000000000` | sun50i-a64-pinephone-1.2.dts, sun50i-a64-pinephone.dtsi (+2) |
| 74 | `arm64-dts-sun50i-a64-pinephone-Add-detailed-OCV-to-capactiy-con.patch` | arm64: dts: sun50i-a64-pinephone: Add detailed OCV... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 75 | `arm64-dts-sun50i-a64-pinephone-Add-front-back-cameras.patch` | arm64: dts: sun50i-a64-pinephone: Add front/back c... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 76 | `arm64-dts-sun50i-a64-pinephone-Add-interrupt-pin-for-WiFi.patch` | arm64: dts: sun50i-a64-pinephone: Add interrupt pi... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 77 | `arm64-dts-sun50i-a64-pinephone-Add-modem-power-manager.patch` | arm64: dts: sun50i-a64-pinephone: Add modem power ... | `000000000000` | sun50i-a64-pinephone-1.2.dts, sun50i-a64-pinephone-1.0.dts (+1) |
| 78 | `arm64-dts-sun50i-a64-pinephone-Add-power-supply-to-stk3311.patch` | arm64: dts: sun50i-a64-pinephone: Add power supply... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 79 | `arm64-dts-sun50i-a64-pinephone-Add-reboot-mode-driver.patch` | arm64: dts: sun50i-a64-pinephone: Add reboot mode ... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 80 | `arm64-dts-sun50i-a64-pinephone-Add-supply-for-i2c-bus-to-anx768.patch` | arm64: dts: sun50i-a64-pinephone: Add supply for i... | `000000000000` | sun50i-a64-pinephone-1.2.dts, sun50i-a64-pinephone-1.0.dts (+1) |
| 81 | `arm64-dts-sun50i-a64-pinephone-Add-support-for-Bluetooth-audio.patch` | arm64: dts: sun50i-a64-pinephone: Add support for ... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 82 | `arm64-dts-sun50i-a64-pinephone-Add-support-for-Pinephone-1.2-be.patch` | arm64: dts: sun50i-a64-pinephone: Add support for ... | `000000000000` | sun50i-a64-pinephone-1.2b.dts |
| 83 | `arm64-dts-sun50i-a64-pinephone-Add-support-for-Pinephone-keyboa.patch` | arm64: dts: sun50i-a64-pinephone: Add support for ... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 84 | `arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch` | arm64: dts: sun50i-a64-pinephone: Add support for ... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 85 | `arm64-dts-sun50i-a64-pinephone-Bump-I2C-frequency-to-400kHz.patch` | arm64: dts: sun50i-a64-pinephone: Bump I2C frequen... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 86 | `arm64-dts-sun50i-a64-pinephone-Don-t-make-lradc-keys-a-wakeup-s.patch` | arm64: dts: sun50i-a64-pinephone: Don't make lradc... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 87 | `arm64-dts-sun50i-a64-pinephone-Enable-Pinephone-Keyboard-power-.patch` | arm64: dts: sun50i-a64-pinephone: Enable Pinephone... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 88 | `arm64-dts-sun50i-a64-pinephone-Enable-internal-HMIC-bias.patch` | arm64: dts: sun50i-a64-pinephone: Enable internal ... | `000000000000` | sun50i-a64-pinephone-1.0.dts |
| 89 | `arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch` | arm64: dts: sun50i-a64-pinephone: Fix BH modem man... | `000000000000` | sun50i-a64-pinephone-1.1.dts |
| 90 | `arm64-dts-sun50i-a64-pinephone-Power-off-the-touch-controller-i.patch` | arm64: dts: sun50i-a64-pinephone: Power off the to... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 91 | `arm64-dts-sun50i-a64-pinephone-Set-minimum-backlight-duty-cycle.patch` | arm64: dts: sun50i-a64-pinephone: Set minimum back... | `000000000000` | sun50i-a64-pinephone-1.2.dts, sun50i-a64-pinephone-1.1.dts |
| 92 | `arm64-dts-sun50i-a64-pinephone-Shorten-post-power-on-delay-on-m.patch` | arm64: dts: sun50i-a64-pinephone: Shorten post-pow... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 93 | `arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch` | arm64: dts: sun50i-a64-pinephone: Use newer jack d... | `000000000000` | sun50i-a64-pinephone.dtsi |
| 94 | `arm64-dts-sun50i-a64-pinephone-Workaround-broken-HDMI-HPD-signa.patch` | arm64: dts: sun50i-a64-pinephone: Workaround broke... | `000000000000` | sun50i-a64-pinephone-1.2.dts, sun50i-a64-pinephone-1.0.dts (+1) |
| 95 | `arm64-dts-sun50i-a64-pinetab-Add-accelerometer.patch` | arm64: dts: sun50i-a64-pinetab: Add accelerometer | `000000000000` | sun50i-a64-pinetab.dts |
| 96 | `arm64-dts-sun50i-a64-pinetab-Name-sound-card-PineTab.patch` | arm64: dts: sun50i-a64-pinetab: Name sound card Pi... | `000000000000` | sun50i-a64-pinetab.dts |
| 97 | `arm64-dts-sun50i-a64-pinetab-enable-RTL8723CS-bluetooth.patch` | arm64: dts: sun50i-a64-pinetab: enable RTL8723CS b... | `000000000000` | sun50i-a64-pinetab.dts |
| 98 | `arm64-dts-sun50i-h5-Add-missing-GPU-trip-point.patch` | arm64: dts: sun50i-h5: Add missing GPU trip point | `000000000000` | sun50i-h5.dtsi |
| 99 | `arm64-dts-sun50i-h5-Use-my-own-more-aggressive-OPPs-on-H5.patch` | arm64: dts: sun50i-h5: Use my own more aggressive ... | `000000000000` | sun50i-h5-cpu-opp.dtsi |
| 100 | `arm64-xor-Select-32regs-without-benchmark-to-speed-up-boot.patch` | arm64: xor: Select 32regs without benchmark to spe... | `000000000000` | xor.h |
| 101 | `bluetooth-bcm-Restore-drive_rts_on_open-true-behavior-on-bcm207.patch` | bluetooth: bcm: Restore drive_rts_on_open = true b... | `000000000000` | hci_bcm.c |
| 102 | `bluetooth-h5-Don-t-re-initialize-rtl8723cs-on-resume.patch` | bluetooth: h5: Don't re-initialize rtl8723cs on re... | `000000000000` | hci_h5.c |
| 103 | `clk-sunxi-ng-Don-t-use-CPU-PLL-gating-and-CPUX-reparenting-to-H.patch` | clk: sunxi-ng: Don't use CPU PLL gating and CPUX r... | `000000000000` | ccu-sun8i-h3.c |
| 104 | `clk-sunxi-ng-Export-CLK_DRAM-for-devfreq.patch` | clk: sunxi-ng: Export CLK_DRAM for devfreq | `000000000000` | sun8i-a83t-ccu.h, ccu-sun8i-a83t.h |
| 105 | `clk-sunxi-ng-Mark-TWD-clocks-as-critical.patch` | clk: sunxi-ng: Mark TWD clocks as critical | `000000000000` | ccu-sun8i-r.c, ccu-sun50i-h6-r.c (+1) |
| 106 | `clk-sunxi-ng-Set-maximum-P-and-M-factors-to-1-for-H3-pll-cpux-c.patch` | clk: sunxi-ng: Set maximum P and M factors to 1 fo... | `000000000000` | ccu-sun8i-h3.c |
| 107 | `clk-sunxi-ng-a64-Increase-PLL_AUDIO-base-frequency.patch` | clk: sunxi-ng: a64: Increase PLL_AUDIO base freque... | `000000000000` | ccu-sun50i-a64.c |
| 108 | `clk-sunxi-ng-sun50i-a64-Switch-parent-of-MIPI-DSI-to-periph0-1x.patch` | clk: sunxi-ng: sun50i-a64: Switch parent of MIPI-D... | `000000000000` | ccu-sun50i-a64.c |
| 109 | `cpufreq-sun50i-Show-detected-CPU-bin-for-easier-debugging.patch` | cpufreq: sun50i: Show detected CPU bin, for easier... | `000000000000` | sun50i-cpufreq-nvmem.c |
| 110 | `drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch` | drm: bridge: dw-hdmi: Allow to accept HPD status f... | `000000000000` | dw-hdmi.c |
| 111 | `drm-bridge-dw-hdmi-Report-HDMI-hotplug-events.patch` | drm: bridge: dw-hdmi: Report HDMI hotplug events | `000000000000` | dw-hdmi.c |
| 112 | `drm-panel-st7703-Fix-xbd599-timings-to-make-refresh-rate-exactl.patch` | drm/panel: st7703: Fix xbd599 timings to make refr... | `000000000000` | panel-sitronix-st7703.c |
| 113 | `drm-sun4i-Implement-gamma-correction.patch` | drm/sun4i: Implement gamma correction | `000000000000` | sun4i_tcon.c, sun4i_tcon.h (+1) |
| 114 | `drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch` | drm/sun4i: Support taking over display pipeline st... | `000000000000` | sun6i_mipi_dsi.h, sun6i_mipi_dsi.c (+9) |
| 115 | `drm-sun4i-tcon-Support-keeping-dclk-rate-upon-ancestor-clock-ch.patch` | drm/sun4i: tcon: Support keeping dclk rate upon an... | `000000000000` | sun4i_tcon.c, sun4i_tcon.h |
| 116 | `dt-bindings-axp20x-adc-allow-to-use-TS-pin-as-GPADC.patch` | dt-bindings: axp20x-adc: allow to use TS pin as GP... | `000000000000` | x-powers,axp209-adc.yaml |
| 117 | `dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch` | dt-bindings: input: gpio-vibrator: Don't require e... | `000000000000` | gpio-vibrator.yaml |
| 118 | `dt-bindings-leds-Add-a-binding-for-AXP813-charger-led.patch` | dt-bindings: leds: Add a binding for AXP813 charge... | `000000000000` | leds-axp20x.yaml |
| 119 | `dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch` | dt-bindings: media: Add bindings for Himax HM5065 ... | `000000000000` | hm5065.txt |
| 120 | `dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch` | dt: bindings: mfd: Add codec related properties to... | `000000000000` | x-powers,ac100.yaml |
| 121 | `dt-bindings-sound-Add-jack-type-property-to-sun8i-a33-codec.patch` | dt-bindings: sound: Add jack-type property to sun8... | `000000000000` | allwinner,sun8i-a33-codec.yaml |
| 122 | `firmware-arm_scpi-Support-unidirectional-mailbox-channels.patch` | firmware: arm_scpi: Support unidirectional mailbox... | `000000000000` | arm_scpi.c |
| 123 | `firmware-scpi-Add-support-for-sending-a-SCPI_CMD_SET_SYS_PWR_ST.patch` | firmware: scpi: Add support for sending a SCPI_CMD... | `000000000000` | arm_scpi.c, scpi_protocol.h |
| 124 | `gnss-ubx-Send-soft-powerdown-message-on-suspend.patch` | gnss: ubx: Send soft powerdown message on suspend | `000000000000` | ubx.c |
| 125 | `hm5065-yaml-bindings-wip.patch` | hm5065: yaml bindings (wip) | `000000000000` | hm5065.yaml |
| 126 | `i2c-mv64xxx-Don-t-make-a-fuss-when-pinctrl-recovery-state-is-no.patch` | i2c: mv64xxx: Don't make a fuss when pinctrl recov... | `000000000000` | i2c-mv64xxx.c |
| 127 | `iio-adc-axp20x_adc-allow-to-set-TS-pin-to-GPADC-mode.patch` | iio: adc: axp20x_adc: allow to set TS pin to GPADC... | `000000000000` | axp20x_adc.c |
| 128 | `iio-adc-sun4i-gpadc-iio-Allow-to-use-sun5i-a13-gpadc-iio-from-D.patch` | iio: adc: sun4i-gpadc-iio: Allow to use sun5i-a13-... | `000000000000` | sun4i-gpadc-iio.c, sun5i.dtsi (+1) |
| 129 | `iio-st_sensors-Don-t-report-error-when-the-device-is-not-presen.patch` | iio: st_sensors: Don't report error when the devic... | `000000000000` | st_sensors_core.c |
| 130 | `input-cyttsp4-Clear-the-ids-buffer-in-a-saner-way.patch` | input: cyttsp4: Clear the ids buffer in a saner wa... | `000000000000` | cyttsp4_core.c |
| 131 | `input-cyttsp4-De-obfuscate-MT-signals-setup-platform-data.patch` | input: cyttsp4: De-obfuscate MT signals setup/plat... | `000000000000` | cyttsp4_core.c, cyttsp4.h (+1) |
| 132 | `input-cyttsp4-De-obfuscate-platform-data-for-keys.patch` | input: cyttsp4: De-obfuscate platform data for key... | `000000000000` | cyttsp4_core.c, cyttsp4.h |
| 133 | `input-cyttsp4-ENOSYS-error-is-ok-when-powering-up.patch` | input: cyttsp4: ENOSYS error is ok when powering u... | `000000000000` | cyttsp4_core.c |
| 134 | `input-cyttsp4-Faster-recovery-from-failed-wakeup-HACK.patch` | input: cyttsp4: Faster recovery from failed wakeup... | `000000000000` | cyttsp4_core.c |
| 135 | `input-cyttsp4-Fix-compile-issue.patch` | input: cyttsp4: Fix compile issue | `000000000000` | cyttsp4_core.c |
| 136 | `input-cyttsp4-Fix-probe-oops.patch` | input: cyttsp4: Fix probe oops | `000000000000` | cyttsp4_core.c |
| 137 | `input-cyttsp4-Fix-warnings.patch` | input: cyttsp4: Fix warnings | `000000000000` | cyttsp4_core.c |
| 138 | `input-cyttsp4-Make-the-driver-not-hog-the-system-s-workqueue.patch` | input: cyttsp4: Make the driver not hog the system... | `000000000000` | cyttsp4_core.c, cyttsp4_core.h |
| 139 | `input-cyttsp4-Port-the-driver-to-use-device-properties.patch` | input: cyttsp4: Port the driver to use device prop... | `000000000000` | cyttsp4_core.c, cyttsp4.h (+1) |
| 140 | `input-cyttsp4-Port-to-6.16.patch` | input: cyttsp4: Port to 6.16 | `000000000000` | cyttsp4_core.c |
| 141 | `input-cyttsp4-Remove-unused-enable_vkeys.patch` | input: cyttsp4: Remove unused enable_vkeys | `000000000000` | cyttsp4.h |
| 142 | `input-cyttsp4-Remove-useless-indirection-with-driver-platform-d.patch` | input: cyttsp4: Remove useless indirection with dr... | `000000000000` | cyttsp4_core.c, cyttsp4.h (+1) |
| 143 | `input-cyttsp4-Restart-on-wakeup-wakeup-by-I2C-read-doesn-t-work.patch` | input: cyttsp4: Restart on wakeup (wakeup by I2C r... | `000000000000` | cyttsp4_core.c |
| 144 | `input-cyttsp4-Use-i2c-spi-names-directly-in-the-driver.patch` | input: cyttsp4: Use i2c/spi names directly in the ... | `000000000000` | cyttsp4_spi.c, cyttsp4_i2c.c (+1) |
| 145 | `input-gpio-vibra-Allow-to-use-vcc-supply-alone-to-control-the-v.patch` | input: gpio-vibra: Allow to use vcc-supply alone t... | `000000000000` | gpio-vibra.c |
| 146 | `leds-axp20x-Support-charger-LED-on-AXP20x-like-PMICs.patch` | leds: axp20x: Support charger LED on AXP20x like P... | `000000000000` | Kconfig, leds-axp20x.c (+2) |
| 147 | `mailbox-Allow-to-run-mailbox-while-timekeeping-is-suspended.patch` | mailbox: Allow to run mailbox while timekeeping is... | `000000000000` | mailbox.c |
| 148 | `media-cedrus-Fix-failure-to-clean-up-hardware-on-probe-failure.patch` | media: cedrus: Fix failure to clean up hardware on... | `000000000000` | cedrus.c |
| 149 | `media-gc2145-Add-PIXEL_RATE-HBLANK-and-VBLANK-controls.patch` | media: gc2145: Add PIXEL_RATE, HBLANK and VBLANK c... | `000000000000` | gc2145.c |
| 150 | `media-gc2145-Added-BGGR-bayer-mode.patch` | media: gc2145: Added BGGR bayer mode | `000000000000` | gc2145.c |
| 151 | `media-gc2145-Disable-debug-output.patch` | media: gc2145: Disable debug output | `000000000000` | gc2145.c |
| 152 | `media-gc2145-Galaxycore-camera-module-driver.patch` | media: gc2145: Galaxycore camera module driver | `000000000000` | gc2145.c, Kconfig (+1) |
| 153 | `media-gc2145-fix-white-balance-colors.patch` | media: gc2145: fix white-balance colors | `000000000000` | gc2145.c |
| 154 | `media-gc2145-implement-system-suspend.patch` | media: gc2145: implement system suspend | `000000000000` | gc2145.c |
| 155 | `media-hm5065-Add-subdev-driver-for-Himax-HM5065-camera-sensor.patch` | media: hm5065: Add subdev driver for Himax HM5065 ... | `000000000000` | hm5065.c, Kconfig (+1) |
| 156 | `media-i2c-gc2145-Move-upstream-driver-out-of-the-way.patch` | media: i2c: gc2145: Move upstream driver out of th... | `000000000000` | Kconfig, Makefile |
| 157 | `media-i2c-gc2145-Parse-and-register-properties.patch` | media: i2c: gc2145: Parse and register properties | `000000000000` | gc2145.c |
| 158 | `media-ov5640-Add-read-only-property-for-vblank.patch` | media: ov5640: Add read-only property for vblank | `000000000000` | ov5640.c |
| 159 | `media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch` | media: ov5640: Don't powerup the sensor during dri... | `000000000000` | ov5640.c |
| 160 | `media-ov5640-Experiment-Try-to-disable-denoising-sharpening.patch` | media: ov5640: [Experiment] Try to disable denoisi... | `000000000000` | ov5640.c |
| 161 | `media-ov5640-Fix-focus-commands-blocking-until-complete.patch` | media: ov5640: Fix focus commands blocking until c... | `000000000000` | ov5640.c |
| 162 | `media-ov5640-Implement-autofocus.patch` | media: ov5640: Implement autofocus | `000000000000` | ov5640.c |
| 163 | `media-ov5640-Improve-error-reporting.patch` | media: ov5640: Improve error reporting | `000000000000` | ov5640.c |
| 164 | `media-ov5640-Improve-firmware-load-time.patch` | media: ov5640: Improve firmware load time | `000000000000` | ov5640.c |
| 165 | `media-ov5640-Sleep-after-poweroff-to-ensure-next-poweron-is-not.patch` | media: ov5640: Sleep after poweroff to ensure next... | `000000000000` | ov5640.c |
| 166 | `media-ov5640-set-default-ae-target-lower.patch` | media: ov5640: set default ae target lower | `000000000000` | ov5640.c |
| 167 | `media-ov5640-use-pm_runtime_force_suspend-resume-for-system-sus.patch` | media: ov5640: use pm_runtime_force_suspend/resume... | `000000000000` | ov5640.c |
| 168 | `media-ov5648-Fix-call-to-pm_runtime_set_suspended.patch` | media: ov5648: Fix call to pm_runtime_set_suspende... | `000000000000` | ov5648.c |
| 169 | `media-sun6i-csi-Add-multicamera-support-for-parallel-bus.patch` | media: sun6i-csi: Add multicamera support for para... | `000000000000` | sun6i_csi_bridge.h, sun6i_csi_bridge.c |
| 170 | `media-sun6i-csi-add-V4L2_CAP_IO_MC-capability.patch` | media: sun6i-csi: add V4L2_CAP_IO_MC capability | `000000000000` | sun6i_csi_capture.c |
| 171 | `media-sun6i-csi-capture-Use-subdev-operation-to-access-bridge-f.patch` | media: sun6i-csi: capture: Use subdev operation to... | `000000000000` | sun6i_csi_bridge.h, sun6i_csi_capture.c (+1) |
| 172 | `media-sun6i-csi-implement-vidioc_enum_framesizes.patch` | media: sun6i-csi: implement vidioc_enum_framesizes | `000000000000` | sun6i_csi_capture.c |
| 173 | `media-sun6i-csi-merge-sun6i_csi_formats-and-sun6i_csi_formats_m.patch` | media: sun6i-csi: merge sun6i_csi_formats and sun6... | `000000000000` | sun6i_csi_capture.h, sun6i_csi_capture.c |
| 174 | `media-sun6i-csi-subdev-Use-subdev-active-state-to-store-active-.patch` | media: sun6i-csi: subdev: Use subdev active state ... | `000000000000` | sun6i_csi_bridge.h, sun6i_csi_bridge.c |
| 175 | `mfd-axp20x-Add-battery-IRQ-resources.patch` | mfd: axp20x: Add battery IRQ resources | `000000000000` | axp20x.c |
| 176 | `misc-modem-power-Power-manager-for-modems.patch` | misc: modem-power: Power manager for modems | `000000000000` | Makefile, modem-power.c (+1) |
| 177 | `mmc-add-delay-after-power-class-selection.patch` | mmc: add delay after power class selection | `000000000000` | mmc.c |
| 178 | `mmc-sunxi-mmc-Remove-runtime-PM.patch` | mmc: sunxi-mmc: Remove runtime-PM | `000000000000` | sunxi-mmc.c |
| 179 | `mtd-spi-nor-Add-Alliance-memory-support.patch` | mtd: spi-nor: Add Alliance memory support | `000000000000` | Makefile, core.h (+2) |
| 180 | `mtd-spi-nor-Add-vdd-regulator-support.patch` | mtd: spi-nor: Add vdd regulator support | `000000000000` | core.c |
| 181 | `net-stmmac-sun8i-Add-support-for-enabling-a-regulator-for-PHY-I.patch` | net: stmmac: sun8i: Add support for enabling a reg... | `000000000000` | dwmac-sun8i.c |
| 182 | `net-stmmac-sun8i-Rename-PHY-regulator-variable-to-regulator_phy.patch` | net: stmmac: sun8i: Rename PHY regulator variable ... | `000000000000` | dwmac-sun8i.c |
| 183 | `net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch` | net: stmmac: sun8i: Use devm_regulator_get for PHY... | `000000000000` | dwmac-sun8i.c |
| 184 | `nfc-pn544-Add-support-for-VBAT-PVDD-regulators.patch` | nfc: pn544: Add support for VBAT/PVDD regulators | `000000000000` | i2c.c |
| 185 | `of-property-fw_devlink-Support-allwinner-sram-links.patch` | of: property: fw_devlink: Support allwinner,sram l... | `000000000000` | property.c |
| 186 | `opp-core-Avoid-confusing-error-when-no-regulator-is-defined-in-.patch` | opp: core: Avoid confusing error when no regulator... | `000000000000` | core.c |
| 187 | `pci-Workaround-ITS-timeouts-on-poweroff-reboot-on-Orange-Pi-5-P.patch` | pci: Workaround ITS timeouts on poweroff/reboot on... | `000000000000` | portdrv.c |
| 188 | `phy-allwinner-sun4i-usb-Add-support-for-usb_role_switch.patch` | phy: allwinner: sun4i-usb: Add support for usb_rol... | `000000000000` | phy-sun4i-usb.c, Kconfig |
| 189 | `power-axp20x_battery-Allow-to-set-target-voltage-to-4.35V.patch` | power: axp20x_battery: Allow to set target voltage... | `000000000000` | axp20x_battery.c |
| 190 | `power-axp803-Add-interrupts-for-low-battery-power-condition.patch` | power: axp803: Add interrupts for low battery powe... | `000000000000` | axp20x_battery.c, axp20x.c |
| 191 | `power-supply-Add-support-for-USB_BC_ENABLED-and-USB_DCP_INPUT_C.patch` | power: supply: Add support for USB_BC_ENABLED and | `000000000000` | power_supply.h, power_supply_sysfs.c |
| 192 | `power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch` | power: supply: axp20x-battery: Add support for | `000000000000` | axp20x_battery.c |
| 193 | `power-supply-axp20x-battery-Enable-poweron-by-RTC-alarm.patch` | power: supply: axp20x-battery: Enable poweron by R... | `000000000000` | axp20x_battery.c |
| 194 | `power-supply-axp20x-battery-Improve-probe-error-reporting.patch` | power: supply: axp20x-battery: Improve probe error... | `000000000000` | axp20x_battery.c |
| 195 | `power-supply-axp20x-battery-Support-POWER_SUPPLY_PROP_CHARGE_BE.patch` | power: supply: axp20x-battery: Support | `000000000000` | axp20x_battery.c |
| 196 | `power-supply-axp20x-usb-power-Add-missing-interrupts.patch` | power: supply: axp20x-usb-power: Add missing inter... | `000000000000` | axp20x_usb_power.c, axp20x.c |
| 197 | `power-supply-axp20x-usb-power-Change-Vbus-hold-voltage-to-4.5V.patch` | power: supply: axp20x-usb-power: Change Vbus hold ... | `000000000000` | axp20x_usb_power.c |
| 198 | `power-supply-axp20x_battery-Add-support-for-reporting-OCV.patch` | power: supply: axp20x_battery: Add support for rep... | `000000000000` | axp20x_battery.c |
| 199 | `power-supply-axp20x_battery-Fix-charging-done-detection.patch` | power: supply: axp20x_battery: Fix charging done d... | `000000000000` | axp20x_battery.c |
| 200 | `power-supply-axp20x_battery-Monitor-battery-health.patch` | power: supply: axp20x_battery: Monitor battery hea... | `000000000000` | axp20x_battery.c |
| 201 | `power-supply-axp20x_battery-Send-uevents-for-status-changes.patch` | power: supply: axp20x_battery: Send uevents for st... | `000000000000` | axp20x_battery.c |
| 202 | `power-supply-axp20x_battery-Setup-thermal-regulation-experiment.patch` | power: supply: axp20x_battery: Setup thermal regul... | `000000000000` | axp20x_battery.c |
| 203 | `regulator-Add-simple-driver-for-enabling-a-regulator-from-users.patch` | regulator: Add simple driver for enabling a regula... | `000000000000` | userspace-consumer-of.c, Kconfig (+1) |
| 204 | `regulator-axp20x-Add-support-for-vin-supply-for-drivevbus.patch` | regulator: axp20x: Add support for vin-supply for ... | `000000000000` | axp20x-regulator.c |
| 205 | `regulator-axp20x-Enable-over-temperature-protection-and-16s-res.patch` | regulator: axp20x: Enable over-temperature protect... | `000000000000` | axp20x-regulator.c |
| 206 | `regulator-axp20x-Turn-N_VBUSEN-to-input-on-x-powers-sense-vbus-.patch` | regulator: axp20x: Turn N_VBUSEN to input on x-pow... | `000000000000` | sun50i-a64-pinephone-1.2.dts, axp20x-regulator.c |
| 207 | `regulator-tp65185-Add-hwmon-device-for-reading-temperature.patch` | regulator: tp65185: Add hwmon device for reading t... | `000000000000` | tp65185x.c |
| 208 | `regulator-tp65185x-Add-tp65185x-eInk-panel-regulator-driver.patch` | regulator: tp65185x: Add tp65185x eInk panel regul... | `000000000000` | Kconfig, Makefile (+1) |
| 209 | `rtc-Print-which-error-caused-RTC-read-failure.patch` | rtc: Print which error caused RTC read failure | `000000000000` | class.c |
| 210 | `rtc-sun6i-Allow-RTC-wakeup-after-shutdown.patch` | rtc: sun6i: Allow RTC wakeup after shutdown | `000000000000` | rtc-sun6i.c |
| 211 | `sound-soc-ac100-codec-Support-analog-part-of-X-Powers-AC100-cod.patch` | sound: soc: ac100-codec: Support analog part of X-... | `000000000000` | ac100.h, ac100.c (+3) |
| 212 | `sound-soc-sun8i-codec-Add-support-for-digital-part-of-the-AC100.patch` | sound: soc: sun8i-codec: Add support for digital p... | `000000000000` | Kconfig, sun8i-codec.c |
| 213 | `sunxi-Use-dev_err_probe-to-handle-EPROBE_DEFER-errors.patch` | sunxi: Use dev_err_probe to handle EPROBE_DEFER er... | `000000000000` | i2c-gpio.c, topology.c (+3) |
| 214 | `thermal-sun8i-Be-loud-when-probe-fails.patch` | thermal: sun8i: Be loud when probe fails | `000000000000` | sun8i_thermal.c |
| 215 | `usb-gadget-Fix-dangling-pointer-in-netdev-private-data.patch` | usb: gadget: Fix dangling pointer in netdev privat... | `000000000000` | f_ecm.c, f_ncm.c (+4) |
| 216 | `usb-musb-sunxi-Avoid-enabling-host-side-code-on-SoCs-where-it-s.patch` | usb: musb: sunxi: Avoid enabling host side code on... | `000000000000` | sunxi.c, musb_core.c |
| 217 | `usb-serial-option-add-reset_resume-callback-for-WWAN-devices.patch` | usb: serial: option: add 'reset_resume' callback f... | `000000000000` | option.c |
| 218 | `usb-typec-altmodes-displayport-Respect-DP_CAP_RECEPTACLE-bit.patch` | usb: typec: altmodes: displayport: Respect DP_CAP_... | `000000000000` | displayport.c |
| 219 | `usb-typec-anx7688-Add-driver-for-ANX7688-USB-C-HDMI-bridge.patch` | usb: typec: anx7688: Add driver for ANX7688 USB-C ... | `000000000000` | anx7688.c, Makefile (+1) |
| 220 | `usb-typec-fusb302-Add-OF-extcon-support.patch` | usb: typec: fusb302: Add OF extcon support | `000000000000` | fusb302.c |
| 221 | `usb-typec-fusb302-Clear-interrupts-before-we-start-toggling.patch` | usb: typec: fusb302: Clear interrupts before we st... | `000000000000` | fusb302.c |
| 222 | `usb-typec-fusb302-Extend-debugging-interface-with-driver-state-.patch` | usb: typec: fusb302: Extend debugging interface wi... | `000000000000` | fusb302.c |
| 223 | `usb-typec-fusb302-Fix-register-definitions.patch` | usb: typec: fusb302: Fix register definitions | `000000000000` | fusb302_reg.h |
| 224 | `usb-typec-fusb302-More-useful-of-logging-status-on-interrupt.patch` | usb: typec: fusb302: More useful of logging status... | `000000000000` | fusb302.c |
| 225 | `usb-typec-fusb302-Retry-reading-of-CC-pins-status-if-activity-i.patch` | usb: typec: fusb302: Retry reading of CC pins stat... | `000000000000` | fusb302.c |
| 226 | `usb-typec-fusb302-Set-the-current-before-enabling-pullups.patch` | usb: typec: fusb302: Set the current before enabli... | `000000000000` | fusb302.c |
| 227 | `usb-typec-fusb302-Slightly-increase-wait-time-for-BC1.2-result.patch` | usb: typec: fusb302: Slightly increase wait time f... | `000000000000` | fusb302.c |
| 228 | `usb-typec-fusb302-Update-VBUS-state-even-if-VBUS-interrupt-is-n.patch` | usb: typec: fusb302: Update VBUS state even if VBU... | `000000000000` | fusb302.c |
| 229 | `usb-typec-tcpm-Fix-PD-devices-capabilities-registration.patch` | usb: typec: tcpm: Fix PD devices/capabilities regi... | `000000000000` | tcpm.c |
| 230 | `usb-typec-tcpm-Improve-logs.patch` | usb: typec: tcpm: Improve logs | `000000000000` | tcpm.c |
| 231 | `usb-typec-tcpm-Unregister-altmodes-before-registering-new-ones.patch` | usb: typec: tcpm: Unregister altmodes before regis... | `000000000000` | tcpm.c |
| 232 | `usb-typec-typec-extcon-Add-typec-extcon-bridge-driver.patch` | usb: typec: typec-extcon: Add typec -> extcon brid... | `000000000000` | typec-extcon.c, Makefile (+1) |
| 233 | `usb-typec-typec-extcon-Allow-to-force-reset-on-each-mux-change.patch` | usb: typec: typec-extcon: Allow to force reset on ... | `000000000000` | typec-extcon.c |
| 234 | `usb-typec-typec-extcon-Enable-debugging-for-now.patch` | usb: typec: typec-extcon: Enable debugging for now | `000000000000` | typec-extcon.c |
| 235 | `video-fbdev-eInk-display-driver-for-A13-based-PocketBooks.patch` | video: fbdev: eInk display driver for A13 based Po... | `000000000000` | sun5i-eink-neon.c, Kconfig (+3) |
| 236 | `video-pwm_bl-Allow-to-change-lth_brightness-via-sysfs.patch` | video: pwm_bl: Allow to change lth_brightness via ... | `000000000000` | pwm_bl.c |

## How to Verify Patches in Mainline

To check if these patches are in Linux kernel 6.18, you can:

### Method 1: Search by Commit ID

For patches with commit IDs (indicated in the table above):

```bash
# Clone the Linux kernel (if not already done)
git clone --depth=1 --branch v6.18 \
  https://github.com/torvalds/linux.git

cd linux

# Check if a commit exists
git cat-file -t <commit-id>
```

### Method 2: Search by Subject

```bash
# Search git log for a specific subject
git log --all --grep "subject line" --oneline
```

### Method 3: Use GitHub Search

1. Go to https://github.com/torvalds/linux
2. Search for the patch subject or modified file names
3. Check the commit history for the v6.18 tag

### Method 4: Use git.kernel.org

1. Visit https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
2. Use the search feature to find commits by:
   - Commit message (subject)
   - File path
   - Author name

## Patch Information Export

For automated verification, here's a list of commit IDs to check:

```
0000000000000000000000000000000000000000
2a8a9e3104ce70230ca67a39fd406d84662e77b2
2ce741f43a65732bd9078046c272743d06a41701
```

## Notes

- This analysis is based on patch file metadata only
- Patches may have been modified when merged upstream
- Some patches might be split into multiple commits or combined
- The commit ID in a patch comes from the original source tree (e.g., vendor kernel)
- Manual verification is recommended for definitive confirmation
