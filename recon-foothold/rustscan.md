# linux attacker

## full port scan

```bash
rustscan -a "$rhost" -- -A -sC -sV -sS --osscan-guess --version-all | tee rustscan-$rhost.txt
```

## full port scan (scan open tcp with udp aswell)

```bash
rustscan -a "$rhost" -- -A -sC -sV -sS -sU --osscan-guess --version-all | tee rustscan-$rhost.txt
```
