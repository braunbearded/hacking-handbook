# extract hash from password protected zip file

```bash
john2zip <file.zip> > zip.hash
```

# crack hash with wordlist

```bash
john file.hash --wordlist=/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```