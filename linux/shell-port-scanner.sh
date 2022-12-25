#!/bin/sh

[ "$1" = "" ] && echo "Usage: shell-port-scanner <ip/dns>" && return

host="$1"
for port in $(seq 1 65535); do
	echo "Testing port $port..."
	timeout .1 bash -c "echo >/dev/tcp/$host/$port" 2>/dev/null &&
		echo "$port is open"
done
echo "Scanning of $host finished"
