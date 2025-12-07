#!/bin/bash
# Script to check if sunxi-6.16 patches are in Linux kernel 6.18
# Generated on 2025-12-07 04:17:42

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
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-cedrus-add-format-filtering-based-on-depth-and-src-format.patch"
    ((NOT_FOUND++))
fi

# media-Add-NV12-and-P010-AFBC-compressed-formats.patch
# Subject: media: Add NV12 and P010 AFBC compressed formats
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: media-Add-NV12-and-P010-AFBC-compressed-formats.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-Add-NV12-and-P010-AFBC-compressed-formats.patch"
    ((NOT_FOUND++))
fi

# media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch
# Subject: media: cedrus: Implement AFBC YUV420 formats for H265
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-cedrus-Implement-AFBC-YUV420-formats-for-H265.patch"
    ((NOT_FOUND++))
fi

# dma-sun6i-dma-add-sun50i-h616-support.patch
# Subject: dma: sun6i-dma: add sun50i-h616 support
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: dma-sun6i-dma-add-sun50i-h616-support.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: dma-sun6i-dma-add-sun50i-h616-support.patch"
    ((NOT_FOUND++))
fi

# media-cedrus-Increase-H6-clock-rate.patch
# Subject: media: cedrus: Increase H6 clock rate
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: media-cedrus-Increase-H6-clock-rate.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-cedrus-Increase-H6-clock-rate.patch"
    ((NOT_FOUND++))
fi

# media-cedrus-Don-t-CPU-map-source-buffers.patch
# Subject: media: cedrus: Don't CPU map source buffers
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: media-cedrus-Don-t-CPU-map-source-buffers.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-cedrus-Don-t-CPU-map-source-buffers.patch"
    ((NOT_FOUND++))
fi

# net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch
# Subject: net: stmmac: sun8i: Use devm_regulator_get for PHY regulator
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch"
    ((NOT_FOUND++))
fi

# mmc-add-delay-after-power-class-selection.patch
# Subject: mmc: add delay after power class selection
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: mmc-add-delay-after-power-class-selection.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: mmc-add-delay-after-power-class-selection.patch"
    ((NOT_FOUND++))
fi

# ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch
# Subject: ARM: dts: sun8i-a83t-tbs-a711: Add powerup/down support for the 3G
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch"
    ((NOT_FOUND++))
fi

# dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch
# Subject: dt-bindings: media: Add bindings for Himax HM5065 camera sensor
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch"
    ((NOT_FOUND++))
fi

# arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch
# Subject: arm64: dts: sun50i-a64-pinephone: Add support for modem audio
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch"
    ((NOT_FOUND++))
fi

# media-ov5640-Implement-autofocus.patch
# Subject: media: ov5640: Implement autofocus
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: media-ov5640-Implement-autofocus.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: media-ov5640-Implement-autofocus.patch"
    ((NOT_FOUND++))
fi

# power-supply-axp20x-battery-Improve-probe-error-reporting.patch
# Subject: power: supply: axp20x-battery: Improve probe error reporting
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: power-supply-axp20x-battery-Improve-probe-error-reporting.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: power-supply-axp20x-battery-Improve-probe-error-reporting.patch"
    ((NOT_FOUND++))
fi

# arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch
# Subject: arm64: dts: sun50i-a64-pinephone: Use newer jack detection
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: arm64-dts-sun50i-a64-pinephone-Use-newer-jack-detection-impleme.patch"
    ((NOT_FOUND++))
fi

# arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch
# Subject: arm64: dts: sun50i-a64-pinephone: Fix BH modem manager behavior
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch"
    ((NOT_FOUND++))
fi

# arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch
# Subject: arm64: dts: allwinner: h5: Enable hdmi sound card on boards with hdmi
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch"
    ((NOT_FOUND++))
fi

# dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch
# Subject: dt-bindings: input: gpio-vibrator: Don't require enable-gpios
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch"
    ((NOT_FOUND++))
fi

# dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch
# Subject: dt: bindings: mfd: Add codec related properties to AC100 PMIC
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: dt-bindings-mfd-Add-codec-related-properties-to-AC100-PMIC.patch"
    ((NOT_FOUND++))
fi

# power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch
# Subject: power: supply: axp20x-battery: Add support for
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
    ((FOUND++))
else
    echo "✗ NOT FOUND: power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch"
    ((NOT_FOUND++))
fi

# rtc-Print-which-error-caused-RTC-read-failure.patch
# Subject: rtc: Print which error caused RTC read failure
if git cat-file -t 0000000000000000000000000000000000000000 >/dev/null 2>&1; then
    echo "✓ FOUND: rtc-Print-which-error-caused-RTC-read-failure.patch"
    echo "  Commit: 0000000000000000000000000000000000000000"
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
