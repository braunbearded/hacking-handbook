#!/bin/sh

[ "$1" = "" ] && echo "Usage: shell-port-scanner <ip/dns>" && return

host="$1"
for port in $(seq 1 65535); do
    timeout .1 bash -c "echo >/dev/tcp/$host/$port" &&
        echo "$port is open"
done
echo "Scanning of $host finished"
