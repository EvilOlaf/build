# Patch Analysis Report: sunxi-6.16 vs Linux Kernel 6.18

**Patch Directory:** `patch/kernel/archive/sunxi-6.16`

**Analysis Date:** 2025-12-06 18:06:53

## Summary

- **Total Patches Analyzed:** 444
- **Patches with Commit IDs:** 444
- **Unique Files Modified:** 598

## Patches by Subsystem

| Subsystem | Count |
|-----------|-------|
| arch | 207 |
| drivers | 195 |
| include | 15 |
| sound | 13 |
| Documentation | 10 |
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
| `arch/arm64/boot/dts/allwinner/Makefile` | 12 |
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
| `drivers/gpu/drm/sun4i/sun8i_vi_layer.c` | 7 |
| `drivers/gpu/drm/sun4i/sun8i_csc.c` | 7 |
| `arch/arm64/boot/dts/allwinner/sun50i-a64-pinephone-1.1.dts` | 6 |
| `arch/arm64/boot/dts/allwinner/sun50i-h6-orangepi-3.dts` | 6 |
| `arch/arm/boot/dts/allwinner/sunxi-h3-h5.dtsi` | 6 |

## Detailed Patch List

Complete list of all patches, organized by directory:

### patches.armbian (176 patches)

| # | Patch File | Subject | Commit ID | Files Changed |
|---|------------|---------|-----------|---------------|
| 1 | `ARM-dts-sun8i-nanopiduo2-Use-key-0-as-power-button.patch` | ARM: dts: sun8i: nanopiduo2: Use key-0 as power bu... | `000000000000` | sun8i-h3-nanopi-duo2.dts |
| 2 | `ARM-dts-sun8i-nanopiduo2-enable-ethernet.patch` | ARM: dts: sun8i: nanopiduo2: enable ethernet | `000000000000` | sun8i-h3-nanopi-duo2.dts |
| 3 | `ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-EMAC1.patch` | ARM64: dts: sun50i-h616: BigTreeTech CB1: Enable E... | `000000000000` | sun50i-h616-bigtreetech-cb1.dtsi |
| 4 | `ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-HDMI.patch` | ARM64: dts: sun50i-h616: BigTreeTech CB1: Enable H... | `f3157390fffb` | sun50i-h616-bigtreetech-cb1.dtsi |
| 5 | `ASoC-AC200-Initial-driver.patch` | ASoC: AC200: Initial driver | `c1601a5d5088` | ac200.c, Makefile (+1) |
| 6 | `Add-BananaPi-BPI-M4-Zero-overlays.patch` | Add BananaPi BPI-M4-Zero overlays | `43a717756368` | sun50i-h616-bananapi-m4-sdio-wifi-bt.dtso, sun50i-h616-bananapi-m4-spi1-cs1-spidev.dtso (+12) |
| 7 | `Add-BananaPi-BPI-M4-Zero-pinctrl.patch` | Add BananaPi BPI-M4-Zero pinctrl | `074c33f4b2b6` | sun50i-h616.dtsi |
| 8 | `Add-FB_TFT-ST7796S-driver.patch` | Add: FB_TFT ST7796S driver | `0987e0158d63` | Makefile, fb_st7796s.c (+1) |
| 9 | `Add-HDMI-support-for-pcDuino-1-and-2-by-including-HDMI-and-DE-n.patch` | Add HDMI support for pcDuino 1 and 2 by including ... | `23514cbc2642` | sun4i-a10-pcduino.dts |
| 10 | `Add-HDMI-support-for-pcDuino-3-by-including-HDMI-and-DE-nodes.patch` | Add HDMI support for pcDuino 3 by including HDMI a... | `8225e98fe295` | sun7i-a20-pcduino3.dts |
| 11 | `Add-dump_reg-and-sunxi-sysinfo-drivers.patch` | Add dump_reg and sunxi-sysinfo drivers | `0ebd4ab1a25d` | Makefile, sunxi-sysinfo.c (+8) |
| 12 | `Add-sunxi-addr-driver-Used-to-fix-uwe5622-bluetooth-MAC-address.patch` | Add sunxi-addr driver - Used to fix uwe5622 blueto... | `836de5e4296b` | Kconfig, sha256.c (+4) |
| 13 | `Add-wifi-nodes-for-Inovato-Quadra.patch` | Add wifi nodes for Inovato Quadra | `6b1d64060b59` | Makefile, sun50i-h6-inovato-quadra.dts |
| 14 | `Add-ws2812-RGB-driver-for-allwinner-H616.patch` | Add: ws2812 RGB driver for allwinner H616 | `4546be7fd381` | leds-ws2812.c, Makefile (+1) |
| 15 | `BigTreeTech-CB1-dts-i2c-gpio-mode-adjustment-and-ws2812-rgb_val.patch` | BigTreeTech CB1: dts: i2c gpio mode adjustment and... | `20dc0b0f3da7` | sun50i-h616-bigtreetech-cb1-emmc.dts, sun50i-h616-bigtreetech-cb1-sd.dts (+1) |
| 16 | `Compile-the-pwm-overlay.patch` | Compile the pwm overlay | `000000000000` | Makefile |
| 17 | `Correct-perf-interrupt-source-number-as-referenced-in-the-Allwi.patch` | Correct perf interrupt source number as referenced... | `000000000000` | sun4i-a10.dtsi |
| 18 | `Doc-dt-bindings-usb-add-binding-for-DWC3-controller-on-Allwinne.patch` | Doc:dt-bindings:usb: add binding for DWC3 controll... | `846209f909c9` | allwinner,dwc3.txt |
| 19 | `Enable-DMA-support-for-the-Allwinner-A10-EMAC-which-already-exi.patch` | Enable DMA support for the Allwinner A10 EMAC, whi... | `000000000000` | sun4i-a10.dtsi |
| 20 | `Enable-creation-of-__symbols__-node.patch` | Enable creation of __symbols__ node | `000000000000` | Makefile.dtbs |
| 21 | `Fix-ghost-touches-on-tsc2007-tft-screen.patch` | Fix ghost touches on tsc2007 tft screen | `b75f5bf0d822` | tsc2007.h, tsc2007.h (+2) |
| 22 | `Fix-include-uapi-spi-spidev-module.patch` | Fix include uapi spi spidev module | `000000000000` | spidev.c |
| 23 | `Input-axp20x-pek-allow-wakeup-after-shutdown.patch` | Input: axp20x-pek - allow wakeup after shutdown | `000000000000` | axp20x-pek.c |
| 24 | `LED-green_power_on-red_status_heartbeat-arch-arm64-boot-dts-all.patch` | LED-green_power_on-red_status_heartbeat | `000000000000` | sun50i-h616-orangepi-zero.dtsi |
| 25 | `Makefile-CONFIG_SHELL-fix-for-builddeb-packaging.patch` | Makefile: CONFIG_SHELL fix for builddeb packaging | `836e3c6dde41` | Makefile |
| 26 | `Move-sun50i-h6-pwm-settings-to-its-own-overlay.patch` | Move sun50i-h6-pwm settings to its own overlay | `17c23b36efb6` | sun50i-h6-pwm.dtso, sun50i-h6-fixup.scr-cmd |
| 27 | `Optimize-TSC2007-touchscreen-add-polling-method.patch` | Optimize: TSC2007 touchscreen add polling method | `baabc51678fa` | tsc2007.h, tsc2007_core.c |
| 28 | `Revert-drm-sun4i-hdmi-switch-to-struct-drm_edid.patch` | Revert "drm/sun4i: hdmi: switch to struct drm_edid... | `aec6c912e969` | sun4i_hdmi_enc.c |
| 29 | `Sound-for-H616-H618-Allwinner-SOCs.patch` | Sound for H616, H618 Allwinner SOCs | `4a2e4646db5c` | snd_sunxi_ahub.c, soc-dai.h (+18) |
| 30 | `Temp_fix-mailbox-arch-arm64-boot-dts-allwinner-sun50i-a64-pinep.patch` | Temp_fix mailbox | `ef5deb15a48b` | sun50i-a64-pinephone.dtsi |
| 31 | `add-dtb-overlay-for-zero2w.patch` | add dtb overlay for zero2w | `4b2f43e4e23c` | sun50i-h616-i2c2-pi.dtso, sun50i-h616-i2c0-pi.dtso (+3) |
| 32 | `add-initial-support-for-orangepi3-lts.patch` | add initial support for orangepi3-lts | `c8c7ccf8c9b5` | Makefile, sun50i-h6-orangepi-3-lts.dts |
| 33 | `add-nodes-for-sunxi-info-sunxi-addr-and-sunxi-dump-reg.patch` | add nodes for sunxi-info, sunxi-addr and sunxi-dum... | `542310e242c4` | sun50i-h6.dtsi, sun50i-h616.dtsi |
| 34 | `arm-arm64-dts-Add-leds-axp20x-charger.patch` | arm:arm64:dts: Add leds axp20x charger | `000000000000` | axp803.dtsi, axp209.dtsi (+2) |
| 35 | `arm-dts-Add-sun8i-h2-plus-nanopi-duo-device.patch` | arm:dts: Add sun8i-h2-plus-nanopi-duo device | `379b3c9bf09d` | sun8i-h2-plus-nanopi-duo.dts, Makefile |
| 36 | `arm-dts-Add-sun8i-h2-plus-sunvell-r69-device.patch` | arm:dts: Add sun8i-h2-plus-sunvell-r69 device | `484b8abd16c1` | sun8i-h2-plus-sunvell-r69.dts, Makefile |
| 37 | `arm-dts-a10-cubiebord-a20-cubietruck-green-LED-mmc0-default-tri.patch` | arm:dts: a10-cubiebord a20-cubietruck green LED mm... | `000000000000` | sun7i-a20-cubietruck.dts, sun4i-a10-cubieboard.dts |
| 38 | `arm-dts-a20-orangepi-and-mini-fix-phy-mode-hdmi.patch` | arm:dts: a20-orangepi and mini fix phy-mode, hdmi | `000000000000` | sun7i-a20-orangepi-mini.dts, sun7i-a20-orangepi.dts |
| 39 | `arm-dts-h3-nanopi-neo-Add-regulator-leds-mmc2.patch` | arm:dts: h3-nanopi-neo Add regulator, leds, mmc2 | `000000000000` | sun8i-h3-nanopi-neo.dts |
| 40 | `arm-dts-h3-nanopi-neo-air-Add-regulator-camera-wifi-bluetooth-o.patch` | arm:dts: h3-nanopi-neo-air Add regulator camera wi... | `000000000000` | sun8i-h3-nanopi-neo-air.dts |
| 41 | `arm-dts-h3-orangepi-2-Add-regulator-vdd-cpu.patch` | arm:dts: h3-orangepi-2 Add regulator vdd cpu | `000000000000` | sun8i-h3-orangepi-2.dts |
| 42 | `arm-dts-overlay-Add-Overlays-for-sunxi.patch` | arm:dts:overlay Add Overlays for sunxi | `3110211a08b8` | sun8i-r40-spi-spidev1.dtso, sun7i-a20-mmc2.dtso (+95) |
| 43 | `arm-dts-overlay-sun8i-h3-cpu-clock-add-overclock.patch` | arm:dts:overlay: sun8i-h3-cpu-clock add overclock | `ec30b77c7935` | sun8i-h3-cpu-clock-1.3GHz-1.3v.dtso, sun8i-h3-cpu-clock-1.2GHz-1.3v.dtso (+2) |
| 44 | `arm-dts-sun5i-a13-olinuxino-Add-panel-lcd-olinuxino-4.3-needed-.patch` | arm:dts:sun5i-a13-olinuxino Add panel lcd-olinuxin... | `000000000000` | sun5i-a13-olinuxino.dts |
| 45 | `arm-dts-sun5i-a13-olinuxino-micro-add-panel-lcd-olinuxino-4.3.patch` | arm:dts:sun5i-a13-olinuxino-micro add panel lcd-ol... | `000000000000` | sun5i-a13-olinuxino-micro.dts |
| 46 | `arm-dts-sun7i-a20-Disable-OOB-IRQ-for-brcm-wifi-on-Cubietruck-a.patch` | arm:dts:sun7i-a20 Disable OOB IRQ for brcm-wifi on... | `000000000000` | sun7i-a20-cubietruck.dts, sun7i-a20-bananapro.dts |
| 47 | `arm-dts-sun7i-a20-bananapro-add-AXP209-regulators.patch` | arm: dts: sun7i-a20-bananapro: add AXP209 regulato... | `000000000000` | sun7i-a20-bananapro.dts |
| 48 | `arm-dts-sun7i-a20-bananapro-add-hdmi-connector-de.patch` | arm:dts: sun7i-a20-bananapro add hdmi-connector, d... | `000000000000` | sun7i-a20-bananapro.dts |
| 49 | `arm-dts-sun7i-a20-cubietruck-add-alias-uart2.patch` | arm:dts: sun7i-a20-cubietruck add alias uart2 | `000000000000` | sun7i-a20-cubietruck.dts |
| 50 | `arm-dts-sun7i-a20-olimex-som-204-evb-olinuxino-micro-decrease-d.patch` | arm:dts:sun7i-a20: olimex-som(204)-evb,olinuxino-m... | `000000000000` | sun7i-a20-olinuxino-micro.dts, sun7i-a20-olimex-som204-evb.dts (+1) |
| 51 | `arm-dts-sun7i-a20-olinuxino-lime2-enable-audio-codec.patch` | arm:dts:sun7i-a20-olinuxino-lime2 enable audio cod... | `000000000000` | sun7i-a20-olinuxino-lime2.dts |
| 52 | `arm-dts-sun7i-a20-olinuxino-lime2-enable-ldo3-always-on.patch` | arm:dts:sun7i-a20-olinuxino-lime2 enable ldo3 alwa... | `000000000000` | sun7i-a20-olinuxino-lime2.dts |
| 53 | `arm-dts-sun7i-a20-olinuxino-micro-emmc-Add-vqmmc-node.patch` | arm:dts:sun7i-a20-olinuxino-micro-emmc Add vqmmc n... | `000000000000` | sun7i-a20-olinuxino-micro-emmc.dts |
| 54 | `arm-dts-sun8i-h2-plus-orangepi-zero-fix-usb_otg-dr_mode.patch` | arm: dts: sun8i-h2-plus-orangepi-zero: fix usb_otg... | `2f8b8f221f69` | sun8i-h2-plus-orangepi-zero.dts |
| 55 | `arm-dts-sun8i-h2-plus-orangepi-zero-fix-xradio-interrupt.patch` | arm:dts: sun8i-h2-plus-orangepi-zero fix xradio in... | `000000000000` | sun8i-h2-plus-orangepi-zero.dts |
| 56 | `arm-dts-sun8i-h3-add-thermal-zones.patch` | arm:dts:sun8i-h3 add thermal zones | `000000000000` | sun8i-h3.dtsi |
| 57 | `arm-dts-sun8i-h3-bananapi-m2-plus-add-wifi_pwrseq.patch` | arm:dts:sun8i-h3-bananapi-m2-plus add wifi_pwrseq | `000000000000` | sun8i-h3-bananapi-m2-plus.dts |
| 58 | `arm-dts-sun8i-h3-nanopi-add-leds-pio-pins.patch` | arm:dts: sun8i-h3-nanopi add leds pio pins | `000000000000` | sun8i-h3-nanopi.dtsi |
| 59 | `arm-dts-sun8i-h3-orangepi-pc-plus-add-wifi_pwrseq.patch` | arm:dts: sun8i-h3-orangepi-pc-plus add wifi_pwrseq | `000000000000` | sun8i-h3-orangepi-pc-plus.dts |
| 60 | `arm-dts-sun8i-h3-reduce-opp-microvolt-to-prevent-not-supported-.patch` | arm: dts: sun8i: h3: reduce opp-microvolt to preve... | `000000000000` | sun8i-h3.dtsi |
| 61 | `arm-dts-sun8i-r40-add-clk_out_a-fix-bananam2ultra.patch` | arm:dts: sun8i-r40 add clk_out_a fix bananam2ultra | `000000000000` | sun8i-r40.dtsi |
| 62 | `arm-dts-sun8i-r40-bananapi-m2-ultra-add-codec-analog.patch` | arm:dts: sun8i-r40 bananapi-m2-ultra add codec ana... | `000000000000` | sun8i-r40.dtsi, sun8i-r40-bananapi-m2-ultra.dts |
| 63 | `arm-dts-sun8i-v3s-s3-pinecube-enable-sound-codec.patch` | arm:dts: sun8i-v3s/s3-pinecube enable sound codec | `404a4f5b185c` | sun8i-v3s.dtsi, sun8i-s3-pinecube.dts |
| 64 | `arm-dts-sun9i-a80-add-thermal-sensor.patch` | arm:dts: sun9i-a80 add thermal sensor | `000000000000` | sun9i-a80.dtsi |
| 65 | `arm-dts-sun9i-a80-add-thermal-zone.patch` | arm:dts: sun9i-a80 add thermal zone | `000000000000` | sun9i-a80.dtsi |
| 66 | `arm-dts-sunxi-h3-h5.dtsi-add-i2s0-i2s1-pins.patch` | arm:dts:sunxi-h3-h5.dtsi add i2s0 i2s1 pins | `000000000000` | sunxi-h3-h5.dtsi |
| 67 | `arm-dts-sunxi-h3-h5.dtsi-force-mmc0-bus-width.patch` | arm:dts: sunxi-h3-h5.dtsi force mmc0 bus-width | `000000000000` | sunxi-h3-h5.dtsi |
| 68 | `arm-patch-call-flush_icache-ASAP-after-writing-new-instruction.patch` | arm/patch: call flush_icache ASAP after writing ne... | `000000000000` | patch.c |
| 69 | `arm64-allwinner-Add-sun50i-h618-bananapi-m4-berry-support.patch` | arm64: allwinner: Add sun50i-h618-bananapi-m4-berr... | `3d72091622a7` | Makefile, sun50i-h616.dtsi (+1) |
| 70 | `arm64-dts-Add-sun50i-h5-nanopi-k1-plus-device.patch` | arm64:dts: Add sun50i-h5-nanopi-k1-plus device | `76fd556315dd` | Makefile, sun50i-h5-nanopi-k1-plus.dts |
| 71 | `arm64-dts-Add-sun50i-h5-nanopi-m1-plus2-device.patch` | arm64:dts: Add sun50i-h5-nanopi-m1-plus2 device | `545864cca39f` | Makefile, sun50i-h5-nanopi-m1-plus2.dts |
| 72 | `arm64-dts-Add-sun50i-h5-nanopi-neo-core2-device.patch` | arm64:dts: Add sun50i-h5-nanopi-neo-core2 device | `67cacba5ece1` | Makefile, sun50i-h5-nanopi-neo-core2.dts |
| 73 | `arm64-dts-Add-sun50i-h5-nanopi-neo2-v1.1-device.patch` | arm64:dts: Add sun50i-h5-nanopi-neo2-v1.1 device | `24eef32e5d45` | Makefile, sun50i-h5-nanopi-neo2-v1.1.dts |
| 74 | `arm64-dts-FIXME-a64-olinuxino-add-regulator-audio-mmc.patch` | arm64:dts: FIXME: a64-olinuxino add regulator audi... | `000000000000` | sun50i-a64-olinuxino.dts |
| 75 | `arm64-dts-add-sun50i-h618-cpu-dvfs.dtsi.patch` | arm64: dts: add sun50i-h618-cpu-dvfs.dtsi | `ead3bcfa953e` | sun50i-h618-cpu-dvfs.dtsi, sun50i-h616-orangepi-zero.dtsi (+2) |
| 76 | `arm64-dts-allwinner-Add-axp313a.dtsi.patch` | arm64: dts: allwinner: Add axp313a.dtsi | `1989d73c62ac` | axp313a.dtsi |
| 77 | `arm64-dts-allwinner-h6-Add-AC200-EPHY-nodes.patch` | arm64: dts: allwinner: h6: Add AC200 EPHY nodes | `8022c01f46c7` | sun50i-h6.dtsi |
| 78 | `arm64-dts-allwinner-h6-add-AC200-codec-nodes.patch` | arm64: dts: allwinner: h6: add AC200 codec nodes | `4cc61081f497` | sun50i-h6.dtsi |
| 79 | `arm64-dts-allwinner-h6-enable-AC200-codec.patch` | arm64: dts: allwinner: h6: enable AC200 codec | `bf158ec72051` | sun50i-h6-orangepi-3.dts, sun50i-h6-pine-h64.dts (+1) |
| 80 | `arm64-dts-allwinner-h6-tanix-enable-Ethernet.patch` | arm64: dts: allwinner: h6: tanix: enable Ethernet | `7c87d7c71b5d` | sun50i-h6-tanix.dtsi |
| 81 | `arm64-dts-allwinner-h616-orangepi-zero2-Enable-expansion-board-.patch` | arm64: dts: allwinner: h616 orangepi zero2: Enable... | `7e7c50571314` | sun50i-h616-orangepi-zero.dtsi |
| 82 | `arm64-dts-allwinner-overlay-Add-Overlays-for-sunxi64.patch` | arm64:dts:allwinner:overlay: Add Overlays for sunx... | `a5de8971554d` | sun50i-a64-spi-add-cs1.dtso, sun50i-h5-uart2.dtso (+47) |
| 83 | `arm64-dts-allwinner-sun50i-h6-Fix-H6-emmc.patch` | arm64: dts/allwinner/sun50i-h6: Fix H6 emmc | `60aea9df8e7b` | sun50i-h6.dtsi |
| 84 | `arm64-dts-allwinner-sun50i-h616-Add-VPU-node.patch` | arm64:dts:allwinner: sun50i-h616 Add VPU node | `3561685a36bd` | sun50i-h616.dtsi |
| 85 | `arm64-dts-h616-8-Add-overlays-i2c-pwm-uart.patch` | arm64: dts: h616(8): Add overlays i2c, pwm, uart | `a59cb6bd6235` | sun50i-h616-uart4-pi.dtso, sun50i-h616-i2c3-pg.dtso (+23) |
| 86 | `arm64-dts-h616-add-hdmi-support-for-zero2-and-zero3.patch` | arm64: dts: h616: add hdmi support for zero2 and z... | `270e1512a91f` | sun50i-h616.dtsi, sun50i-h616-orangepi-zero.dtsi (+1) |
| 87 | `arm64-dts-h616-add-wifi-support-for-orange-pi-zero-2-and-zero3.patch` | arm64: dts: h616: add wifi support for orange pi z... | `558ee0b5606d` | sun50i-h616-orangepi-zero.dtsi |
| 88 | `arm64-dts-nanopi-a64-set-right-phy-mode-to-rgmii-id.patch` | arm64:dts: nanopi-a64 set right phy-mode to rgmii-... | `000000000000` | sun50i-a64-nanopi-a64.dts |
| 89 | `arm64-dts-overlay-sun50i-a64-pine64-7inch-lcd.patch` | arm64:dts:overlay: sun50i-a64-pine64-7inch-lcd | `4a77c8ac8b0e` | Makefile, README.sun50i-a64-overlays (+1) |
| 90 | `arm64-dts-overlay-sun50i-h5-add-gpio-regulator-overclock.patch` | arm64:dts:overlay sun50i-h5 add gpio regulator ove... | `c5b7968c7a82` | sun50i-h5-cpu-clock-1.0GHz-1.1v.dtso, sun50i-h5-cpu-clock-1.2GHz-1.3v.dtso (+3) |
| 91 | `arm64-dts-sun50i-a64-force-mmc0-bus-width.patch` | arm64:dts: sun50i-a64 force mmc0 bus-width | `85906a7fbd36` | sun50i-a64.dtsi |
| 92 | `arm64-dts-sun50i-a64-olinuxino-1Ge16GW-Disable-clock-phase-and-.patch` | arm64:dts:sun50i-a64-olinuxino-1Ge16GW Disable clo... | `000000000000` | sun50i-a64-olinuxino-1Ge16GW.dts |
| 93 | `arm64-dts-sun50i-a64-olinuxino-1Ge16GW-enable-bluetooth.patch` | arm64:dts: sun50i-a64-olinuxino-1Ge16GW: enable bl... | `000000000000` | sun50i-a64-olinuxino-1Ge16GW.dts |
| 94 | `arm64-dts-sun50i-a64-olinuxino-add-boards.patch` | arm64:dts:sun50i-a64-olinuxino add boards | `b94c32c09b84` | sun50i-a64-olinuxino-1G.dts, Makefile (+4) |
| 95 | `arm64-dts-sun50i-a64-olinuxino-emmc-enable-bluetooth.patch` | arm64:dts: sun50i-a64-olinuxino-emmc: enable bluet... | `000000000000` | sun50i-a64-olinuxino-emmc.dts |
| 96 | `arm64-dts-sun50i-a64-orangepi-win-add-aliase-ethernet1.patch` | arm64:dts: sun50i-a64-orangepi-win add aliase ethe... | `000000000000` | sun50i-a64-orangepi-win.dts |
| 97 | `arm64-dts-sun50i-a64-pine64-add-spi0.patch` | arm64:dts: sun50i-a64-pine64 add spi0 | `ea92626f9272` | sun50i-a64-pine64.dts |
| 98 | `arm64-dts-sun50i-a64-pine64-enable-wifi-mmc1.patch` | arm64:dts: sun50i-a64-pine64 enable wifi mmc1 | `315aba156b72` | sun50i-a64-pine64.dts |
| 99 | `arm64-dts-sun50i-a64-sopine-baseboard-enable-Bluetooth.patch` | arm64:dts: sun50i-a64-sopine-baseboard enable Blue... | `51557cb59db2` | sun50i-a64-sopine-baseboard.dts |
| 100 | `arm64-dts-sun50i-a64-sopine-baseboard-mmc1-status-okay.patch` | arm64:dts: sun50i-a64-sopine-baseboard: mmc1: stat... | `efde7c83c1b9` | sun50i-a64-sopine-baseboard.dts |
| 101 | `arm64-dts-sun50i-a64.dtsi-adjust-thermal-trip-points.patch` | arm64:dts:sun50i-a64.dtsi adjust thermal trip poin... | `000000000000` | sun50i-a64.dtsi |
| 102 | `arm64-dts-sun50i-h313-x96q-lpddr3.patch` | arm64: dts: sun50i-h313-x96q-lpddr3 | `58fa02e703c1` | Makefile, sun50i-h313-x96q-lpddr3.dts (+1) |
| 103 | `arm64-dts-sun50i-h5-add-cpu-opp-refs.patch` | arm64:dts:sun50i-h5 add cpu opp refs | `000000000000` | sun50i-h5-nanopi-neo-core2.dts, sun50i-h5-orangepi-prime.dts (+6) |
| 104 | `arm64-dts-sun50i-h5-add-termal-zones.patch` | arm64:dts:sun50i-h5 add termal zones | `635972bcdd65` | sun50i-h5.dtsi |
| 105 | `arm64-dts-sun50i-h5-enable-power-button-for-orangepi-prime.patch` | arm64: dts: sun50i: h5: enable power button for or... | `000000000000` | sun50i-h5-orangepi-prime.dts |
| 106 | `arm64-dts-sun50i-h5-nanopi-neo2-add-regulator-led-triger.patch` | arm64:dts: sun50i-h5-nanopi-neo2 add regulator, le... | `000000000000` | sun50i-h5-nanopi-neo2.dts |
| 107 | `arm64-dts-sun50i-h5-nanopi-r1s-h5-add-rtl8153-support.patch` | arm64: dts: sun50i-h5-nanopi-r1s-h5: add rtl8153 s... | `000000000000` | sun50i-h5-nanopi-r1s-h5.dts |
| 108 | `arm64-dts-sun50i-h5-orangepi-pc2-add-spi-flash.patch` | arm64:dts: sun50i-h5-orangepi-pc2 add spi flash | `1415de6f0412` | sun50i-h5-orangepi-pc2.dts |
| 109 | `arm64-dts-sun50i-h5-orangepi-prime-add-regulator.patch` | arm64:dts: sun50i-h5-orangepi-prime add regulator | `c53547f45310` | sun50i-h5-orangepi-prime.dts |
| 110 | `arm64-dts-sun50i-h5-orangepi-prime-add-rtl8723cs.patch` | arm64:dts: sun50i-h5-orangepi-prime add rtl8723cs | `8a8d8ca9c2cd` | sun50i-h5-orangepi-prime.dts |
| 111 | `arm64-dts-sun50i-h5-orangepi-zero-plus-add-regulator.patch` | arm64:dts: sun50i-h5-orangepi-zero-plus add regula... | `000000000000` | sun50i-h5-orangepi-zero-plus.dts |
| 112 | `arm64-dts-sun50i-h6-Add-r_uart-uart2-3-pins.patch` | arm64:dts: sun50i-h6 Add r_uart uart2-3 pins | `4b393b56438e` | sun50i-h6.dtsi |
| 113 | `arm64-dts-sun50i-h6-orangepi-3-add-r_uart-aliase.patch` | arm64:dts: sun50i-h6-orangepi-3 add r_uart aliase | `000000000000` | sun50i-h6-orangepi-3.dts |
| 114 | `arm64-dts-sun50i-h6-orangepi-3-delete-node-spi0.patch` | arm64:dts: sun50i-h6-orangepi-3 delete-node &spi0 | `505db041831f` | sun50i-h6-orangepi-3.dts |
| 115 | `arm64-dts-sun50i-h6-orangepi-add-cpu-opp-refs.patch` | arm64:dts: sun50i-h6-orangepi add cpu opp refs | `000000000000` | sun50i-h6-orangepi.dtsi |
| 116 | `arm64-dts-sun50i-h6-orangepi-enable-higher-clock-regulator-max-.patch` | arm64:dts: sun50i-h6-orangepi enable higher clock | `ed7bdf184c5a` | sun50i-h6-orangepi.dtsi |
| 117 | `arm64-dts-sun50i-h6-orangepi-lite2-spi0-usb3phy-dwc3-enable.patch` | arm64:dts: sun50i-h6-orangepi-lite2 spi0, usb3phy,... | `000000000000` | sun50i-h6-orangepi-lite2.dts |
| 118 | `arm64-dts-sun50i-h6-pine-h64-add-dwc3-usb3phy.patch` | arm64:dts: sun50i-h6-pine-h64 add dwc3 usb3phy | `2e09c0cf2afa` | sun50i-h6-pine-h64.dts |
| 119 | `arm64-dts-sun50i-h6-pine-h64-add-wifi-rtl8723cs.patch` | arm64:dts: sun50i-h6-pine-h64 add wifi rtl8723cs | `e4b7f55f57e5` | sun50i-h6-pine-h64.dts |
| 120 | `arm64-dts-sun50i-h6.dtsi-add-pinctrl-pins-for-spi.patch` | arm64:dts: sun50i-h6.dtsi add pinctrl pins for spi | `4edd2fb769ff` | sun50i-h6.dtsi |
| 121 | `arm64-dts-sun50i-h6.dtsi-improve-thermals.patch` | arm64:dts: sun50i-h6.dtsi improve thermals | `6b72eec004a4` | sun50i-h6.dtsi |
| 122 | `arm64-dts-sun50i-h616-add-pwm-nodes-support.patch` | arm64: dts: sun50i-h616: add pwm nodes support | `476ae5840384` | sun50i-h616.dtsi |
| 123 | `arm64-dts-sun50i-h616-bigtreetech-cb1-sd-emmc.patch` | arm64: dts: sun50i-h616-bigtreetech-cb1(sd, emmc) | `a8ee1b34a672` | Makefile, sun50i-h616-bigtreetech-cb1-emmc.dts (+2) |
| 124 | `arm64-dts-sun50i-h616-orangepi-zero2-Enable-GPU-mali.patch` | arm64:dts: sun50i-h616-orangepi-zero2 Enable GPU m... | `32714948ee14` | sun50i-h616-orangepi-zero2.dts |
| 125 | `arm64-dts-sun50i-h616-orangepi-zero2-reg_usb1_vbus-status-ok.patch` | arm64: dts: sun50i-h616-orangepi-zero2: reg_usb1_v... | `000000000000` | sun50i-h616-orangepi-zero.dtsi |
| 126 | `arm64-dts-sun50i-h616-x96-mate-T95-eth-sd-card-hack.patch` | arm64:dts: sun50i-h616-x96-mate T95 eth & sd card ... | `2134cc3eccff` | sun50i-h616-x96-mate.dts, sun50i-h616.dtsi |
| 127 | `arm64-dts-sun50i-h616-x96-mate-add-hdmi.patch` | arm64:dts: sun50i-h616-x96-mate add hdmi | `e48549cc1b24` | sun50i-h616-x96-mate.dts |
| 128 | `arm64-dts-sun50i-h616.dtsi-reserved-memory-512K-for-BL31.patch` | arm64: dts: sun50i-h616.dtsi: reserved memory 512K... | `abf887a3265a` | sun50i-h616.dtsi |
| 129 | `arm64-dts-sun50i-h618-orangepi-zero2w-Add-missing-nodes.patch` | arm64: dts: sun50i-h618-orangepi-zero2w: Add missi... | `83fbd972f2a7` | sun50i-h616.dtsi, sun50i-h618-orangepi-zero2w.dts |
| 130 | `arm64-dts-sun50i-h618-orangepi-zero3-Enable-GPU-mali.patch` | arm64:dts: sun50i-h618-orangepi-zero3 Enable GPU m... | `05fded634606` | sun50i-h618-orangepi-zero3.dts |
| 131 | `arm64-sun50i-h616-Add-i2c-2-3-4-uart-2-5-pins.patch` | arm64: sun50i-h616: Add i2c(2,3,4), uart(2,5) pins | `05e16d776c12` | sun50i-h616.dtsi |
| 132 | `cb1-overlay.patch` | cb1-overlay | `ce1965678125` | sun50i-h616-fixup.scr-cmd, sun50i-h616-spidev1_0.dtso (+10) |
| 133 | `clk-gate-add-support-for-regmap-based-gates.patch` | clk: gate: add support for regmap based gates | `000000000000` | clk-provider.h, clk-gate.c |
| 134 | `driver-allwinner-h618-emac.patch` | driver: allwinner h618 emac | `d182957e3479` | sunxi-gmac.c, ac200.h (+12) |
| 135 | `drivers-devfreq-sun8i-a33-mbus-disable-autorefresh.patch` | drivers: devfreq: sun8i-a33-mbus: disable autorefr... | `000000000000` | sun8i-a33-mbus.c |
| 136 | `drivers-pwm-Add-pwm-sunxi-enhance-driver-for-h616.patch` | drivers: pwm: Add pwm-sunxi-enhance driver for h61... | `78c40257c314` | pwm-sunxi-enhance.c, Makefile (+2) |
| 137 | `drv-clocksource-arm_arch_timer-fix-a64-timejump.patch` | drv:clocksource:arm_arch_timer fix a64 timejump | `000000000000` | arm_arch_timer.c |
| 138 | `drv-gpu-drm-gem-dma-Export-with-handle-allocator.patch` | drv:gpu:drm: gem: dma: Export with handle allocato... | `000000000000` | drm_gem_dma_helper.h, drm_gem_dma_helper.c |
| 139 | `drv-gpu-drm-panel-simple-Add-compability-olinuxino-lcd.patch` | drv:gpu:drm: panel-simple Add compability olinuxin... | `f01c1716f180` | panel-simple.c |
| 140 | `drv-gpu-drm-sun4i-Add-GEM-allocator.patch` | drv:gpu:drm:sun4i: Add GEM allocator | `c4ff09ffb5ec` | sun4i_drm.h, sun4i_drv.c |
| 141 | `drv-gpu-drm-sun4i-Add-HDMI-audio-sun4i-hdmi-encoder.patch` | drv:gpu:drm:sun4i: Add HDMI audio sun4i-hdmi encod... | `c7f9993fb9fa` | Kconfig, sun4i_hdmi.h (+3) |
| 142 | `drv-gpu-drm-sun4i-sun8i_mixer.c-add-h3-mixer1.patch` | drv:gpu:drm:sun4i:sun8i_mixer.c add h3 mixer1 | `eb4ea7b5f644` | sun8i_mixer.c |
| 143 | `drv-iio-adc-axp20x_adc-arm64-dts-axp803-hwmon-enable-thermal.patch` | drv:iio:adc:axp20x_adc arm64:dts:axp803 hwmon enab... | `62c8a5f644fb` | axp803.dtsi, axp20x_adc.c |
| 144 | `drv-input-touchscreen-sun4i-ts-Enable-parsing.patch` | drv:input:touchscreen:sun4i-ts Enable parsing | `000000000000` | sun4i-ts.c |
| 145 | `drv-media-dvb-frontends-si2168-fix-cmd-timeout.patch` | drv:media:dvb-frontends:si2168: fix cmd timeout | `000000000000` | si2168.c |
| 146 | `drv-mfd-axp20x-add-sysfs-interface.patch` | drv:mfd:axp20x add sysfs interface | `2a8a9e3104ce` | axp20x.c |
| 147 | `drv-mmc-host-sunxi-mmc-Disable-DDR52-mode-on-all-A20-based-boar.patch` | drv:mmc:host:sunxi-mmc Disable DDR52 mode on all A... | `000000000000` | sunxi-mmc.c |
| 148 | `drv-mmc-host-sunxi-mmc-add-h5-emmc-compatible.patch` | drv:mmc:host:sunxi-mmc: add h5 emmc compatible | `000000000000` | sunxi-mmc.c |
| 149 | `drv-mtd-nand-raw-nand_ids.c-add-H27UBG8T2BTR-BC-nand.patch` | drv:mtd:nand:raw:nand_ids.c add H27UBG8T2BTR-BC na... | `000000000000` | nand_ids.c |
| 150 | `drv-net-stmmac-dwmac-sun8i-second-EMAC-clock-register.patch` | drv:net:stmmac:dwmac-sun8i: second EMAC clock regi... | `0e86acce2282` | dwmac-sun8i.c |
| 151 | `drv-nvmem-sunxi_sid-Support-SID-on-H616.patch` | drv:nvmem:sunxi_sid: Support SID on H616 | `000000000000` | sunxi_sid.c |
| 152 | `drv-of-Device-Tree-Overlay-ConfigFS-interface.patch` | drv:of: Device Tree Overlay ConfigFS interface | `0bfb8399d8b4` | Makefile, configfs.c (+2) |
| 153 | `drv-phy-sun4i-usb-Allow-reset-line-to-be-shared.patch` | drv:phy: sun4i-usb: Allow reset line to be shared | `711fd07f4f2f` | phy-sun4i-usb.c |
| 154 | `drv-pinctrl-pinctrl-sun50i-a64-disable_strict_mode.patch` | drv:pinctrl: pinctrl-sun50i-a64 disable_strict_mod... | `000000000000` | pinctrl-sun50i-a64.c |
| 155 | `drv-pinctrl-sunxi-pinctrl-sun50i-h6.c-GPIO-disable_strict_mode.patch` | drv:pinctrl:sunxi:pinctrl-sun50i-h6.c GPIO disable... | `000000000000` | pinctrl-sun50i-h6.c |
| 156 | `drv-soc-sunxi-sram-Add-SRAM-C1-H616-handling.patch` | drv:soc: sunxi: sram: Add SRAM C1 H616 handling | `000000000000` | sunxi_sram.c |
| 157 | `drv-spi-spi-sun4i.c-spi-bug-low-on-sck.patch` | drv:spi:spi-sun4i.c spi bug low on sck | `f45c4632c0d5` | spi-sun4i.c |
| 158 | `drv-spi-spidev-Add-armbian-spi-dev-compatible.patch` | drv:spi:spidev Add armbian spi-dev compatible | `36b50c879cbe` | spidev.c |
| 159 | `drv-staging-media-sunxi-cedrus-add-H616-variant.patch` | drv:staging:media:sunxi:cedrus: add H616 variant | `bb7878b3cdbe` | cedrus.c |
| 160 | `drv-staging-rtl8723bs-AP-bugfix.patch` | drv:staging:rtl8723bs: AP bugfix | `426ff5c4a9a4` | ioctl_cfg80211.c |
| 161 | `drv-usb-gadget-composite-rename-gadget-serial-console-manufactu.patch` | drv:usb:gadget:composite rename gadget serial cons... | `18640635e385` | composite.c |
| 162 | `enable-TV-Output-on-OrangePi-Zero-LTE.patch` | enable TV Output on OrangePi Zero LTE | `401cf6db854d` | sunxi-h3-h5.dtsi, Makefile (+14) |
| 163 | `fix-cpu-opp-table-sun8i-a83t.patch` | fix: cpu opp table sun8i-a83t | `000000000000` | sun8i-a83t.dtsi |
| 164 | `h616-add-keys.patch` | h616: add keys | `b0d0e0e7cbe9` | sun4i-lradc-keys.c, Makefile (+2) |
| 165 | `include-uapi-drm_fourcc-add-ARM-tiled-format-modifier.patch` | include:uapi:drm_fourcc: add ARM tiled format modi... | `3f384c786fde` | drm_fourcc.h |
| 166 | `mfd-Add-support-for-X-Powers-AC200-EPHY-syscon.patch` | mfd: Add support for X-Powers AC200 EPHY syscon | `95a8f4f5c784` | Kconfig, ac200-ephy-ctl.c (+1) |
| 167 | `mfd-Add-support-for-X-Powers-AC200.patch` | mfd: Add support for X-Powers AC200 | `77b6d5f86a69` | Makefile, ac200.c (+1) |
| 168 | `mmc-host-sunxi-mmc-Fix-H6-emmc.patch` | mmc/host/sunxi-mmc: Fix H6 emmc | `000000000000` | sunxi-mmc.c |
| 169 | `net-phy-Add-support-for-AC200-EPHY.patch` | net: phy: Add support for AC200 EPHY | `d411012cf317` | Makefile, Kconfig (+1) |
| 170 | `net-usb-r8152-add-LED-configuration-from-OF.patch` | net: usb: r8152: add LED configuration from OF | `5f76b8851beb` | r8152.c |
| 171 | `nvmem-sunxi_sid-add-sunxi_get_soc_chipid-sunxi_get_serial.patch` | nvmem: sunxi_sid: add sunxi_get_soc_chipid, sunxi_... | `000000000000` | sunxi_sid.c |
| 172 | `scripts-add-overlay-compilation-support.patch` | scripts: add overlay compilation support | `ca92cb0984d0` | Makefile.dtbs, Makefile.dtbinst (+1) |
| 173 | `sound-soc-sunxi-Provoke-the-early-load-of-sun8i-codec-analog.patch` | sound:soc:sunxi: Provoke the early load of sun8i-c... | `000000000000` | Makefile |
| 174 | `sound-soc-sunxi-sun4i-codec-adcis-select-capture-source.patch` | sound:soc:sunxi:sun4i-codec adcis select capture s... | `d15c10166033` | sun4i-codec.c |
| 175 | `sound-soc-sunxi-sun8i-codec-analog-enable-sound.patch` | sound:soc:sunxi:sun8i-codec-analog enable sound | `000000000000` | sun8i-codec-analog.c |
| 176 | `sun50i-h616-Add-the-missing-digital-audio-node.patch` | sun50i-h616: Add the missing digital audio node | `9a7f38264bbc` | sun50i-h616.dtsi, sun50i-h618-bananapi-m4-berry.dts |

### patches.drm (26 patches)

| # | Patch File | Subject | Commit ID | Files Changed |
|---|------------|---------|-----------|---------------|
| 1 | `drm-sun4i-Report-page-flip-after-vsync-is-complete-not-in-the-m.patch` | drm: sun4i: Report page flip after vsync is comple... | `c14e5e16fb3e` | sun4i_tcon.c, sun4i_tcon.h |
| 2 | `drm-sun4i-add-sun50i-h616-hdmi-phy-support.patch` | drm: sun4i: add sun50i-h616-hdmi-phy support | `6c8bbaf43b8e` | sun8i_hdmi_phy.c |
| 3 | `drm-sun4i-de2-Initialize-layer-fields-earlier.patch` | drm: sun4i: de2: Initialize layer fields earlier | `5c2859b3cccd` | sun8i_ui_layer.c, sun8i_vi_layer.c |
| 4 | `drm-sun4i-de2-de3-Change-CSC-argument.patch` | drm: sun4i: de2/de3: Change CSC argument | `54669ac67e47` | sun8i_csc.c, sun8i_vi_layer.c (+1) |
| 5 | `drm-sun4i-de2-de3-Merge-CSC-functions-into-one.patch` | drm: sun4i: de2/de3: Merge CSC functions into one | `09744193cdcf` | sun8i_csc.c, sun8i_vi_layer.c (+1) |
| 6 | `drm-sun4i-de2-de3-add-generic-blender-register-reference-functi.patch` | drm: sun4i: de2/de3: add generic blender register ... | `7e2082f55e65` | sun8i_mixer.h |
| 7 | `drm-sun4i-de2-de3-add-mixer-version-enum.patch` | drm: sun4i: de2/de3: add mixer version enum | `90f292bafa6d` | sun8i_vi_scaler.c, sun8i_vi_layer.c (+4) |
| 8 | `drm-sun4i-de2-de3-call-csc-setup-also-for-UI-layer.patch` | drm: sun4i: de2/de3: call csc setup also for UI la... | `000c586a34ad` | sun8i_ui_layer.c, sun8i_csc.c |
| 9 | `drm-sun4i-de2-de3-refactor-mixer-initialisation.patch` | drm: sun4i: de2/de3: refactor mixer initialisation | `4042b1c4ed4e` | sun8i_mixer.c |
| 10 | `drm-sun4i-de2-de3-use-generic-register-reference-function-for-l.patch` | drm: sun4i: de2/de3: use generic register referenc... | `91877bc54df8` | sun8i_ui_layer.c, sun8i_mixer.c (+1) |
| 11 | `drm-sun4i-de3-Add-YUV-formatter-module.patch` | drm: sun4i: de3: Add YUV formatter module | `8bdcc131fedb` | Makefile, sun50i_fmt.c (+1) |
| 12 | `drm-sun4i-de3-Implement-AFBC-support.patch` | drm: sun4i: de3: Implement AFBC support | `0788787d1240` | Makefile, sun50i_afbc.h (+2) |
| 13 | `drm-sun4i-de3-add-YUV-support-to-the-DE3-mixer.patch` | drm: sun4i: de3: add YUV support to the DE3 mixer | `681152c96fe0` | sunxi_engine.h, sun8i_mixer.c |
| 14 | `drm-sun4i-de3-add-YUV-support-to-the-TCON.patch` | drm: sun4i: de3: add YUV support to the TCON | `1000fdf61f22` | sun4i_tcon.c |
| 15 | `drm-sun4i-de3-add-YUV-support-to-the-color-space-correction-mod.patch` | drm: sun4i: de3: add YUV support to the color spac... | `a23ed976ee72` | sun8i_csc.c |
| 16 | `drm-sun4i-de3-add-format-enumeration-function-to-engine.patch` | drm: sun4i: de3: add format enumeration function t... | `99d327853acb` | sunxi_engine.h |
| 17 | `drm-sun4i-de3-add-formatter-flag-to-mixer-config.patch` | drm: sun4i: de3: add formatter flag to mixer confi... | `56afb6bff57f` | sun8i_mixer.c, sun8i_mixer.h |
| 18 | `drm-sun4i-de3-pass-engine-reference-to-ccsc-setup-function.patch` | drm: sun4i: de3: pass engine reference to ccsc set... | `2d7c88fc2af6` | sun8i_csc.c |
| 19 | `drm-sun4i-de33-csc-add-Display-Engine-3.3-DE33-support.patch` | drm: sun4i: de33: csc: add Display Engine 3.3 (DE3... | `0d003a88bcac` | sun8i_csc.c, sun8i_csc.h |
| 20 | `drm-sun4i-de33-fmt-add-Display-Engine-3.3-DE33-support.patch` | drm: sun4i: de33: fmt: add Display Engine 3.3 (DE3... | `792b816c952b` | sun50i_fmt.c, sun50i_fmt.h |
| 21 | `drm-sun4i-de33-mixer-add-Display-Engine-3.3-DE33-support.patch` | drm: sun4i: de33: mixer: add Display Engine 3.3 (D... | `bbbfdc8bc71a` | sun8i_mixer.c, sun8i_mixer.h |
| 22 | `drm-sun4i-de33-vi_scaler-add-Display-Engine-3.3-DE33-support.patch` | drm: sun4i: de33: vi_scaler: add Display Engine 3.... | `412294545ec9` | sun8i_ui_layer.c, sun8i_vi_scaler.c |
| 23 | `drm-sun4i-support-YUV-formats-in-VI-scaler.patch` | drm: sun4i: support YUV formats in VI scaler | `e0de25f60a35` | sun8i_vi_scaler.c |
| 24 | `drm-sun4i-vi_scaler-refactor-vi_scaler-enablement.patch` | drm: sun4i: vi_scaler refactor vi_scaler enablemen... | `0c10a80b8e37` | sun8i_vi_scaler.h, sun8i_vi_scaler.c (+1) |
| 25 | `dt-bindings-allwinner-add-H616-DE33-bus-binding.patch` | dt-bindings: allwinner: add H616 DE33 bus binding | `b8344d8eb9d0` | allwinner,sun50i-a64-de2.yaml |
| 26 | `dt-bindings-allwinner-add-H616-DE33-mixer-binding.patch` | dt-bindings: allwinner: add H616 DE33 mixer bindin... | `12d7983166ed` | allwinner,sun8i-a83t-de2-mixer.yaml |

### patches.media (6 patches)

| # | Patch File | Subject | Commit ID | Files Changed |
|---|------------|---------|-----------|---------------|
| 1 | `dma-sun6i-dma-add-sun50i-h616-support.patch` | dma: sun6i-dma: add sun50i-h616 support | `672717a70d3f` | sun6i-dma.c |
| 2 | `media-Add-NV12-and-P010-AFBC-compressed-formats.patch` | media: Add NV12 and P010 AFBC compressed formats | `e43c6b985ac6` | videodev2.h, v4l2-ioctl.c |
| 3 | `media-cedrus-Don-t-CPU-map-source-buffers.patch` | media: cedrus: Don't CPU map source buffers | `80b16fcddf18` | cedrus_video.c |
| 4 | `media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch` | media: cedrus: Implement AFBC YUV420 formats for H... | `81241983ba12` | cedrus_regs.h, cedrus_hw.c (+3) |
| 5 | `media-cedrus-Increase-H6-clock-rate.patch` | media: cedrus: Increase H6 clock rate | `c0dffc32c3a6` | cedrus.c |
| 6 | `media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch` | media: cedrus: add format filtering based on depth... | `be75f442cae7` | cedrus_video.h, cedrus_video.c |

### patches.megous (236 patches)

| # | Patch File | Subject | Commit ID | Files Changed |
|---|------------|---------|-----------|---------------|
| 1 | `2-arm64-dts-sun50i-Define-orientation-and-rotation-for-PinePhone-.patch` | arm64: dts: sun50i: Define orientation and rotatio... | `babd7ba10901` | sun50i-a64-pinephone.dtsi |
| 2 | `ARM-dts-axp813-Add-charger-LED.patch` | ARM: dts: axp813: Add charger LED | `3b1f07be7287` | axp81x.dtsi |
| 3 | `ARM-dts-sun5i-Add-PocketBook-Touch-Lux-3-display-ctp-support.patch` | ARM: dts: sun5i: Add PocketBook Touch Lux 3 displa... | `65ab846a1fed` | sun5i-a13-pocketbook-touch-lux-3.dts |
| 4 | `ARM-dts-sun5i-Add-soc-handle.patch` | ARM: dts: sun5i: Add soc handle | `c23b72ad5a48` | sun5i.dtsi |
| 5 | `ARM-dts-sun5i-a13-pocketbook-touch-lux-3-Add-RTC-clock-cells.patch` | ARM: dts: sun5i-a13-pocketbook-touch-lux-3: Add RT... | `3204bd45b054` | sun5i-a13-pocketbook-touch-lux-3.dts |
| 6 | `ARM-dts-sun8i-a83t-Add-MBUS-node.patch` | ARM: dts: sun8i: a83t: Add MBUS node | `7c46723de140` | sun8i-a83t.dtsi |
| 7 | `ARM-dts-sun8i-a83t-Add-cedrus-video-codec-support-to-A83T-untes.patch` | ARM: dts: sun8i-a83t: Add cedrus video codec suppo... | `dbfa68bb8bff` | sun8i-a83t.dtsi |
| 8 | `ARM-dts-sun8i-a83t-Add-hdmi-sound-card.patch` | ARM: dts: sun8i: a83t: Add hdmi sound card | `4e1ffe039332` | sun8i-a83t.dtsi |
| 9 | `ARM-dts-sun8i-a83t-Add-missing-GPU-trip-point.patch` | ARM: dts: sun8i-a83t: Add missing GPU trip point | `455e56be4e20` | sun8i-a83t.dtsi |
| 10 | `ARM-dts-sun8i-a83t-Enable-hdmi-sound-card-on-boards-with-hdmi.patch` | ARM: dts: sun8i: a83t: Enable hdmi sound card on b... | `ea78de6c4aab` | sun8i-a83t-bananapi-m3.dts, sun8i-a83t-cubietruck-plus.dts |
| 11 | `ARM-dts-sun8i-a83t-Improve-CPU-OPP-tables-go-up-to-1.8GHz.patch` | ARM: dts: sun8i-a83t: Improve CPU OPP tables (go u... | `75d25c0f8096` | sun8i-a83t.dtsi |
| 12 | `ARM-dts-sun8i-a83t-Set-fifo-size-for-uarts.patch` | ARM: dts: sun8i-a83t: Set fifo-size for uarts | `407da3bb8788` | sun8i-a83t.dtsi |
| 13 | `ARM-dts-sun8i-a83t-tbs-a711-Add-PN544-NFC-support.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add PN544 NFC suppo... | `8c597603a316` | sun8i-a83t-tbs-a711.dts |
| 14 | `ARM-dts-sun8i-a83t-tbs-a711-Add-camera-sensors-HM5065-GC2145.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add camera sensors ... | `b4f121b88340` | sun8i-a83t-tbs-a711.dts |
| 15 | `ARM-dts-sun8i-a83t-tbs-a711-Add-flash-led-support.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add flash led suppo... | `019b5fe6a62f` | sun8i-a83t-tbs-a711.dts |
| 16 | `ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add powerup/down su... | `5b1f89dbd335` | sun8i-a83t-tbs-a711.dts |
| 17 | `ARM-dts-sun8i-a83t-tbs-a711-Add-regulators-to-the-accelerometer.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add regulators to t... | `d3aafc0e82f0` | sun8i-a83t-tbs-a711.dts |
| 18 | `ARM-dts-sun8i-a83t-tbs-a711-Add-sound-support-via-AC100-codec.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add sound support v... | `28d9bff7bbc1` | sun8i-a83t-tbs-a711.dts |
| 19 | `ARM-dts-sun8i-a83t-tbs-a711-Add-support-for-the-vibrator-motor.patch` | ARM: dts: sun8i-a83t-tbs-a711: Add support for the... | `bc4e7ff402a8` | sun8i-a83t-tbs-a711.dts |
| 20 | `ARM-dts-sun8i-a83t-tbs-a711-Enable-charging-LED.patch` | ARM: dts: sun8i-a83t-tbs-a711: Enable charging LED | `0395da54b819` | sun8i-a83t-tbs-a711.dts |
| 21 | `ARM-dts-sun8i-a83t-tbs-a711-Give-Linux-more-privileges-over-SCP.patch` | ARM: dts: sun8i-a83t-tbs-a711: Give Linux more pri... | `059050249c1d` | sun8i-a83t.dtsi |
| 22 | `ARM-dts-sun8i-a83t-tbs-a711-Increase-voltage-on-the-vibrator.patch` | ARM: dts: sun8i-a83t-tbs-a711: Increase voltage on... | `0676a665a91d` | sun8i-a83t-tbs-a711.dts |
| 23 | `ARM-dts-sun8i-h2-plus-bananapi-m2-zero-Enable-HDMI-audio.patch` | ARM: dts: sun8i: h2-plus: bananapi-m2-zero: Enable... | `9ed682abf8c8` | sun8i-h2-plus-bananapi-m2-zero.dts |
| 24 | `ARM-dts-sun8i-h3-Enable-hdmi-sound-card-on-boards-with-hdmi.patch` | ARM: dts: sun8i: h3: Enable hdmi sound card on boa... | `5323f01be1bd` | sun8i-h3-orangepi-lite.dts, sun8i-h3-emlid-neutis-n5h3-devboard.dts (+8) |
| 25 | `ARM-dts-sun8i-h3-Use-my-own-more-aggressive-OPPs-on-H3.patch` | ARM: dts: sun8i-h3: Use my own more aggressive OPP... | `cb05a11519a6` | sun8i-h3.dtsi |
| 26 | `ARM-dts-sun8i-h3-orange-pi-one-Enable-all-gpio-header-UARTs.patch` | ARM: dts: sun8i-h3-orange-pi-one: Enable all gpio ... | `251198af980d` | sun8i-h3-orangepi-one.dts |
| 27 | `ARM-dts-sun8i-h3-orange-pi-pc-Increase-max-CPUX-voltage-to-1.4V.patch` | ARM: dts: sun8i-h3-orange-pi-pc: Increase max CPUX... | `64f543a20114` | sun8i-h3-orangepi-pc.dts |
| 28 | `ARM-dts-sun8i-r40-Add-hdmi-sound-card.patch` | ARM: dts: sun8i: r40: Add hdmi sound card | `f72b5462f634` | sun8i-r40.dtsi |
| 29 | `ARM-dts-sun8i-r40-bananapi-m2-ultra-Enable-HDMI-audio.patch` | ARM: dts: sun8i: r40: bananapi-m2-ultra: Enable HD... | `42a96825b819` | sun8i-r40-bananapi-m2-ultra.dts |
| 30 | `ARM-dts-sun8i-v40-bananapi-m2-berry-Enable-HDMI-audio.patch` | ARM: dts: sun8i: v40: bananapi-m2-berry: Enable HD... | `f7ebb1938b69` | sun8i-v40-bananapi-m2-berry.dts |
| 31 | `ARM-dts-suni-a83t-Add-i2s0-pins.patch` | ARM: dts: suni-a83t: Add i2s0 pins | `d19697dd4b59` | sun8i-a83t.dtsi |
| 32 | `ARM-dts-sunxi-Add-aliases-for-MMC.patch` | ARM: dts: sunxi: Add aliases for MMC | `3e83ea68d7e6` | sun8i-h3.dtsi, sun8i-a83t.dtsi (+1) |
| 33 | `ARM-dts-sunxi-a83t-Add-SCPI-protocol.patch` | ARM: dts: sunxi: a83t: Add SCPI protocol | `ae4167d13fa1` | sun8i-a83t.dtsi |
| 34 | `ARM-dts-sunxi-h3-h5-Add-SCPI-protocol.patch` | ARM: dts: sunxi: h3/h5: Add SCPI protocol | `bb0153162714` | sunxi-h3-h5.dtsi, sun8i-h3.dtsi (+1) |
| 35 | `ARM-dts-sunxi-h3-h5-Add-hdmi-sound-card.patch` | ARM: dts: sunxi: h3/h5: Add hdmi sound card | `52961661dcef` | sunxi-h3-h5.dtsi |
| 36 | `ARM-sunxi-Add-experimental-suspend-to-memory-implementation-for.patch` | ARM: sunxi: Add experimental suspend to memory imp... | `44ed294ee215` | sunxi.c |
| 37 | `ARM-sunxi-Use-SCPI-to-send-suspend-message-to-SCP-on-A83T.patch` | ARM: sunxi: Use SCPI to send suspend message to SC... | `368c89a83102` | sunxi.c |
| 38 | `ARM-sunxi-sunxi_cpu0_hotplug_support_set-is-not-supported-on-A8.patch` | ARM: sunxi: sunxi_cpu0_hotplug_support_set is not ... | `ff4d244c254a` | mc_smp.c |
| 39 | `ASOC-sun9i-hdmi-audio-Initial-implementation.patch` | ASOC: sun9i-hdmi-audio: Initial implementation | `1ab2cc80d4c0` | Makefile, Kconfig (+1) |
| 40 | `ASoC-ec25-New-codec-driver-for-the-EC25-modem.patch` | ASoC: ec25: New codec driver for the EC25 modem | `82745a579de2` | ec25.c, Makefile (+1) |
| 41 | `ASoC-simple-card-Allow-to-define-pins-for-aux-jack-devices.patch` | ASoC: simple-card: Allow to define pins for aux ja... | `8977f7a800ae` | simple-card-utils.c |
| 42 | `ASoC-sun8i-codec-Add-debug-output-for-jack-detection.patch` | ASoC: sun8i-codec: Add debug output for jack detec... | `ed4d0a091a27` | sun8i-codec.c |
| 43 | `ASoC-sun8i-codec-Allow-the-jack-type-to-be-set-via-device-tree.patch` | ASoC: sun8i-codec: Allow the jack type to be set v... | `ac76eb562601` | sun8i-codec.c |
| 44 | `ASoC-sun8i-codec-Set-jack_type-from-DT-in-probe.patch` | ASoC: sun8i-codec: Set jack_type from DT in probe | `282f0e41b191` | sun8i-codec.c |
| 45 | `ASoC-sun8i-codec-define-button-keycodes.patch` | ASoC: sun8i-codec: define button keycodes | `4034f4e90fe6` | sun8i-codec.c |
| 46 | `Add-support-for-my-private-Sapomat-device.patch` | Add support for my private Sapomat device | `7bd8ad9c9778` | sun8i-h3-orangepi-pc-sapomat.dts, Makefile |
| 47 | `Defconfigs-for-all-my-devices.patch` | Defconfigs for all my devices | `29fe01c39d6c` | tbs_a711_defconfig, orangepi_defconfig (+4) |
| 48 | `Fix-broken-allwinner-sram-dependency-on-h616-h618.patch` | Fix broken allwinner,sram dependency on h616, h618 | `e8b24e85296e` | property.c |
| 49 | `Fix-intptr_t-typedef.patch` | Fix intptr_t typedef | `5d46a9e55357` | types.h |
| 50 | `MAINTAINERS-Add-entry-for-Himax-HM5065.patch` | MAINTAINERS: Add entry for Himax HM5065 | `2ce741f43a65` | MAINTAINERS |
| 51 | `Make-microbuttons-on-Orange-Pi-PC-and-PC-2-work-as-power-off-bu.patch` | Make microbuttons on Orange Pi PC and PC 2 work as... | `325a2fb637ea` | sun8i-h3-orangepi-one.dts, sun50i-h5-orangepi-pc2.dts |
| 52 | `Mark-some-slow-drivers-for-async-probe-with-PROBE_PREFER_ASYNCH.patch` | Mark some slow drivers for async probe with PROBE_... | `3f375e427480` | i2c.c, bma180.c |
| 53 | `Move-a-node-to-avoid-merge-conflict.patch` | Move a node to avoid merge conflict | `c3623224b8c0` | sunxi-h3-h5.dtsi, sun50i-h6-orangepi-3.dts (+1) |
| 54 | `Revert-ASoC-soc-core-merge-snd_soc_unregister_component-and-snd.patch` | Revert "ASoC: soc-core: merge snd_soc_unregister_c... | `fdf9a3133610` | soc.h, soc-core.c |
| 55 | `Revert-Input-cyttsp4-remove-driver.patch` | Revert "Input: cyttsp4 - remove driver" | `5fa9f90b1e13` | cyttsp4_i2c.c, cyttsp_i2c_common.c (+8) |
| 56 | `Revert-drm-sun4i-lvds-Invert-the-LVDS-polarity.patch` | Revert "drm/sun4i: lvds: Invert the LVDS polarity" | `49999c3dbebc` | sun4i_tcon.c |
| 57 | `Revert-usb-dwc3-Abort-suspend-on-soft-disconnect-failure.patch` | Revert "usb: dwc3: Abort suspend on soft disconnec... | `bfaf13fd6940` | gadget.c, core.c |
| 58 | `Revert-usb-typec-tcpm-unregister-existing-source-caps-before-re.patch` | Revert "usb: typec: tcpm: unregister existing sour... | `18df5a34038c` | tcpm.c |
| 59 | `arm64-allwinner-dts-a64-enable-K101-IM2BYL02-panel-for-PineTab.patch` | arm64: allwinner: dts: a64: enable K101-IM2BYL02 p... | `c0add6f072c4` | sun50i-a64-pinetab.dts |
| 60 | `arm64-dts-allwinner-Enforce-consistent-MMC-numbering.patch` | arm64: dts: allwinner: Enforce consistent MMC numb... | `0a4a41fa8ade` | sun50i-h6.dtsi, sun50i-a64.dtsi (+1) |
| 61 | `arm64-dts-allwinner-a64-Add-hdmi-sound-card.patch` | arm64: dts: allwinner: a64: Add hdmi sound card | `cb90c0e2677a` | sun50i-a64.dtsi |
| 62 | `arm64-dts-allwinner-a64-Enable-hdmi-sound-card-on-boards-with-h.patch` | arm64: dts: allwinner: a64: Enable hdmi sound card... | `46db097304f6` | sun50i-a64-teres-i.dts, sun50i-a64-pine64.dts (+5) |
| 63 | `arm64-dts-allwinner-a64-Fix-LRADC-compatible.patch` | arm64: dts: allwinner: a64: Fix LRADC compatible | `6ccacf9c0f11` | sun50i-a64.dtsi |
| 64 | `arm64-dts-allwinner-a64-pinetab-add-front-camera.patch` | arm64: dts: allwinner: a64: pinetab: add front cam... | `bfbed3e69267` | sun50i-a64-pinetab.dts |
| 65 | `arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch` | arm64: dts: allwinner: h5: Enable hdmi sound card ... | `cf056f9d1d53` | sun50i-h5-emlid-neutis-n5-devboard.dts, sun50i-h5-orangepi-zero-plus2.dts (+2) |
| 66 | `arm64-dts-allwinner-h6-Add-hdmi-sound-card.patch` | arm64: dts: allwinner: h6: Add hdmi sound card | `82458044eed7` | sun50i-h6.dtsi |
| 67 | `arm64-dts-allwinner-h6-Enable-hdmi-sound-card-on-boards-with-hd.patch` | arm64: dts: allwinner: h6: Enable hdmi sound card ... | `ff19a25fd2ae` | sun50i-h6-orangepi-3.dts, sun50i-h6-pine-h64.dts (+2) |
| 68 | `arm64-dts-allwinner-orange-pi-3-Enable-ethernet.patch` | arm64: dts: allwinner: orange-pi-3: Enable etherne... | `da6176323404` | sun50i-h6-orangepi-3.dts |
| 69 | `arm64-dts-rk3399-Add-dmc_opp_table.patch` | arm64: dts: rk3399: Add dmc_opp_table | `7ff04b0bdae8` | rk3399.dtsi |
| 70 | `arm64-dts-sun50-a64-pinephone-Define-jack-pins-in-DT.patch` | arm64: dts: sun50-a64-pinephone: Define jack pins ... | `a5b7326c8575` | sun50i-a64-pinephone.dtsi |
| 71 | `arm64-dts-sun50i-Define-orientation-and-rotation-for-PinePhone-.patch` | arm64: dts: sun50i: Define orientation and rotatio... | `9159b591ce22` | sun50i-a64-pinephone.dtsi |
| 72 | `arm64-dts-sun50i-a64-Set-fifo-size-for-uarts.patch` | arm64: dts: sun50i-a64: Set fifo-size for uarts | `538b7bed8233` | sun50i-a64.dtsi |
| 73 | `arm64-dts-sun50i-a64-pinephone-Add-Type-C-support-for-all-PP-va.patch` | arm64: dts: sun50i-a64-pinephone: Add Type-C suppo... | `82c1ef311dfa` | sun50i-a64-pinephone-1.1.dts, sun50i-a64-pinephone-1.0.dts (+2) |
| 74 | `arm64-dts-sun50i-a64-pinephone-Add-detailed-OCV-to-capactiy-con.patch` | arm64: dts: sun50i-a64-pinephone: Add detailed OCV... | `15ef8921384b` | sun50i-a64-pinephone.dtsi |
| 75 | `arm64-dts-sun50i-a64-pinephone-Add-front-back-cameras.patch` | arm64: dts: sun50i-a64-pinephone: Add front/back c... | `a9b433c7c17a` | sun50i-a64-pinephone.dtsi |
| 76 | `arm64-dts-sun50i-a64-pinephone-Add-interrupt-pin-for-WiFi.patch` | arm64: dts: sun50i-a64-pinephone: Add interrupt pi... | `e0c585577e06` | sun50i-a64-pinephone.dtsi |
| 77 | `arm64-dts-sun50i-a64-pinephone-Add-modem-power-manager.patch` | arm64: dts: sun50i-a64-pinephone: Add modem power ... | `a02549f60d91` | sun50i-a64-pinephone-1.1.dts, sun50i-a64-pinephone-1.0.dts (+1) |
| 78 | `arm64-dts-sun50i-a64-pinephone-Add-power-supply-to-stk3311.patch` | arm64: dts: sun50i-a64-pinephone: Add power supply... | `4b1c8532a7fb` | sun50i-a64-pinephone.dtsi |
| 79 | `arm64-dts-sun50i-a64-pinephone-Add-reboot-mode-driver.patch` | arm64: dts: sun50i-a64-pinephone: Add reboot mode ... | `308f56b99b31` | sun50i-a64-pinephone.dtsi |
| 80 | `arm64-dts-sun50i-a64-pinephone-Add-supply-for-i2c-bus-to-anx768.patch` | arm64: dts: sun50i-a64-pinephone: Add supply for i... | `360891b201c9` | sun50i-a64-pinephone-1.1.dts, sun50i-a64-pinephone-1.0.dts (+1) |
| 81 | `arm64-dts-sun50i-a64-pinephone-Add-support-for-Bluetooth-audio.patch` | arm64: dts: sun50i-a64-pinephone: Add support for ... | `f16fd80bf929` | sun50i-a64-pinephone.dtsi |
| 82 | `arm64-dts-sun50i-a64-pinephone-Add-support-for-Pinephone-1.2-be.patch` | arm64: dts: sun50i-a64-pinephone: Add support for ... | `3abf71beb765` | Makefile, sun50i-a64-pinephone-1.2b.dts |
| 83 | `arm64-dts-sun50i-a64-pinephone-Add-support-for-Pinephone-keyboa.patch` | arm64: dts: sun50i-a64-pinephone: Add support for ... | `1df14f80a223` | sun50i-a64-pinephone.dtsi |
| 84 | `arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch` | arm64: dts: sun50i-a64-pinephone: Add support for ... | `d33975afbcf4` | sun50i-a64-pinephone.dtsi |
| 85 | `arm64-dts-sun50i-a64-pinephone-Bump-I2C-frequency-to-400kHz.patch` | arm64: dts: sun50i-a64-pinephone: Bump I2C frequen... | `a1398167dbe8` | sun50i-a64-pinephone.dtsi |
| 86 | `arm64-dts-sun50i-a64-pinephone-Don-t-make-lradc-keys-a-wakeup-s.patch` | arm64: dts: sun50i-a64-pinephone: Don't make lradc... | `a987a03decda` | sun50i-a64-pinephone.dtsi |
| 87 | `arm64-dts-sun50i-a64-pinephone-Enable-Pinephone-Keyboard-power-.patch` | arm64: dts: sun50i-a64-pinephone: Enable Pinephone... | `058f37ec6205` | sun50i-a64-pinephone.dtsi |
| 88 | `arm64-dts-sun50i-a64-pinephone-Enable-internal-HMIC-bias.patch` | arm64: dts: sun50i-a64-pinephone: Enable internal ... | `dcdcb612a1bb` | sun50i-a64-pinephone-1.0.dts |
| 89 | `arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch` | arm64: dts: sun50i-a64-pinephone: Fix BH modem man... | `6945687a57df` | sun50i-a64-pinephone-1.1.dts |
| 90 | `arm64-dts-sun50i-a64-pinephone-Power-off-the-touch-controller-i.patch` | arm64: dts: sun50i-a64-pinephone: Power off the to... | `97a405169544` | sun50i-a64-pinephone.dtsi |
| 91 | `arm64-dts-sun50i-a64-pinephone-Set-minimum-backlight-duty-cycle.patch` | arm64: dts: sun50i-a64-pinephone: Set minimum back... | `5fb3c2c424a0` | sun50i-a64-pinephone-1.1.dts, sun50i-a64-pinephone-1.2.dts |
| 92 | `arm64-dts-sun50i-a64-pinephone-Shorten-post-power-on-delay-on-m.patch` | arm64: dts: sun50i-a64-pinephone: Shorten post-pow... | `b241ef1dff82` | sun50i-a64-pinephone.dtsi |
| 93 | `arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch` | arm64: dts: sun50i-a64-pinephone: Use newer jack d... | `f1a9b4f7e3a4` | sun50i-a64-pinephone.dtsi |
| 94 | `arm64-dts-sun50i-a64-pinephone-Workaround-broken-HDMI-HPD-signa.patch` | arm64: dts: sun50i-a64-pinephone: Workaround broke... | `472d4b36112e` | sun50i-a64-pinephone-1.1.dts, sun50i-a64-pinephone-1.0.dts (+1) |
| 95 | `arm64-dts-sun50i-a64-pinetab-Add-accelerometer.patch` | arm64: dts: sun50i-a64-pinetab: Add accelerometer | `c3ebe28518e3` | sun50i-a64-pinetab.dts |
| 96 | `arm64-dts-sun50i-a64-pinetab-Name-sound-card-PineTab.patch` | arm64: dts: sun50i-a64-pinetab: Name sound card Pi... | `3fb6768c3303` | sun50i-a64-pinetab.dts |
| 97 | `arm64-dts-sun50i-a64-pinetab-enable-RTL8723CS-bluetooth.patch` | arm64: dts: sun50i-a64-pinetab: enable RTL8723CS b... | `3b4036339ed5` | sun50i-a64-pinetab.dts |
| 98 | `arm64-dts-sun50i-h5-Add-missing-GPU-trip-point.patch` | arm64: dts: sun50i-h5: Add missing GPU trip point | `9ecccf77a9e6` | sun50i-h5.dtsi |
| 99 | `arm64-dts-sun50i-h5-Use-my-own-more-aggressive-OPPs-on-H5.patch` | arm64: dts: sun50i-h5: Use my own more aggressive ... | `d3a05ab72807` | sun50i-h5-cpu-opp.dtsi |
| 100 | `arm64-xor-Select-32regs-without-benchmark-to-speed-up-boot.patch` | arm64: xor: Select 32regs without benchmark to spe... | `89163782655e` | xor.h |
| 101 | `bluetooth-bcm-Restore-drive_rts_on_open-true-behavior-on-bcm207.patch` | bluetooth: bcm: Restore drive_rts_on_open = true b... | `2301fedd353a` | hci_bcm.c |
| 102 | `bluetooth-h5-Don-t-re-initialize-rtl8723cs-on-resume.patch` | bluetooth: h5: Don't re-initialize rtl8723cs on re... | `d1b8c3ed5aea` | hci_h5.c |
| 103 | `clk-sunxi-ng-Don-t-use-CPU-PLL-gating-and-CPUX-reparenting-to-H.patch` | clk: sunxi-ng: Don't use CPU PLL gating and CPUX r... | `f002c96d4151` | ccu-sun8i-h3.c |
| 104 | `clk-sunxi-ng-Export-CLK_DRAM-for-devfreq.patch` | clk: sunxi-ng: Export CLK_DRAM for devfreq | `ca6cbf9bc69e` | ccu-sun8i-a83t.h, sun8i-a83t-ccu.h |
| 105 | `clk-sunxi-ng-Mark-TWD-clocks-as-critical.patch` | clk: sunxi-ng: Mark TWD clocks as critical | `4c7904aa4949` | ccu-sun50i-h6-r.c, ccu-sun8i-r.c (+1) |
| 106 | `clk-sunxi-ng-Set-maximum-P-and-M-factors-to-1-for-H3-pll-cpux-c.patch` | clk: sunxi-ng: Set maximum P and M factors to 1 fo... | `384414128368` | ccu-sun8i-h3.c |
| 107 | `clk-sunxi-ng-a64-Increase-PLL_AUDIO-base-frequency.patch` | clk: sunxi-ng: a64: Increase PLL_AUDIO base freque... | `d2cd63999170` | ccu-sun50i-a64.c |
| 108 | `clk-sunxi-ng-sun50i-a64-Switch-parent-of-MIPI-DSI-to-periph0-1x.patch` | clk: sunxi-ng: sun50i-a64: Switch parent of MIPI-D... | `8750f19f56a9` | ccu-sun50i-a64.c |
| 109 | `cpufreq-sun50i-Show-detected-CPU-bin-for-easier-debugging.patch` | cpufreq: sun50i: Show detected CPU bin, for easier... | `362e712ca085` | sun50i-cpufreq-nvmem.c |
| 110 | `drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch` | drm: bridge: dw-hdmi: Allow to accept HPD status f... | `e805834532c1` | dw-hdmi.c |
| 111 | `drm-bridge-dw-hdmi-Report-HDMI-hotplug-events.patch` | drm: bridge: dw-hdmi: Report HDMI hotplug events | `2e4558922e9a` | dw-hdmi.c |
| 112 | `drm-panel-st7703-Fix-xbd599-timings-to-make-refresh-rate-exactl.patch` | drm/panel: st7703: Fix xbd599 timings to make refr... | `f61e96564da2` | panel-sitronix-st7703.c |
| 113 | `drm-sun4i-Implement-gamma-correction.patch` | drm/sun4i: Implement gamma correction | `75d1c33957e1` | sun4i_tcon.c, sun4i_crtc.c (+1) |
| 114 | `drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch` | drm/sun4i: Support taking over display pipeline st... | `169ec4104890` | sun4i_tcon.c, sun6i_mipi_dsi.c (+9) |
| 115 | `drm-sun4i-tcon-Support-keeping-dclk-rate-upon-ancestor-clock-ch.patch` | drm/sun4i: tcon: Support keeping dclk rate upon an... | `035e210f29f9` | sun4i_tcon.c, sun4i_tcon.h |
| 116 | `dt-bindings-axp20x-adc-allow-to-use-TS-pin-as-GPADC.patch` | dt-bindings: axp20x-adc: allow to use TS pin as GP... | `c436c559658b` | x-powers,axp209-adc.yaml |
| 117 | `dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch` | dt-bindings: input: gpio-vibrator: Don't require e... | `98a548464384` | gpio-vibrator.yaml |
| 118 | `dt-bindings-leds-Add-a-binding-for-AXP813-charger-led.patch` | dt-bindings: leds: Add a binding for AXP813 charge... | `059ef07ac6ec` | leds-axp20x.yaml |
| 119 | `dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch` | dt-bindings: media: Add bindings for Himax HM5065 ... | `34bcb830ea7b` | hm5065.txt |
| 120 | `dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch` | dt: bindings: mfd: Add codec related properties to... | `6745aeb62132` | x-powers,ac100.yaml |
| 121 | `dt-bindings-sound-Add-jack-type-property-to-sun8i-a33-codec.patch` | dt-bindings: sound: Add jack-type property to sun8... | `901accbff222` | allwinner,sun8i-a33-codec.yaml |
| 122 | `firmware-arm_scpi-Support-unidirectional-mailbox-channels.patch` | firmware: arm_scpi: Support unidirectional mailbox... | `c608cd8089e3` | arm_scpi.c |
| 123 | `firmware-scpi-Add-support-for-sending-a-SCPI_CMD_SET_SYS_PWR_ST.patch` | firmware: scpi: Add support for sending a SCPI_CMD... | `92e17d313943` | scpi_protocol.h, arm_scpi.c |
| 124 | `gnss-ubx-Send-soft-powerdown-message-on-suspend.patch` | gnss: ubx: Send soft powerdown message on suspend | `06873d985e41` | ubx.c |
| 125 | `hm5065-yaml-bindings-wip.patch` | hm5065: yaml bindings (wip) | `a96f8d952aaf` | hm5065.yaml |
| 126 | `i2c-mv64xxx-Don-t-make-a-fuss-when-pinctrl-recovery-state-is-no.patch` | i2c: mv64xxx: Don't make a fuss when pinctrl recov... | `a4420f8cb039` | i2c-mv64xxx.c |
| 127 | `iio-adc-axp20x_adc-allow-to-set-TS-pin-to-GPADC-mode.patch` | iio: adc: axp20x_adc: allow to set TS pin to GPADC... | `a1f938613117` | axp20x_adc.c |
| 128 | `iio-adc-sun4i-gpadc-iio-Allow-to-use-sun5i-a13-gpadc-iio-from-D.patch` | iio: adc: sun4i-gpadc-iio: Allow to use sun5i-a13-... | `fd13c5d5ad83` | sun4i-gpadc.c, sun4i-gpadc-iio.c (+1) |
| 129 | `iio-st_sensors-Don-t-report-error-when-the-device-is-not-presen.patch` | iio: st_sensors: Don't report error when the devic... | `6cc7f49d7052` | st_sensors_core.c |
| 130 | `input-cyttsp4-Clear-the-ids-buffer-in-a-saner-way.patch` | input: cyttsp4: Clear the ids buffer in a saner wa... | `da1627af35c4` | cyttsp4_core.c |
| 131 | `input-cyttsp4-De-obfuscate-MT-signals-setup-platform-data.patch` | input: cyttsp4: De-obfuscate MT signals setup/plat... | `dd1af93a5440` | cyttsp4.h, cyttsp4_core.c (+1) |
| 132 | `input-cyttsp4-De-obfuscate-platform-data-for-keys.patch` | input: cyttsp4: De-obfuscate platform data for key... | `38c4d8b0b403` | cyttsp4.h, cyttsp4_core.c |
| 133 | `input-cyttsp4-ENOSYS-error-is-ok-when-powering-up.patch` | input: cyttsp4: ENOSYS error is ok when powering u... | `616c5bfc7639` | cyttsp4_core.c |
| 134 | `input-cyttsp4-Faster-recovery-from-failed-wakeup-HACK.patch` | input: cyttsp4: Faster recovery from failed wakeup... | `47e05de81584` | cyttsp4_core.c |
| 135 | `input-cyttsp4-Fix-compile-issue.patch` | input: cyttsp4: Fix compile issue | `2da7b23bff3f` | cyttsp4_core.c |
| 136 | `input-cyttsp4-Fix-probe-oops.patch` | input: cyttsp4: Fix probe oops | `b3c73d724464` | cyttsp4_core.c |
| 137 | `input-cyttsp4-Fix-warnings.patch` | input: cyttsp4: Fix warnings | `e9aef2daaaf2` | cyttsp4_core.c |
| 138 | `input-cyttsp4-Make-the-driver-not-hog-the-system-s-workqueue.patch` | input: cyttsp4: Make the driver not hog the system... | `ee59658dec51` | cyttsp4_core.c, cyttsp4_core.h |
| 139 | `input-cyttsp4-Port-the-driver-to-use-device-properties.patch` | input: cyttsp4: Port the driver to use device prop... | `c5e37563e5f6` | cyttsp4.h, cyttsp4_core.c (+1) |
| 140 | `input-cyttsp4-Port-to-6.16.patch` | input: cyttsp4: Port to 6.16 | `dbe2f0d56705` | cyttsp4_core.c |
| 141 | `input-cyttsp4-Remove-unused-enable_vkeys.patch` | input: cyttsp4: Remove unused enable_vkeys | `3adb08ca82e0` | cyttsp4.h |
| 142 | `input-cyttsp4-Remove-useless-indirection-with-driver-platform-d.patch` | input: cyttsp4: Remove useless indirection with dr... | `5378058989e1` | cyttsp4.h, cyttsp4_core.c (+1) |
| 143 | `input-cyttsp4-Restart-on-wakeup-wakeup-by-I2C-read-doesn-t-work.patch` | input: cyttsp4: Restart on wakeup (wakeup by I2C r... | `135226c59637` | cyttsp4_core.c |
| 144 | `input-cyttsp4-Use-i2c-spi-names-directly-in-the-driver.patch` | input: cyttsp4: Use i2c/spi names directly in the ... | `4956567a4863` | cyttsp4_i2c.c, cyttsp4.h (+1) |
| 145 | `input-gpio-vibra-Allow-to-use-vcc-supply-alone-to-control-the-v.patch` | input: gpio-vibra: Allow to use vcc-supply alone t... | `45e08489668b` | gpio-vibra.c |
| 146 | `leds-axp20x-Support-charger-LED-on-AXP20x-like-PMICs.patch` | leds: axp20x: Support charger LED on AXP20x like P... | `ee885f8f16b9` | axp20x.c, Kconfig (+2) |
| 147 | `mailbox-Allow-to-run-mailbox-while-timekeeping-is-suspended.patch` | mailbox: Allow to run mailbox while timekeeping is... | `ddcf008387a3` | mailbox.c |
| 148 | `media-cedrus-Fix-failure-to-clean-up-hardware-on-probe-failure.patch` | media: cedrus: Fix failure to clean up hardware on... | `a3de20c76246` | cedrus.c |
| 149 | `media-gc2145-Add-PIXEL_RATE-HBLANK-and-VBLANK-controls.patch` | media: gc2145: Add PIXEL_RATE, HBLANK and VBLANK c... | `385d1b0778f7` | gc2145.c |
| 150 | `media-gc2145-Added-BGGR-bayer-mode.patch` | media: gc2145: Added BGGR bayer mode | `b1451189507e` | gc2145.c |
| 151 | `media-gc2145-Disable-debug-output.patch` | media: gc2145: Disable debug output | `aa006146fa6f` | gc2145.c |
| 152 | `media-gc2145-Galaxycore-camera-module-driver.patch` | media: gc2145: Galaxycore camera module driver | `d7b8e4fcb6be` | Makefile, gc2145.c (+1) |
| 153 | `media-gc2145-fix-white-balance-colors.patch` | media: gc2145: fix white-balance colors | `d808d7dd8970` | gc2145.c |
| 154 | `media-gc2145-implement-system-suspend.patch` | media: gc2145: implement system suspend | `3f9659775c39` | gc2145.c |
| 155 | `media-hm5065-Add-subdev-driver-for-Himax-HM5065-camera-sensor.patch` | media: hm5065: Add subdev driver for Himax HM5065 ... | `221ae31ff719` | Makefile, hm5065.c (+1) |
| 156 | `media-i2c-gc2145-Move-upstream-driver-out-of-the-way.patch` | media: i2c: gc2145: Move upstream driver out of th... | `04d24d569d04` | Makefile, Kconfig |
| 157 | `media-i2c-gc2145-Parse-and-register-properties.patch` | media: i2c: gc2145: Parse and register properties | `42ac1b1b0330` | gc2145.c |
| 158 | `media-ov5640-Add-read-only-property-for-vblank.patch` | media: ov5640: Add read-only property for vblank | `5aa48677af3f` | ov5640.c |
| 159 | `media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch` | media: ov5640: Don't powerup the sensor during dri... | `b5e86ca2fe4b` | ov5640.c |
| 160 | `media-ov5640-Experiment-Try-to-disable-denoising-sharpening.patch` | media: ov5640: [Experiment] Try to disable denoisi... | `a9079e289ab1` | ov5640.c |
| 161 | `media-ov5640-Fix-focus-commands-blocking-until-complete.patch` | media: ov5640: Fix focus commands blocking until c... | `d42ba1010939` | ov5640.c |
| 162 | `media-ov5640-Implement-autofocus.patch` | media: ov5640: Implement autofocus | `639e94cc1789` | ov5640.c |
| 163 | `media-ov5640-Improve-error-reporting.patch` | media: ov5640: Improve error reporting | `99132bcca8ec` | ov5640.c |
| 164 | `media-ov5640-Improve-firmware-load-time.patch` | media: ov5640: Improve firmware load time | `39760aef81cf` | ov5640.c |
| 165 | `media-ov5640-Sleep-after-poweroff-to-ensure-next-poweron-is-not.patch` | media: ov5640: Sleep after poweroff to ensure next... | `9ddb83d2597d` | ov5640.c |
| 166 | `media-ov5640-set-default-ae-target-lower.patch` | media: ov5640: set default ae target lower | `d46586eca46b` | ov5640.c |
| 167 | `media-ov5640-use-pm_runtime_force_suspend-resume-for-system-sus.patch` | media: ov5640: use pm_runtime_force_suspend/resume... | `0f03480e5d68` | ov5640.c |
| 168 | `media-ov5648-Fix-call-to-pm_runtime_set_suspended.patch` | media: ov5648: Fix call to pm_runtime_set_suspende... | `7705e2580071` | ov5648.c |
| 169 | `media-sun6i-csi-Add-multicamera-support-for-parallel-bus.patch` | media: sun6i-csi: Add multicamera support for para... | `a1e98688f287` | sun6i_csi_bridge.h, sun6i_csi_bridge.c |
| 170 | `media-sun6i-csi-add-V4L2_CAP_IO_MC-capability.patch` | media: sun6i-csi: add V4L2_CAP_IO_MC capability | `f0b0e2ae8bed` | sun6i_csi_capture.c |
| 171 | `media-sun6i-csi-capture-Use-subdev-operation-to-access-bridge-f.patch` | media: sun6i-csi: capture: Use subdev operation to... | `2409b62538d7` | sun6i_csi_capture.c, sun6i_csi_bridge.h (+1) |
| 172 | `media-sun6i-csi-implement-vidioc_enum_framesizes.patch` | media: sun6i-csi: implement vidioc_enum_framesizes | `b0f43b990523` | sun6i_csi_capture.c |
| 173 | `media-sun6i-csi-merge-sun6i_csi_formats-and-sun6i_csi_formats_m.patch` | media: sun6i-csi: merge sun6i_csi_formats and sun6... | `85030c734bb1` | sun6i_csi_capture.h, sun6i_csi_capture.c |
| 174 | `media-sun6i-csi-subdev-Use-subdev-active-state-to-store-active-.patch` | media: sun6i-csi: subdev: Use subdev active state ... | `0c438b3a5abb` | sun6i_csi_bridge.h, sun6i_csi_bridge.c |
| 175 | `mfd-axp20x-Add-battery-IRQ-resources.patch` | mfd: axp20x: Add battery IRQ resources | `561e37314446` | axp20x.c |
| 176 | `misc-modem-power-Power-manager-for-modems.patch` | misc: modem-power: Power manager for modems | `48722668c4da` | Kconfig, Makefile (+1) |
| 177 | `mmc-add-delay-after-power-class-selection.patch` | mmc: add delay after power class selection | `cc541c517e0d` | mmc.c |
| 178 | `mmc-sunxi-mmc-Remove-runtime-PM.patch` | mmc: sunxi-mmc: Remove runtime-PM | `33c5231e0211` | sunxi-mmc.c |
| 179 | `mtd-spi-nor-Add-Alliance-memory-support.patch` | mtd: spi-nor: Add Alliance memory support | `00467f6c1dc8` | core.c, core.h (+2) |
| 180 | `mtd-spi-nor-Add-vdd-regulator-support.patch` | mtd: spi-nor: Add vdd regulator support | `48fb368a71aa` | core.c |
| 181 | `net-stmmac-sun8i-Add-support-for-enabling-a-regulator-for-PHY-I.patch` | net: stmmac: sun8i: Add support for enabling a reg... | `fa80f05a6818` | dwmac-sun8i.c |
| 182 | `net-stmmac-sun8i-Rename-PHY-regulator-variable-to-regulator_phy.patch` | net: stmmac: sun8i: Rename PHY regulator variable ... | `4bc2d5b9f73d` | dwmac-sun8i.c |
| 183 | `net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch` | net: stmmac: sun8i: Use devm_regulator_get for PHY... | `41d867cddaf5` | dwmac-sun8i.c |
| 184 | `nfc-pn544-Add-support-for-VBAT-PVDD-regulators.patch` | nfc: pn544: Add support for VBAT/PVDD regulators | `efa45d11e0ac` | i2c.c |
| 185 | `of-property-fw_devlink-Support-allwinner-sram-links.patch` | of: property: fw_devlink: Support allwinner,sram l... | `e28c92494b43` | property.c |
| 186 | `opp-core-Avoid-confusing-error-when-no-regulator-is-defined-in-.patch` | opp: core: Avoid confusing error when no regulator... | `5c9259b91a5e` | core.c |
| 187 | `pci-Workaround-ITS-timeouts-on-poweroff-reboot-on-Orange-Pi-5-P.patch` | pci: Workaround ITS timeouts on poweroff/reboot on... | `3f1a6443ef36` | portdrv.c |
| 188 | `phy-allwinner-sun4i-usb-Add-support-for-usb_role_switch.patch` | phy: allwinner: sun4i-usb: Add support for usb_rol... | `9384e9542ba3` | Kconfig, phy-sun4i-usb.c |
| 189 | `power-axp20x_battery-Allow-to-set-target-voltage-to-4.35V.patch` | power: axp20x_battery: Allow to set target voltage... | `46493cb95bcc` | axp20x_battery.c |
| 190 | `power-axp803-Add-interrupts-for-low-battery-power-condition.patch` | power: axp803: Add interrupts for low battery powe... | `3e4b43db8292` | axp20x.c, axp20x_battery.c |
| 191 | `power-supply-Add-support-for-USB_BC_ENABLED-and-USB_DCP_INPUT_C.patch` | power: supply: Add support for USB_BC_ENABLED and | `c271a238f52a` | power_supply.h, power_supply_sysfs.c |
| 192 | `power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch` | power: supply: axp20x-battery: Add support for | `dc52e71a420e` | axp20x_battery.c |
| 193 | `power-supply-axp20x-battery-Enable-poweron-by-RTC-alarm.patch` | power: supply: axp20x-battery: Enable poweron by R... | `24a2fadfced9` | axp20x_battery.c |
| 194 | `power-supply-axp20x-battery-Improve-probe-error-reporting.patch` | power: supply: axp20x-battery: Improve probe error... | `c527915eb794` | axp20x_battery.c |
| 195 | `power-supply-axp20x-battery-Support-POWER_SUPPLY_PROP_CHARGE_BE.patch` | power: supply: axp20x-battery: Support | `e1e4ad3c4acf` | axp20x_battery.c |
| 196 | `power-supply-axp20x-usb-power-Add-missing-interrupts.patch` | power: supply: axp20x-usb-power: Add missing inter... | `6dd47cd1ee09` | axp20x.c, axp20x_usb_power.c |
| 197 | `power-supply-axp20x-usb-power-Change-Vbus-hold-voltage-to-4.5V.patch` | power: supply: axp20x-usb-power: Change Vbus hold ... | `9880eaca7a2f` | axp20x_usb_power.c |
| 198 | `power-supply-axp20x_battery-Add-support-for-reporting-OCV.patch` | power: supply: axp20x_battery: Add support for rep... | `90dfd9733896` | axp20x_battery.c |
| 199 | `power-supply-axp20x_battery-Fix-charging-done-detection.patch` | power: supply: axp20x_battery: Fix charging done d... | `488236884b03` | axp20x_battery.c |
| 200 | `power-supply-axp20x_battery-Monitor-battery-health.patch` | power: supply: axp20x_battery: Monitor battery hea... | `c2539f144cef` | axp20x_battery.c |
| 201 | `power-supply-axp20x_battery-Send-uevents-for-status-changes.patch` | power: supply: axp20x_battery: Send uevents for st... | `d9a8e2ce4c70` | axp20x_battery.c |
| 202 | `power-supply-axp20x_battery-Setup-thermal-regulation-experiment.patch` | power: supply: axp20x_battery: Setup thermal regul... | `543cdf679cbe` | axp20x_battery.c |
| 203 | `regulator-Add-simple-driver-for-enabling-a-regulator-from-users.patch` | regulator: Add simple driver for enabling a regula... | `442d6912f184` | Kconfig, userspace-consumer-of.c (+1) |
| 204 | `regulator-axp20x-Add-support-for-vin-supply-for-drivevbus.patch` | regulator: axp20x: Add support for vin-supply for ... | `849676865a11` | axp20x-regulator.c |
| 205 | `regulator-axp20x-Enable-over-temperature-protection-and-16s-res.patch` | regulator: axp20x: Enable over-temperature protect... | `aeacc51e5cbf` | axp20x-regulator.c |
| 206 | `regulator-axp20x-Turn-N_VBUSEN-to-input-on-x-powers-sense-vbus-.patch` | regulator: axp20x: Turn N_VBUSEN to input on x-pow... | `f241ce33c253` | axp20x-regulator.c, sun50i-a64-pinephone-1.2.dts |
| 207 | `regulator-tp65185-Add-hwmon-device-for-reading-temperature.patch` | regulator: tp65185: Add hwmon device for reading t... | `d6cfba904118` | tp65185x.c |
| 208 | `regulator-tp65185x-Add-tp65185x-eInk-panel-regulator-driver.patch` | regulator: tp65185x: Add tp65185x eInk panel regul... | `6d604af83206` | Kconfig, tp65185x.c (+1) |
| 209 | `rtc-Print-which-error-caused-RTC-read-failure.patch` | rtc: Print which error caused RTC read failure | `d92e4969a270` | class.c |
| 210 | `rtc-sun6i-Allow-RTC-wakeup-after-shutdown.patch` | rtc: sun6i: Allow RTC wakeup after shutdown | `fc0d46cc7c7c` | rtc-sun6i.c |
| 211 | `sound-soc-ac100-codec-Support-analog-part-of-X-Powers-AC100-cod.patch` | sound: soc: ac100-codec: Support analog part of X-... | `c0952f0527ca` | ac100.h, ac100-codec.c (+3) |
| 212 | `sound-soc-sun8i-codec-Add-support-for-digital-part-of-the-AC100.patch` | sound: soc: sun8i-codec: Add support for digital p... | `aa96ef7e331d` | Kconfig, sun8i-codec.c |
| 213 | `sunxi-Use-dev_err_probe-to-handle-EPROBE_DEFER-errors.patch` | sunxi: Use dev_err_probe to handle EPROBE_DEFER er... | `bd83c5592609` | topology.c, panel-sitronix-st7703.c (+3) |
| 214 | `thermal-sun8i-Be-loud-when-probe-fails.patch` | thermal: sun8i: Be loud when probe fails | `aea2a6a0dad7` | sun8i_thermal.c |
| 215 | `usb-gadget-Fix-dangling-pointer-in-netdev-private-data.patch` | usb: gadget: Fix dangling pointer in netdev privat... | `1a3a502402d3` | f_eem.c, f_ncm.c (+4) |
| 216 | `usb-musb-sunxi-Avoid-enabling-host-side-code-on-SoCs-where-it-s.patch` | usb: musb: sunxi: Avoid enabling host side code on... | `2f2bc8c3fbba` | musb_core.c, sunxi.c |
| 217 | `usb-serial-option-add-reset_resume-callback-for-WWAN-devices.patch` | usb: serial: option: add 'reset_resume' callback f... | `6668c2e64770` | option.c |
| 218 | `usb-typec-altmodes-displayport-Respect-DP_CAP_RECEPTACLE-bit.patch` | usb: typec: altmodes: displayport: Respect DP_CAP_... | `d6b00ba0e47f` | displayport.c |
| 219 | `usb-typec-anx7688-Add-driver-for-ANX7688-USB-C-HDMI-bridge.patch` | usb: typec: anx7688: Add driver for ANX7688 USB-C ... | `ce1a3ecc2fa0` | Kconfig, anx7688.c (+1) |
| 220 | `usb-typec-fusb302-Add-OF-extcon-support.patch` | usb: typec: fusb302: Add OF extcon support | `144530433533` | fusb302.c |
| 221 | `usb-typec-fusb302-Clear-interrupts-before-we-start-toggling.patch` | usb: typec: fusb302: Clear interrupts before we st... | `19b79cda1dcb` | fusb302.c |
| 222 | `usb-typec-fusb302-Extend-debugging-interface-with-driver-state-.patch` | usb: typec: fusb302: Extend debugging interface wi... | `5ea24d51821b` | fusb302.c |
| 223 | `usb-typec-fusb302-Fix-register-definitions.patch` | usb: typec: fusb302: Fix register definitions | `d672d78b89e9` | fusb302_reg.h |
| 224 | `usb-typec-fusb302-More-useful-of-logging-status-on-interrupt.patch` | usb: typec: fusb302: More useful of logging status... | `8618ac54bfcb` | fusb302.c |
| 225 | `usb-typec-fusb302-Retry-reading-of-CC-pins-status-if-activity-i.patch` | usb: typec: fusb302: Retry reading of CC pins stat... | `636cc1b239e4` | fusb302.c |
| 226 | `usb-typec-fusb302-Set-the-current-before-enabling-pullups.patch` | usb: typec: fusb302: Set the current before enabli... | `da54e4696c24` | fusb302.c |
| 227 | `usb-typec-fusb302-Slightly-increase-wait-time-for-BC1.2-result.patch` | usb: typec: fusb302: Slightly increase wait time f... | `d23a432cc778` | fusb302.c |
| 228 | `usb-typec-fusb302-Update-VBUS-state-even-if-VBUS-interrupt-is-n.patch` | usb: typec: fusb302: Update VBUS state even if VBU... | `f1ef44be900f` | fusb302.c |
| 229 | `usb-typec-tcpm-Fix-PD-devices-capabilities-registration.patch` | usb: typec: tcpm: Fix PD devices/capabilities regi... | `b05486720062` | tcpm.c |
| 230 | `usb-typec-tcpm-Improve-logs.patch` | usb: typec: tcpm: Improve logs | `8189e2f8b1e8` | tcpm.c |
| 231 | `usb-typec-tcpm-Unregister-altmodes-before-registering-new-ones.patch` | usb: typec: tcpm: Unregister altmodes before regis... | `ae4e6f449c02` | tcpm.c |
| 232 | `usb-typec-typec-extcon-Add-typec-extcon-bridge-driver.patch` | usb: typec: typec-extcon: Add typec -> extcon brid... | `ae68b1494b81` | Kconfig, typec-extcon.c (+1) |
| 233 | `usb-typec-typec-extcon-Allow-to-force-reset-on-each-mux-change.patch` | usb: typec: typec-extcon: Allow to force reset on ... | `35fa24b62d8f` | typec-extcon.c |
| 234 | `usb-typec-typec-extcon-Enable-debugging-for-now.patch` | usb: typec: typec-extcon: Enable debugging for now | `82e832f54944` | typec-extcon.c |
| 235 | `video-fbdev-eInk-display-driver-for-A13-based-PocketBooks.patch` | video: fbdev: eInk display driver for A13 based Po... | `5373656aae6e` | sun5i-eink.c, Makefile (+3) |
| 236 | `video-pwm_bl-Allow-to-change-lth_brightness-via-sysfs.patch` | video: pwm_bl: Allow to change lth_brightness via ... | `d1289f356aaa` | pwm_bl.c |

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
000c586a34ad82e4673e6dfda5457147b0d85606
00467f6c1dc8fff19839cca8909f9fc29cff7f27
019b5fe6a62f804b0a3c1bc32b014bea4983dc50
035e210f29f9ef80bdade15c9abf482930ad6f75
0395da54b8196c91aa132f56e6ab0d0e4abdc589
04d24d569d041161f44cde6acff2999fd9b73fae
058f37ec620528d6d4ebc11aba6d0b65694185fb
059050249c1d35276ebc8323bcddeee8510e2c1e
059ef07ac6ec8cb6df756402278c0408b0d7cb5d
05e16d776c12bd7a31a80a4b9485afe67581c5a4
05fded634606c9f96d33246df3e928fcce656b5e
0676a665a91d8b48e0d7042a15809ff8e5378762
06873d985e4124a65dcadedd6aa327a1de69fcb4
074c33f4b2b60ea6d76968099f8210c61bbad7e1
0788787d1240dba85ecbbdb559cb46d413975656
09744193cdcf400e5a4c54d9309acf5aea3a591c
0987e0158d63711b01a2435fa515d80a5b540422
0a4a41fa8ade7228868aa848a58c2be52e3ebe75
0bfb8399d8b4f46ac87a2ae980126ca2c6c6cb1f
0c10a80b8e37d9a7fc57d8bf968c70419423065a
0c438b3a5abbfe509eefb5303a2d8e4af7fe500a
0d003a88bcacf5f405f3922b0c56b7eecdb68386
0e86acce22820a1b61e674de21f25408aba69812
0ebd4ab1a25d17cb321499d1ab328cd7d0efa033
0f03480e5d6811d4ea60629b504e68eb36e8e0e4
1000fdf61f22e06c607f003ef500d75266bc3920
12d7983166ed867dd72c023af036b1397aec66ba
135226c59637b44a58c28eed1ae3fb80e32558c7
1415de6f04125006c28aca89749a2709fd4294e7
14453043353361c0065e30c899403408ea1751d2
15ef8921384b272e193a44812ec8f84eb982ce2a
169ec4104890f77b3ed761bd92934ce91906d03c
17c23b36efb63cd249c5cfc8ce4a6b790f1dfeda
18640635e385dffab84e97be3bd0d9a1f145326a
18df5a34038c63bf771a9ab221c874e601b81f2e
1989d73c62ac37fa9130595b0543c0459f77aed5
19b79cda1dcbf9b0c5284414d7cfa84dd308bac1
1a3a502402d3288c5676fbf79d2e72e9e8e3e61a
1ab2cc80d4c013f9f63ff7cc0412894abad1b575
1df14f80a2234d5d78d556d7de6dd5357350401e
20dc0b0f3da7895d50f2824b4608c5e44729f892
2134cc3eccff78757188425e0a249cc7be9fcaf1
221ae31ff7197eb341df91ccd829dc0fe222a63f
2301fedd353a65ab03e8ac19b43da8ba8498b437
23514cbc264217bcb6c2e6f199c38d0f713061ea
2409b62538d7e623fed03358219f80c79430482e
24a2fadfced9799dd7ea4195edc3cf5f59a5d960
24eef32e5d453be8b2780c8dbc32311064fbb735
251198af980dcd9fe85a78514f114dcf193538c3
270e1512a91f294089822d2c3a3fcb8560d86561
282f0e41b191b88d286081221ac40120252fb41f
28d9bff7bbc1085a8126a9a70d7dfb3b6a62f1b9
29fe01c39d6ca9a293d046938db4decde8f82e5b
2a8a9e3104ce70230ca67a39fd406d84662e77b2
2ce741f43a65732bd9078046c272743d06a41701
2d7c88fc2af6d07ccadc99b157753638b4940293
2da7b23bff3f433868b6ca56225f53b4d5aed462
2e09c0cf2afa5c4bf0293b12b6653aac8431d454
2e4558922e9a16fa9e7d29b5a912279906dacb74
2f2bc8c3fbba94de0c43fc061a70f4e16d7c3bf5
2f8b8f221f69c044f5d8821025c60ae76cce2bfc
308f56b99b313484b257e4d574b45f305d20c29c
3110211a08b8a2d759a8c01170732fa5ffb0d850
315aba156b72f9e93430c8ffda6f02d09bda47d1
3204bd45b054653cd8c9b5691aea86359822a753
325a2fb637eaac4bee2a6ea78e10040b6b2e7c7d
32714948ee14cc6a990115c6594c481148ac950f
33c5231e021131f742ab815a1211a81b2093814c
34bcb830ea7b7a2a835604050fe3502f29951a9e
3561685a36bdb6cba7af84f303e068b8448bf652
35fa24b62d8fefe3c6eca767939391bb39569b1a
360891b201c9534abc7441aca1db3eb3aeaeea3f
362e712ca085c612a3325789df035bbb699348aa
368c89a83102c2b8e8c6acf72963bfb90caa1d24
36b50c879cbe1ac572e0c2c9dacc32f7405fd36e
379b3c9bf09db69afb31eb1f9f7f65e5a83b4308
38441412836804c8b3add48632e2d587e2d90c02
385d1b0778f7dd86842459c02a5702330371382b
38c4d8b0b4039f2a14bc0342e51348e226717725
39760aef81cfc8305d04f65e9a6149519b8d9352
3abf71beb7655982c8ea766110734342d1b4b975
3adb08ca82e02dc9bfbd8e01d7f1957048161e90
3b1f07be7287ba414ee6920c1d5a22d200733b37
3b4036339ed5ffeb92f907d0b47b736bf5b12637
3d72091622a7cccc4896cbfe71e25503dd174b8e
3e4b43db829267e63a613fe706770e99e48fdd5f
3e83ea68d7e6cbe55637ee15ca8d613b57496ca6
3f1a6443ef36006523a0f169352f2f69dfbf4a18
3f375e42748006d39032cb24896f6ad01c57f507
3f384c786fde4cbdf48499fbc77b582630dd6ede
3f9659775c39e3e333f8b68f3baf1bf2d8c5053a
3fb6768c3303c9a8bb0465cca521c0977fe02c92
401cf6db854dc76d05332b5699597836d4eb0845
4034f4e90fe681ff4645fe724424ae48f3909e19
4042b1c4ed4e1cfe9170cbb57d49e13f419afa3d
404a4f5b185c2fa8946f4cdc45d5236f635ccf33
407da3bb87888f573863184cbd690280c001ad23
412294545ec91452cc3eccff746a4243879b4cde
41d867cddaf5e97ec163019d673ae15e184beea3
426ff5c4a9a47d9da2701ce9365af6fd64ca50c9
42a96825b819aef86f3c08ba6eb435cf4262c10c
42ac1b1b033051a109ec5f2f796d5c598c266beb
43a7177563683a1e7d192138f65073d687ed068b
442d6912f184ccb9e0d3f0cae317d76aea561c69
44ed294ee215d25c629c547d7aa767d6d474f658
4546be7fd3812ee3a733beececa504bf7cb4bfac
455e56be4e202bd7dee9cf188e1063e874c8f5d8
45e08489668b33255f20cdba3b2927fc4cb2c8eb
46493cb95bcc10a72c1103a26d794776c8968240
46db097304f674f7daff29b6710463e1b6ac62e0
472d4b36112e4463498f165982d47ef15c36be28
476ae5840384c7b61eb4270cdf7641772807f100
47e05de8158448eb083838045f8aac3e45a09e2d
484b8abd16c1dd8ddaa0c9027b53de524d24809c
48722668c4da2bbe831afcbb16d5a3c43a17e33e
488236884b035bc7e3ab2ac27b5abb4bfbb82b3e
48fb368a71aa4d14c37b39f30e84529b7507064b
4956567a4863c841d2b9339416e56ba3a3e3235f
49999c3dbebce9f4542e5f0a9db55377c611c011
4a2e4646db5c5202f822d7b3958a312ea3c0b8e7
4a77c8ac8b0e2b479e81fb817bd05fd59b2788e3
4b1c8532a7fbfc7e2b3e42fa41ccd45b31bfd8e3
4b2f43e4e23c5e6184568a6b0bf0e85fce4aefb3
4b393b56438e7a170b78930bef7c538f91d5ef45
4bc2d5b9f73d952e97473128d1ad7927bcfceece
4c7904aa4949e751c1313da5bb69c5c0656b54dd
4cc61081f4976fe099e43da801811e3756f870be
4e1ffe039332d9041531f512c208506e571d0a5c
4edd2fb769ff25e9c348b63c7fb5aa79c16a52f1
505db041831ffe038d8cbb0920c3b2d97d8d4a5f
51557cb59db2cf6317ebb3a9ebbf2f808ed71bc7
52961661dcef9266fc76b8c4755004e1e013a643
5323f01be1bd567087b616965c90581d2fc8ed08
5373656aae6e4a4b21a407c91fa2891ffdf6f3b6
5378058989e1bdda285ba0acddb12d0f95d21c93
538b7bed8233cd18367cd34fb607d8a967aff845
542310e242c48b0a793d12532d7f2ff2f6679658
543cdf679cbe303243af83c06431058a9d5930d9
545864cca39f36c642f8c86759d4fc55dbb85cf0
54669ac67e47835b8cc3eea215026385a0050567
558ee0b5606d131de95198b99853c568b5ca3a84
561e373144469232ae9a06314590de367ca43d66
56afb6bff57f83073c83a49f6f6bccf387ab8116
58fa02e703c12f3304f6711fea0d58921391a54a
5aa48677af3fde2b4a95fe7dadf8761ad474c01a
5b1f89dbd335917afc7e2f63467562509eabf4d7
5c2859b3cccd1b1b3f1700fd70c06770f418247a
5c9259b91a5e4d7adc9bfb2d3331109957e41c85
5d46a9e553570329c9b6482186b28766ae1fae21
5ea24d51821bcada6db6ff470f04dc77949dffdf
5f76b8851beb09853ef80bd190178eb03fe15dd9
5fa9f90b1e132dec177f60af5aca3c1ad2e019e8
5fb3c2c424a0c02e59943fba68dc9448de0f7f10
60aea9df8e7b65137adb0d8f081576fda5127f5e
616c5bfc7639a34a048d0b4cb36b73d2960ce623
62c8a5f644fb4bacc836456d83bc0cc69645102a
635972bcdd65219aaec23d98e1405f8bdf43d3ba
636cc1b239e43e2359ad66907679e95f6a96068a
639e94cc1789aa3841edefb3846c97059479b1fd
64f543a201145dfbc832be06aa3dc6d942d96bf1
65ab846a1feda2dcedb84b393bee71fa34593c4f
6668c2e647703b7664475a4069d8cb5e08cdb535
672717a70d3fa52c55aa222a011d27dff2756787
6745aeb621323a7d0b1022730c8ab32e4203520a
67cacba5ece1f10e6c611b0ad62911e128f4406e
681152c96fe02df6fb36ecef2fed562511d871fe
6945687a57dff96300080ec1edb2df467f376050
6b1d64060b59702b34bf07068aeff10139c69400
6b72eec004a4dab3878b7d5099c6b25ceff0894e
6c8bbaf43b8eaf62d4682ce66a35fc7f341f4a13
6cc7f49d7052b3f5178539112bafcf5985c3c1b7
6ccacf9c0f118a48731436f46b0632e058e536fc
6d604af832065db8e9603a53ab85ec26b42c287c
6dd47cd1ee0965e25b854984bcf9f3c1d35eaad5
711fd07f4f2fb4697271dd78076e2d4c6092c685
75d1c33957e1db4ac4f803c85ff58c45d32fad5b
75d25c0f809655532b54cdabe4e5ac810c1fa0cc
76fd556315ddc27df6cc7cdc159e6a47d66f4659
7705e258007194e67bfc2e1ae2b70861205ad890
77b6d5f86a69c0e37612406ba6715c3040100271
78c40257c314701e08887a90c995d9c97c1e9a37
792b816c952bcf5dbf7c3ac7d90937bc71f0a7cd
7bd8ad9c9778bb66afee88678c1a45d44a59be5d
7c46723de140a192eb485cfdf9ca4ee467d93b1f
7c87d7c71b5d5982bdcf592fe12fb851c30d54de
7e2082f55e6595ca976245d7a7ac1d89d5b1258b
7e7c505713145cd6e7543b86f27e9c1c7b4a74e5
7ff04b0bdae864def87539f21ed65134d883be29
8022c01f46c79dcc8457e580b784904a24dec9f3
80b16fcddf1837c631796c25f3123b7adbbf815a
81241983ba12f281a839a530da460088170cca2e
8189e2f8b1e8d73890b335b4255fa07e1e11fb13
8225e98fe295d59bbf4cd5017e04110077ff4d99
82458044eed7f24ff5810818c05aaceb87522ddf
82745a579de223e56b7c35c8e4a5e7f9e91e409c
82c1ef311dfa48e730d927ae71322bfee0430545
82e832f549443dd6784ff83736bbff1979c66f1f
836de5e4296b33c8145b3e6bbc09a7836f059212
836e3c6dde4128b0c846e8baeffb6a8e8ea58e00
83fbd972f2a780e4429f51cc0eec543cffed26b6
846209f909c9cf9d7a29a72328ed27b9ee504ac1
849676865a11e1e2289eeb3be821f9e19ea12c0b
85030c734bb151e5b91e79c635967ea53e3a3148
85906a7fbd369ed9a0f6637d1f25eb5ce71d7a4b
8618ac54bfcb97c03e345cca7335f56351590d25
8750f19f56a935544b273de02153bca8cca3067e
89163782655ea1a6507c0445e55d220711d5d7c8
8977f7a800aeac075fed063786f6f46e92a593eb
8a8d8ca9c2cd5d399cdcce38d2a66ad8dcb5be62
8bdcc131fedb576a8db65bb6e87ca8742660add0
8c597603a316edf73fabf320a412b2b636c691cd
901accbff22299264f49c6209ac5e7e73e2e875a
90dfd973389661adcf4cb0d7594ef6d2ffa4f996
90f292bafa6d6198248b7349cd9945a1258ceaac
9159b591ce223a9b432e31410c522d653f5b059d
91877bc54df84b7fabe8265b152ac38032193403
92e17d313943f86a74fb5348821f2076ed66d58e
9384e9542ba3502e2908036be9020bb65ffc3400
95a8f4f5c78481e12ca0be354835531ae71f3f25
97a40516954459a0b55a9c49c3130910be5c6b10
9880eaca7a2f62b2f7ae42e75f302294e83181df
98a5484643843d4e6fceadc7c8cfa54c512bd7d6
99132bcca8ec0cfe040be718c89c754ef0051804
99d327853acbc5d6c6d4140f004f82fcd5c40ea1
9a7f38264bbc353a097cf1ddd56f86681d2c8475
9ddb83d2597da91098fcd2362b3eee19cd889ffb
9ecccf77a9e6bdcaad4ab62225f14f4e42da0147
9ed682abf8c8c9b0f701562789f208757b8f39ca
a02549f60d913332f50fad6f2c5907169633ab5d
a1398167dbe8f451aaf5331159806738863cb988
a1e98688f287ae916670c1a43cd98c786d8a31a1
a1f9386131173c601dc3d8d9232d5e39b81388ab
a23ed976ee720c2445791716d975f040ef576c2b
a3de20c762463e20ec2b691d553894f4b48dae56
a4420f8cb0399502a5b1fd25f7dbd7320c1b7ef6
a59cb6bd62351166ac38d070c12cfb7dfeff411e
a5b7326c857524e90c52998545ba7f6fb572bca0
a5de8971554d5cd8ff1bb665d7e5c58087a7f1a8
a8ee1b34a672b7291293887f9cde1cad01787048
a9079e289ab17afbf6e56ba480646749bbe63200
a96f8d952aaf4b58aae5b59bf2c41ff5a2944de7
a987a03decda46c52dbcc0e399ca2349d48f6b97
a9b433c7c17a1a0e308fe3364a79f54ab640569c
aa006146fa6fab6e5990824db17a335624414925
aa96ef7e331de5408b1cc3bb3eccefcdeae1a547
abf887a3265a84d1593b319133e5ee106301a23a
ac76eb562601f29b0bca131770d85936a398fac3
ae4167d13fa154234c7fc616fa7a57d60020cc39
ae4e6f449c027fe4951c09a82da7eb844c32d192
ae68b1494b8169fe39adadb59733998e5f54652d
aea2a6a0dad79e34fb74777825991051c75d31a6
aeacc51e5cbf50b6ba83e4eaedc898d84faee2d3
aec6c912e969a433916d8f40b663fb3bef57cdf3
b05486720062e0bded36291a6f54dfb7c1530598
b0d0e0e7cbe9d70a50a8a9cfdcfdffb028d6cef7
b0f43b9905231f2835e8f7475d3d545ce6bbca21
b1451189507e0d1d0d425f1fa4477e9869c8dd00
b241ef1dff821a0915ac1345a27256ce913a3937
b3c73d7244644f61a019fc4cb5236b90cdfa8f53
b4f121b883403a1eacbe797574da04d8b9867075
b5e86ca2fe4bafa43cd73a0390a998bc90b3c8d9
b75f5bf0d822ac325c205a489941f33256ed4b9a
b8344d8eb9d000bc2984a5fcafc25b527f361b5b
b94c32c09b848a2b678554a39e81e31cb0ee5ea0
baabc51678faaf2020ee7791e2a52e39517cbc93
babd7ba10901306332153cf26d6b97700c3a0630
bb01531627146b6235b863e36fa978cef608d538
bb7878b3cdbebd2e3c5975b65f92f59141bd76b9
bbbfdc8bc71a4d5a6fb291aae3027f40dd999816
bc4e7ff402a8509cfc6a1c65c434b76adab1b767
bd83c5592609c8e66280117491c62337c0c5a249
be75f442cae72a4e646e1f5d7374f579ee026c3d
bf158ec720514f6b714ae71cb95d5792fdbc411d
bfaf13fd69401d5c6e0f512277e3f84bd12b1036
bfbed3e6926704dccb61277ec991afff33b84628
c0952f0527cadd6d0631f88e72d7e82f3e1c4c31
c0add6f072c443e3cdf2ce1387a5da46c82e6399
c0dffc32c3a65a1c25bf04f979faf8b6a82b88f8
c14e5e16fb3eb34fbfc87bd4aefd88981a9d767f
c1601a5d5088a43c4a92fcb3ea1f4529de6a584c
c23b72ad5a483643ee89ca9f8731d92774f4735a
c2539f144cef118aee2e09cda0b8c0c58d368fe2
c271a238f52a6955996c8b781ada54e980993809
c3623224b8c0f881cd2f75fe43399d765612dcfd
c3ebe28518e3178406d7b112db9b1475355975f3
c436c559658b7d5e26176d52504b4a5a4fda73dc
c4ff09ffb5ec28fe119e3fa89dbd464b5d208637
c527915eb794fac0a75fce1fa096e2133050e25b
c53547f453102a2add3119cc599eda1d3fcb1f4e
c5b7968c7a8250669ecf04a0b0804f8d79984925
c5e37563e5f69874bf7dfa42d6cdd737061ac800
c608cd8089e3f73037e77a061af2038508ba90cd
c7f9993fb9fa967e80d5b2dc2d422b5dc8ce9f7c
c8c7ccf8c9b5f40503fdad69170c21279337dac4
ca6cbf9bc69e68eb939e42baf29d374e176104e8
ca92cb0984d06618ddf61ca20a543eb263a25962
cb05a11519a68c95d48d47b6d42fd68e81f51bb2
cb90c0e2677a987f4928d2030c7af510b1baf629
cc541c517e0dea4d8d362980eff9f3d2283ffbdb
ce19656781252e0d532425ee4858734d5634cb1f
ce1a3ecc2fa0477b447fad617cf25b94d626a9f2
cf056f9d1d534ffae9793137b755214549cdb572
d1289f356aaa248c8caf7e198032922f0e9e36b0
d15c101660339e266a7a3548aaea04a48f2fa108
d182957e3479420bc224a5ec7df1d5ce1430cf2f
d19697dd4b59d117a79f218bce9d0e0ec909d6e4
d1b8c3ed5aea01c318002f6842f5391fd6d68a76
d23a432cc778455189537e497b2fe5077686eaca
d2cd639991705e5180a9cb8566a08ea8d429087d
d33975afbcf46a53258f1ed2f4f5602d7b1ccfaa
d3a05ab7280719e14989495aa6bc409ba52c70ae
d3aafc0e82f025df6608fc273e11287bcaaed7e5
d411012cf317335c075daa0b48309c6e8ca76075
d42ba1010939131685bdfea2c393e24ffa1193fe
d46586eca46bf3e85854e61ac90c6d22d5092469
d672d78b89e93cc2e446a15d2bfbb8d5d29455e0
d6b00ba0e47f4ae5dcb634d68bf6b2f69776e7ed
d6cfba904118678134f123c54d7bfb901e02561d
d7b8e4fcb6bec026c30eadf8c6d8e76bbcc2883a
d808d7dd89700ff848065f37bcfeea01b8631bce
d92e4969a270a358d68542495a37a67f4f8e4484
d9a8e2ce4c70a517e32da1371f2f3b295a80abe2
da1627af35c4e4b4eafc1e42ef255a2edd110fd1
da54e4696c24203e3fafe2d08312ccac72a42d3a
da61763234048d21610acb51d67924cf4aaabcd9
dbe2f0d5670532898fc7dabce014697b8d42eed2
dbfa68bb8bff41a44713e8248f518f045b90f176
dc52e71a420ed1baba6c504500d62806f72c5092
dcdcb612a1bb9a614bbddaf099b7866851b0786d
dd1af93a544046dc8bb4d596b489cc1d2ec117d1
ddcf008387a37a5aa76118c77ba3554a3ef3475a
e0c585577e066959d3749845aefc89c44b857165
e0de25f60a3535d345b33dcc541c814499151788
e1e4ad3c4acf9ea58571579b9a3eddee393f046b
e28c92494b435a8bb8b42f385b08f95303c51e10
e43c6b985ac6d4f40a8e15526460c2d201d71407
e48549cc1b24a6e51f469768b1a2c13cbf3199d7
e4b7f55f57e5c895fe5dea8d5712affe95fc5f9f
e805834532c1b09ab54b15717f0a59b26f397cb2
e8b24e85296e6acfe0151a2ea9a7c8d498c85cd3
e9aef2daaaf208e2cfc3e02778ae5a63042186f5
ea78de6c4aab8eff9974c40fbefa36042e794c5e
ea92626f9272ba51dba6dba2dbc70dc58e5d055e
ead3bcfa953eb0248206557e61608a4d686da2ae
eb4ea7b5f64403ab03684cbcf9650cdec7f82129
ec30b77c7935d7f1ec1ea430424dddfe552e55c8
ed4d0a091a27c0cf4df577178de481f0b7f534db
ed7bdf184c5acfb1b82d8374615a05080794585b
ee59658dec51dd8e72655b243161e7fcd213d415
ee885f8f16b9702908a3b0e52f87b060a60311f1
ef5deb15a48bd970f378ae63a058ecd70bf42834
efa45d11e0acc23471af017ee59d4e7bd3ed1937
efde7c83c1b9f8ea84c13e1eb6511593326aa14b
f002c96d415150a714932921d8361c910d7ceb1b
f01c1716f180cb356fd9c9a12ea0eaf4ed7d9069
f0b0e2ae8bedcaaad48ced97ab1d257e6f778e7d
f16fd80bf929f431bb28d9adf059db5acd058c69
f1a9b4f7e3a451514b09daa50b43494f8f86612c
f1ef44be900f311965351eff277860734461c108
f241ce33c2539195316bdb39a4d41b82d500d57f
f3157390fffbb9dcc634e99d1d0e6728997d789b
f45c4632c0d5d25901f125ad80b245e5bdf50f7f
f61e96564da25fff51dd3e764d471b9320937e4c
f72b5462f63489d3e37b03a9a7f778d5842f0620
f7ebb1938b694b81fa4be16f1bd191aeb30ab6be
fa80f05a68181f0bc64355a0f39e1d155a2f6fe0
fc0d46cc7c7ca6691326354d96a2940a5c5a85a8
fd13c5d5ad837eaf5a1588d1b1a08c79376dbee7
fdf9a313361032f5524bcbb6afd964b95c900415
ff19a25fd2ae104ad9bc5c9bb49cec698552bff2
ff4d244c254a1dbca345d139552df8e96a74d76d
```

## Notes

- This analysis is based on patch file metadata only
- Patches may have been modified when merged upstream
- Some patches might be split into multiple commits or combined
- The commit ID in a patch comes from the original source tree (e.g., vendor kernel)
- Manual verification is recommended for definitive confirmation
