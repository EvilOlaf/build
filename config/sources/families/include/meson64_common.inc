#
# SPDX-License-Identifier: GPL-2.0
#
# Copyright (c) 2013-2023 Igor Pecovnik, igor@armbian.com
#
# This file is a part of the Armbian Build Framework
# https://github.com/armbian/build/
#
UBOOT_TARGET_MAP="${UBOOT_TARGET_MAP:-u-boot-dtb.img;;u-boot.bin.sd.bin:u-boot.bin u-boot-dtb.img}"
BOOTSCRIPT="boot-meson64.cmd:boot.cmd"
BOOTENV_FILE='meson.txt'
LINUXFAMILY=meson64
ARCH=arm64
SERIALCON=ttyAML0
SRC_LOADADDR='LOADADDR=0x1080000'
BOOTBRANCH="${BOOTBRANCH_BOARD:-"tag:v2022.07"}"
BOOTPATCHDIR="${BOOTPATCHDIR:-"v2022.07"}"
OVERLAY_PREFIX='meson'
OVERLAY_DIR="/boot/dtb/amlogic/overlay"

# This is an extension method, put directly in meson64_common. A "built-in" extension if you will.
# Bring in LibreELEC's amlogic-boot-fip repo, which is the authoritative source for FIP blobs.
# To add FIP blobs for a new board, send a PR there, they're awesome.
function fetch_sources_tools__libreelec_amlogic_fip() {
	fetch_from_repo "https://github.com/LibreELEC/amlogic-boot-fip" "amlogic-boot-fip" "branch:master"
}

# this family does not need it
ATF_COMPILE="no"

# Set CPUMIN et al if not already set in the board config.
CPUMIN=${CPUMIN:-500000}
CPUMAX=${CPUMAX:-1536000}
GOVERNOR=${GOVERNOR:-ondemand}

case $BRANCH in

	current)
		declare -g KERNEL_MAJOR_MINOR="6.12"
		;;
	edge)
		declare -g KERNEL_MAJOR_MINOR="6.15"
		;;

esac

# Use custom vendor driver for wireless rtl88x2cs
# See https://github.com/armbian/build/pull/6227
# @TODO Only use for BOARDFAMILY="jethub" devices?
function custom_kernel_config__enable_rtl88x2cs_driver() {
	kernel_config_modifying_hashes+=("CONFIG_RTL8822CS=m")
	if [[ -f .config ]]; then
		display_alert "Enabling rtl88x2cs driver in kernel config" "armbian-kernel" "wrn"
		kernel_config_set_m CONFIG_RTL8822CS
	fi
}

# this helper function includes postprocess for s400 and its variants.
# $1 PATH for uboot blob repo
# $2 dir name in uboot blob repo
uboot_axg_postprocess_ng() {
	run_host_command_logged mv -v u-boot.bin bl33.bin

	run_host_command_logged $1/blx_fix.sh $1/$2/bl30.bin \
		$1/$2/zero_tmp \
		$1/$2/bl30_zero.bin \
		$1/$2/bl301.bin \
		$1/$2/bl301_zero.bin \
		$1/$2/bl30_new.bin bl30

	run_host_command_logged python3 $1/acs_tool.py $1/$2/bl2.bin \
		$1/$2/bl2_acs.bin \
		$1/$2/acs.bin 0

	run_host_command_logged $1/blx_fix.sh $1/$2/bl2_acs.bin \
		$1/$2/zero_tmp \
		$1/$2/bl2_zero.bin \
		$1/$2/bl21.bin \
		$1/$2/bl21_zero.bin \
		$1/$2/bl2_new.bin bl2

	run_host_x86_binary_logged $1/$2/aml_encrypt_axg --bl3sig --input $1/$2/bl30_new.bin \
		--output bl30_new.bin.enc \
		--level v3 --type bl30

	run_host_x86_binary_logged $1/$2/aml_encrypt_axg --bl3sig --input $1/$2/bl31.img \
		--output bl31.img.enc \
		--level v3 --type bl31

	run_host_x86_binary_logged $1/$2/aml_encrypt_axg --bl3sig --input bl33.bin --compress lz4 \
		--output bl33.bin.enc \
		--level v3 --type bl33

	run_host_x86_binary_logged $1/$2/aml_encrypt_axg --bl2sig --input $1/$2/bl2_new.bin \
		--output bl2.n.bin.sig

	run_host_x86_binary_logged $1/$2/aml_encrypt_axg --bootmk \
		--output u-boot.bin \
		--bl2 bl2.n.bin.sig \
		--bl30 bl30_new.bin.enc \
		--bl31 bl31.img.enc \
		--bl33 bl33.bin.enc --level v3
}

# this helper function includes postprocess for u200 and its variants.
# $1 PATH for uboot blob repo
# $2 family g12a or g12b
uboot_g12_postprocess() {
	run_host_command_logged mv -v u-boot.bin bl33.bin

	run_host_command_logged $1/blx_fix.sh $1/bl30.bin \
		zero_tmp \
		bl30_zero.bin \
		$1/bl301.bin \
		bl301_zero.bin \
		bl30_new.bin bl30

	run_host_command_logged $1/blx_fix.sh $1/bl2.bin \
		zero_tmp \
		bl2_zero.bin \
		$1/acs.bin \
		bl21_zero.bin \
		bl2_new.bin bl2

	run_host_x86_binary_logged $1/aml_encrypt_$2 --bl30sig \
		--input bl30_new.bin \
		--output bl30_new.bin.g12.enc \
		--level v3
	run_host_x86_binary_logged $1/aml_encrypt_$2 --bl3sig \
		--input bl30_new.bin.g12.enc \
		--output bl30_new.bin.enc \
		--level v3 --type bl30
	run_host_x86_binary_logged $1/aml_encrypt_$2 --bl3sig \
		--input $1/bl31.img \
		--output bl31.img.enc \
		--level v3 --type bl31
	run_host_x86_binary_logged $1/aml_encrypt_$2 --bl3sig \
		--input bl33.bin \
		--compress lz4 \
		--output bl33.bin.enc \
		--level v3 --type bl33
	run_host_x86_binary_logged $1/aml_encrypt_$2 --bl2sig \
		--input bl2_new.bin \
		--output bl2.n.bin.sig
	if [ -e $1/lpddr3_1d.fw ]; then
		run_host_x86_binary_logged $1/aml_encrypt_$2 --bootmk --output u-boot.bin \
			--bl2 bl2.n.bin.sig \
			--bl30 bl30_new.bin.enc \
			--bl31 bl31.img.enc \
			--bl33 bl33.bin.enc \
			--ddrfw1 $1/ddr4_1d.fw \
			--ddrfw2 $1/ddr4_2d.fw \
			--ddrfw3 $1/ddr3_1d.fw \
			--ddrfw4 $1/piei.fw \
			--ddrfw5 $1/lpddr4_1d.fw \
			--ddrfw6 $1/lpddr4_2d.fw \
			--ddrfw7 $1/diag_lpddr4.fw \
			--ddrfw8 $1/aml_ddr.fw \
			--ddrfw9 $1/lpddr3_1d.fw \
			--level v3
	else
		run_host_x86_binary_logged $1/aml_encrypt_$2 --bootmk --output u-boot.bin \
			--bl2 bl2.n.bin.sig \
			--bl30 bl30_new.bin.enc \
			--bl31 bl31.img.enc \
			--bl33 bl33.bin.enc \
			--ddrfw1 $1/ddr4_1d.fw \
			--ddrfw2 $1/ddr4_2d.fw \
			--ddrfw3 $1/ddr3_1d.fw \
			--ddrfw4 $1/piei.fw \
			--ddrfw5 $1/lpddr4_1d.fw \
			--ddrfw6 $1/lpddr4_2d.fw \
			--ddrfw7 $1/diag_lpddr4.fw \
			--ddrfw8 $1/aml_ddr.fw \
			--level v3
	fi

}

# this helper function includes postprocess for meson gxl and gxm.
# $1 PATH for uboot blob repo
uboot_gxl_postprocess_ng() {
	run_host_command_logged mv -v u-boot.bin bl33.bin

	run_host_command_logged $1/blx_fix.sh $1/bl30.bin \
		$1/zero_tmp \
		$1/bl30_zero.bin \
		$1/bl301.bin \
		$1/bl301_zero.bin \
		$1/bl30_new.bin bl30

	run_host_command_logged python3 $1/acs_tool.py $1/bl2.bin $1/bl2_acs.bin $1/acs.bin 0

	run_host_command_logged $1/blx_fix.sh $1/bl2_acs.bin \
		$1/zero_tmp \
		$1/bl2_zero.bin \
		$1/bl21.bin \
		$1/bl21_zero.bin \
		$1/bl2_new.bin bl2

	run_host_command_logged $1/aml_encrypt_gxl --bl3enc --input $1/bl30_new.bin
	run_host_command_logged $1/aml_encrypt_gxl --bl3enc --input $1/bl31.img
	run_host_command_logged $1/aml_encrypt_gxl --bl3enc --input bl33.bin
	run_host_command_logged $1/aml_encrypt_gxl --bl2sig --input $1/bl2_new.bin \
		--output bl2.n.bin.sig

	run_host_command_logged $1/aml_encrypt_gxl --bootmk --output u-boot.bin \
		--bl2 bl2.n.bin.sig \
		--bl30 $1/bl30_new.bin.enc \
		--bl31 $1/bl31.img.enc \
		--bl33 bl33.bin.enc
}

write_uboot_platform() {
	dd if=$1/u-boot.bin of=$2 bs=1 count=442 conv=fsync 2>&1
	dd if=$1/u-boot.bin of=$2 bs=512 skip=1 seek=1 conv=fsync 2>&1
}

family_tweaks_bsp() {
	mkdir -p $destination/etc/udev/rules.d
	mkdir -p $destination/usr/local/bin

	mkdir -p "$destination"/etc/X11/xorg.conf.d
	case "${BOARD}" in
		"odroidc2" | "nanopik2-s905" | "lepotato" | "sweet-potato" | "lafrite" | "khadas-vim1" | "khadas-vim2" | "aml-c400-plus" | "aml-s9xx-box")
			cat <<- EOF > "$destination"/etc/X11/xorg.conf.d/02-driver.conf
				Section "OutputClass"
				    Identifier "Amlogic"
				    MatchDriver "meson"
				    Driver "modesetting"
				    Option "PrimaryGPU" "true"
				EndSection
				Section "Screen"
				    Identifier      "Default Screen"
				    Device          "Meson"
				    Monitor         "foo"
				    DefaultDepth  24
				    SubSection "Display"
				       Depth    24
				       Modes    "1920x1080" "1440x900" "1280x720" "1280x1024" "1280x960" "1024x768" "800x600" "640x480" "720x400"
				    EndSubSection
				EndSection
			EOF
			;;
		"jethubj200" | "odroidn2" | "odroidc4" | "khadas-vim2" | "odroidhc4" | "khadas-vim3" | "khadas-vim3l" | "radxa-zero" | "radxa-zero2" | "bananapi-m2s")
			cat <<- EOF > "$destination"/etc/X11/xorg.conf
				Section "Device"
				    Identifier  "DRM Graphics Acclerated"

				    ## Use modesetting and glamor
				        Driver      "modesetting"
				        Option      "AccelMethod"    "glamor"     ### "glamor" to enable 3D acceleration, "none" to disable.
				        Option      "DRI"            "2"
				        Option      "Dri2Vsync"      "true"
				        Option      "TripleBuffer"   "True"
				    ## End glamor configuration

				    EndSection

				    Section "Screen"
				        Identifier "Default Screen"
				            SubSection "Display"
				                Depth 24
				            EndSubSection
				        EndSection
			EOF
			;;
	esac
}
