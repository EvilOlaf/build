declare -g BUILD_MINIMAL=yes

function extension_prepare_config__slim {
	EXTRA_IMAGE_SUFFIXES+=("-slim")

	PACKAGES_STRIP=("alsa-utils" "bash-completion" "bc" "dosfstools" "figlet" "htop" "lsof" "jq" "man-db" "nano" "openssh-server" "psmisc" "rsyslog" "toilet" "wget" "wireguard-tools")
	remove_packages "${PACKAGES_STRIP[@]}"

	PACKAGES_ADD=("dropbear")
	add_packages_to_rootfs "${PACKAGES_ADD[@]}"
}
