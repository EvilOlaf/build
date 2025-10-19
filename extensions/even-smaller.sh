declare -g BUILD_MINIMAL=yes

function extension_prepare_config__slim() {
	display_alert "Extension: ${EXTENSION}: Adding image suffix" "-slim" "info"
	EXTRA_IMAGE_SUFFIXES+=("-slim")

	display_alert "Extension: ${EXTENSION}: Stripping unneeded packages" "from aggregated list" "info"
	PACKAGES_STRIP=("alsa-utils" "bash-completion" "bc" "dosfstools" "figlet" "htop" "lsof" "jq" "man-db" "nano" "openssh-server" "psmisc" "rsyslog" "toilet" "wget" "wireguard-tools")
	remove_packages "${PACKAGES_STRIP[@]}"

	display_alert "Extension: ${EXTENSION}: Adding packages to aggregated list" "dropbear" "info"
	PACKAGES_ADD=("dropbear")
	add_packages_to_rootfs "${PACKAGES_ADD[@]}"
}

function post_post_debootstrap_tweaks__slim_remove_packages() {
	display_alert "Extension: ${EXTENSION}: Removing forcefully installed packages" "again" "info"
	chroot_sdcard apt-get remove --purge -y rfkill bluetooth bluez bluez-tools armbian-config whiptail device-tree-compiler fping libfdt1 gpgconf gpg
	chroot_sdcard apt autoremove --purge -y
}