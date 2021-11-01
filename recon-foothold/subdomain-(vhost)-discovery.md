# linux attacker

## sub domain enum

```bash
amass enum -src -ip -passive -d <domain> -o output.txt
amass enum -src -ip -d <domain> -o output.txt
amass enum -src -ip -active -d <domain> -o output.txt
amass enum -d <domain> -active -brute -w /usr/share/seclists/Discovery/DNS/deepmagic.com-prefixes-top50000.txt
```

## vhost

```bash
ffuf -c -u "http://$rhost$rport" -w pot-vhosts.txt -o ffuf-vhost-$rhost.txt -od ffuf-vhost-$rhost -H "Host: FUZZ.$rhost" -fs <filter size>
```

