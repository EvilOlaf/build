#!/bin/bash
# Script to check if sunxi-6.16 patches are in Linux kernel 6.18
# Generated on 2025-12-06 18:06:53

set -e

KERNEL_VERSION="6.18"
KERNEL_DIR="linux-$KERNEL_VERSION"

# Clone kernel if not exists
if [ ! -d "$KERNEL_DIR" ]; then
    echo "Cloning Linux kernel v$KERNEL_VERSION..."
    git clone --depth=1 --branch "v$KERNEL_VERSION" \
        https://github.com/torvalds/linux.git \
        "$KERNEL_DIR"
fi

cd "$KERNEL_DIR"

echo "Checking patches..."
echo ""

FOUND=0
NOT_FOUND=0

# Check patches by commit ID (444 patches)

# media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch
# Subject: media: cedrus: add format filtering based on depth and src format
if git cat-file -t be75f442cae72a4e646e1f5d7374f579ee026c3d >/dev/null 2>&1; then
    echo "✓ FOUND: media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch"
    echo "  Commit: be75f442cae72a4e646e1f5d7374f579ee026c3d"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch"
    ((NOT_FOUND++))
fi

# media-Add-NV12-and-P010-AFBC-compressed-formats.patch
# Subject: media: Add NV12 and P010 AFBC compressed formats
if git cat-file -t e43c6b985ac6d4f40a8e15526460c2d201d71407 >/dev/null 2>&1; then
    echo "✓ FOUND: media-Add-NV12-and-P010-AFBC-compressed-formats.patch"
    echo "  Commit: e43c6b985ac6d4f40a8e15526460c2d201d71407"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-Add-NV12-and-P010-AFBC-compressed-formats.patch"
    ((NOT_FOUND++))
fi

# media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch
# Subject: media: cedrus: Implement AFBC YUV420 formats for H265
if git cat-file -t 81241983ba12f281a839a530da460088170cca2e >/dev/null 2>&1; then
    echo "✓ FOUND: media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch"
    echo "  Commit: 81241983ba12f281a839a530da460088170cca2e"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch"
    ((NOT_FOUND++))
fi

# dma-sun6i-dma-add-sun50i-h616-support.patch
# Subject: dma: sun6i-dma: add sun50i-h616 support
if git cat-file -t 672717a70d3fa52c55aa222a011d27dff2756787 >/dev/null 2>&1; then
    echo "✓ FOUND: dma-sun6i-dma-add-sun50i-h616-support.patch"
    echo "  Commit: 672717a70d3fa52c55aa222a011d27dff2756787"
    ((FOUND++))
else
    echo "✗ NOT FOUND: dma-sun6i-dma-add-sun50i-h616-support.patch"
    ((NOT_FOUND++))
fi

# media-cedrus-Increase-H6-clock-rate.patch
# Subject: media: cedrus: Increase H6 clock rate
if git cat-file -t c0dffc32c3a65a1c25bf04f979faf8b6a82b88f8 >/dev/null 2>&1; then
    echo "✓ FOUND: media-cedrus-Increase-H6-clock-rate.patch"
    echo "  Commit: c0dffc32c3a65a1c25bf04f979faf8b6a82b88f8"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-cedrus-Increase-H6-clock-rate.patch"
    ((NOT_FOUND++))
fi

# media-cedrus-Don-t-CPU-map-source-buffers.patch
# Subject: media: cedrus: Don't CPU map source buffers
if git cat-file -t 80b16fcddf1837c631796c25f3123b7adbbf815a >/dev/null 2>&1; then
    echo "✓ FOUND: media-cedrus-Don-t-CPU-map-source-buffers.patch"
    echo "  Commit: 80b16fcddf1837c631796c25f3123b7adbbf815a"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-cedrus-Don-t-CPU-map-source-buffers.patch"
    ((NOT_FOUND++))
fi

# net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch
# Subject: net: stmmac: sun8i: Use devm_regulator_get for PHY regulator
if git cat-file -t 41d867cddaf5e97ec163019d673ae15e184beea3 >/dev/null 2>&1; then
    echo "✓ FOUND: net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch"
    echo "  Commit: 41d867cddaf5e97ec163019d673ae15e184beea3"
    ((FOUND++))
else
    echo "✗ NOT FOUND: net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch"
    ((NOT_FOUND++))
fi

# mmc-add-delay-after-power-class-selection.patch
# Subject: mmc: add delay after power class selection
if git cat-file -t cc541c517e0dea4d8d362980eff9f3d2283ffbdb >/dev/null 2>&1; then
    echo "✓ FOUND: mmc-add-delay-after-power-class-selection.patch"
    echo "  Commit: cc541c517e0dea4d8d362980eff9f3d2283ffbdb"
    ((FOUND++))
else
    echo "✗ NOT FOUND: mmc-add-delay-after-power-class-selection.patch"
    ((NOT_FOUND++))
fi

# ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch
# Subject: ARM: dts: sun8i-a83t-tbs-a711: Add powerup/down support for the 3G
if git cat-file -t 5b1f89dbd335917afc7e2f63467562509eabf4d7 >/dev/null 2>&1; then
    echo "✓ FOUND: ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch"
    echo "  Commit: 5b1f89dbd335917afc7e2f63467562509eabf4d7"
    ((FOUND++))
else
    echo "✗ NOT FOUND: ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch"
    ((NOT_FOUND++))
fi

# dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch
# Subject: dt-bindings: media: Add bindings for Himax HM5065 camera sensor
if git cat-file -t 34bcb830ea7b7a2a835604050fe3502f29951a9e >/dev/null 2>&1; then
    echo "✓ FOUND: dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch"
    echo "  Commit: 34bcb830ea7b7a2a835604050fe3502f29951a9e"
    ((FOUND++))
else
    echo "✗ NOT FOUND: dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch"
    ((NOT_FOUND++))
fi

# arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch
# Subject: arm64: dts: sun50i-a64-pinephone: Add support for modem audio
if git cat-file -t d33975afbcf46a53258f1ed2f4f5602d7b1ccfaa >/dev/null 2>&1; then
    echo "✓ FOUND: arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch"
    echo "  Commit: d33975afbcf46a53258f1ed2f4f5602d7b1ccfaa"
    ((FOUND++))
else
    echo "✗ NOT FOUND: arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch"
    ((NOT_FOUND++))
fi

# media-ov5640-Implement-autofocus.patch
# Subject: media: ov5640: Implement autofocus
if git cat-file -t 639e94cc1789aa3841edefb3846c97059479b1fd >/dev/null 2>&1; then
    echo "✓ FOUND: media-ov5640-Implement-autofocus.patch"
    echo "  Commit: 639e94cc1789aa3841edefb3846c97059479b1fd"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-ov5640-Implement-autofocus.patch"
    ((NOT_FOUND++))
fi

# power-supply-axp20x-battery-Improve-probe-error-reporting.patch
# Subject: power: supply: axp20x-battery: Improve probe error reporting
if git cat-file -t c527915eb794fac0a75fce1fa096e2133050e25b >/dev/null 2>&1; then
    echo "✓ FOUND: power-supply-axp20x-battery-Improve-probe-error-reporting.patch"
    echo "  Commit: c527915eb794fac0a75fce1fa096e2133050e25b"
    ((FOUND++))
else
    echo "✗ NOT FOUND: power-supply-axp20x-battery-Improve-probe-error-reporting.patch"
    ((NOT_FOUND++))
fi

# arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch
# Subject: arm64: dts: sun50i-a64-pinephone: Use newer jack detection
if git cat-file -t f1a9b4f7e3a451514b09daa50b43494f8f86612c >/dev/null 2>&1; then
    echo "✓ FOUND: arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch"
    echo "  Commit: f1a9b4f7e3a451514b09daa50b43494f8f86612c"
    ((FOUND++))
else
    echo "✗ NOT FOUND: arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch"
    ((NOT_FOUND++))
fi

# arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch
# Subject: arm64: dts: sun50i-a64-pinephone: Fix BH modem manager behavior
if git cat-file -t 6945687a57dff96300080ec1edb2df467f376050 >/dev/null 2>&1; then
    echo "✓ FOUND: arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch"
    echo "  Commit: 6945687a57dff96300080ec1edb2df467f376050"
    ((FOUND++))
else
    echo "✗ NOT FOUND: arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch"
    ((NOT_FOUND++))
fi

# arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch
# Subject: arm64: dts: allwinner: h5: Enable hdmi sound card on boards with hdmi
if git cat-file -t cf056f9d1d534ffae9793137b755214549cdb572 >/dev/null 2>&1; then
    echo "✓ FOUND: arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch"
    echo "  Commit: cf056f9d1d534ffae9793137b755214549cdb572"
    ((FOUND++))
else
    echo "✗ NOT FOUND: arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch"
    ((NOT_FOUND++))
fi

# dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch
# Subject: dt-bindings: input: gpio-vibrator: Don't require enable-gpios
if git cat-file -t 98a5484643843d4e6fceadc7c8cfa54c512bd7d6 >/dev/null 2>&1; then
    echo "✓ FOUND: dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch"
    echo "  Commit: 98a5484643843d4e6fceadc7c8cfa54c512bd7d6"
    ((FOUND++))
else
    echo "✗ NOT FOUND: dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch"
    ((NOT_FOUND++))
fi

# dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch
# Subject: dt: bindings: mfd: Add codec related properties to AC100 PMIC
if git cat-file -t 6745aeb621323a7d0b1022730c8ab32e4203520a >/dev/null 2>&1; then
    echo "✓ FOUND: dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch"
    echo "  Commit: 6745aeb621323a7d0b1022730c8ab32e4203520a"
    ((FOUND++))
else
    echo "✗ NOT FOUND: dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch"
    ((NOT_FOUND++))
fi

# power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch
# Subject: power: supply: axp20x-battery: Add support for
if git cat-file -t dc52e71a420ed1baba6c504500d62806f72c5092 >/dev/null 2>&1; then
    echo "✓ FOUND: power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch"
    echo "  Commit: dc52e71a420ed1baba6c504500d62806f72c5092"
    ((FOUND++))
else
    echo "✗ NOT FOUND: power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch"
    ((NOT_FOUND++))
fi

# rtc-Print-which-error-caused-RTC-read-failure.patch
# Subject: rtc: Print which error caused RTC read failure
if git cat-file -t d92e4969a270a358d68542495a37a67f4f8e4484 >/dev/null 2>&1; then
    echo "✓ FOUND: rtc-Print-which-error-caused-RTC-read-failure.patch"
    echo "  Commit: d92e4969a270a358d68542495a37a67f4f8e4484"
    ((FOUND++))
else
    echo "✗ NOT FOUND: rtc-Print-which-error-caused-RTC-read-failure.patch"
    ((NOT_FOUND++))
fi

# ... 424 more patches with commit IDs
# (edit this script to check all of them)


echo ""
echo "Summary:"
echo "  Found: $FOUND"
echo "  Not found: $NOT_FOUND"
