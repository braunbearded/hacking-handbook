# crack hash.hash with plain wordlist

Long password will be ignored with -O flag!

```bash
hashcat -O -a 0 -m 0 hash.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

# crack hash.hash with plain wordlist (unix password)

Long password will be ignored with -O flag!

```bash
hashcat -O -a 0 -m 500 hash.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

# crack hash.hash with wordlist + ruleset

Long password will be ignored with -O flag!

```bash
hashcat -O -a 0 -m 0 -r /usr/share/hashcat/rules/best64.rule hash.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

# crack ntlm with wordlist

Long password will be ignored with -O flag!

LM hash length:   17
NTLM hash length: 33

```bash
hashcat -O -a 0 -m 1000 ntlm.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

# crack ntlm2 with wordlist

Long password will be ignored with -O flag!

LM hash length:   17
NTLM hash length: 33

```bash
cat ntlm.hash
some.user::domainOrHost:LMHASH:NTLMHASH:0010101stuff...011010

hashcat -O -a 0 -m 5600 ntlm.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

# show cracked passwords

add option `--show` to previous command
