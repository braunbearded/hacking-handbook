# linux attacker

## full port scan

```bash
rustscan -a "$rhost" -- -A -sC -sV -sS --osscan-guess --version-all | tee rustscan-$rhost.txt
```

## full port scan (scan open tcp with udp aswell)

```bash
rustscan -a "$rhost" -- -A -sC -sV -sS -sU --osscan-guess --version-all | tee rustscan-$rhost.txt
```

## full port scan (udp and tcp) + save nmap output

```bash
mkdir -p nmap-$rhost && rustscan -a "$rhost" -- -A -sC -sV -sS -sU --osscan-guess --version-all -oA nmap-$rhost/fullscan
```

## searchsploit with nmap scan

```bash
searchsploit --nmap portscan.xml
```

## fast udp scan top1000

```bash
nmap -v -Pn -sU --max-retries 1 --max-scan-delay 1 --version-intensity 0 "$rhost" -oA "nmap-$rhost/top1000-udp"
```
