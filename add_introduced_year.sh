#!/bin/bash

# Script to add INTRODUCED variable to board configuration files
# The INTRODUCED year is extracted from the git creation date of the file

BOARD_DIR="config/boards"

# Find all board configuration files (.conf, .csc, .wip, .tvb)
for board_file in "$BOARD_DIR"/*.{conf,csc,wip,tvb}; do
	# Skip if glob didn't match anything
	[[ -f "$board_file" ]] || continue

	echo "Processing: $board_file"

	# Get the creation date from git (with --follow to track renames)
	creation_date=$(git log --diff-filter=A --format="%ai" --follow -- "$board_file" 2>/dev/null | head -1)

	if [[ -z "$creation_date" ]]; then
		echo "  Warning: No git history found, skipping"
		continue
	fi

	# Extract the year (first 4 characters of the date)
	introduced_year="${creation_date:0:4}"

	echo "  Introduced year: $introduced_year"

	# Check if INTRODUCED already exists
	if grep -q "^INTRODUCED=" "$board_file"; then
		echo "  INTRODUCED already exists, skipping"
		continue
	fi

	# Find the line number of the description comment (first line starting with #)
	desc_line=$(grep -n "^#" "$board_file" | cut -d: -f1 | head -1)

	if [[ -z "$desc_line" ]]; then
		echo "  Warning: No description comment found, skipping"
		continue
	fi

	# Insert INTRODUCED after the description comment
	# Using sed to insert after the description line
	sed -i "${desc_line}a INTRODUCED=$introduced_year" "$board_file"

	echo "  Added INTRODUCED=$introduced_year after line $desc_line"
done

echo ""
echo "Done!"
