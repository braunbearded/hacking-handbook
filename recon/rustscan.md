# full port scan

```
rustscan -a "$rhost" -- -A -sC -sV -sS --osscan-guess --version-all | tee rustscan-$rhost.txt
```

