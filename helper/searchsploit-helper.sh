#!/bin/sh

[ "$1" = "" ] && echo "usage: spi 'some|regex'" && return
regex="$1"
exploits_path="/usr/share/exploitdb/exploits"
#arch="$(find "$exploits_path" -type d -not -path '*/dos' | cut -d '/' -f 6-)"

#selected_arch="$(echo "$arch" | fzf -m --cycle --prompt "Select architecture:")"
#echo "$selected_arch" | sed "s#^#$exploits_path/#" | tr '\n' ' '
#rg --no-heading '.' $(echo "$selected_arch" | sed "s#^#$exploits_path/#" | tr '\n' ' ') | sort -u | fzf -d '/' --with-nth '6..'

#find "$exploits_path" -type f -not -path '*/dos/*' | grep -E "$regex" | xargs -I '{}' sh -c 'printf "%s%s\n" "$(echo "{}" | cut -d "/" -f 6-)" "$(cat {} | tr "\n" " ")"' 2> /dev/null | fzf
selected="$(find "$exploits_path" -type f -not -path '*/dos/*' | grep -E "$regex" | xargs -I '{}' sh -c 'printf "%s:%s\n" "{}" "$(cat {} | tr "\n" " ")"' 2>/dev/null | fzf -d '/' --with-nth '6..' | cut -d ":" -f 1)"

if [ -f "$(basename "$selected")" ]; then
	cat "$selected"
	echo ""
	echo ""
	echo "##########################################################################################################"
	echo "Could not copy file $(echo "$selected" | cut -d '/' -f 5-) because it already exists in this directory!"
	echo "##########################################################################################################"
else
	cp "$selected" .
	cat "$selected"
	echo ""
	echo ""
	echo "##########################################################################################################"
	echo "File $(echo "$selected" | cut -d '/' -f 5-) was copied to current directory!"
	echo "##########################################################################################################"
fi
