# extract hash from password protected zip file

```bash
john2zip <file.zip> > zip.hash
```

# crack hash with wordlist

```bash
john file.hash --wordlist=/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

# extend wordlist with ruleset

```bash
john ---wordlist=wordlist.txt --rules --stdout > wordlist-with-rules.txt
```

# crack passwd shadow password

```bash
unshadow passwd_file shadow_file > shadow.hash
john --wordlist=/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt shadow.hash
```

# crack kerberos golden ticket 

```bash
john --format=krb5tgs --wordlist=/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt tgs.txt
```

# crack ntlm hash

```bash
john --format=NT --wordlist=/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt ntlm.hash
```
