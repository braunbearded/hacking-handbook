# linux attacker

## sub domain enum

```bash
amass enum -src -ip -passive -d <domain> -o output.txt
amass enum -src -ip -d <domain> -o output.txt
amass enum -src -ip -active -d <domain> -o output.txt
amass enum -d <domain> -active -brute -w /usr/share/seclists/Discovery/DNS/deepmagic.com-prefixes-top50000.txt
```

## vhost discovery with custom wordlist

```bash
ffuf -c -u "http://$rhost$rport" -w pot-vhosts.txt -o ffuf-vhost-$rhost.txt -od ffuf-vhost-$rhost -H "Host: FUZZ.$rhost" -fs <filter size>
```

## vhost discovery with default wordlist

```bash
rdomain="" ffuf_out="ffuf-vhost-$rdomain"; ffuf -c -u "http://$rhost" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -o "$ffuf_out/summary.txt" -od "$ffuf_out" -H "Host: FUZZ.$rdomain" -fs
```
