# crack hash.hash with plain wordlist

```
hashcat -O -a 0 -m 0 hash.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

# crach hash.hash with wordlist + ruleset

```
hashcat -O -a 0 -m 0 -r /usr/share/hashcat/rules/best64.rule hash.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

