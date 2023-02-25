#!/bin/sh

for i in $(seq 1 255); do
	host "192.168.137.$i" some_dns | tr -d "\n" | grep -v "not found"
	echo ""
done
