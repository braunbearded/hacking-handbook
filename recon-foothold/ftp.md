# linux attacker

## standard ftp

Users to check:

- anonymous
- ftp
- root
- admin
- administrator

```bash
ftp $rhost
ftp "user@$rhost"
```

## download all ftp files

```bash
lftp -u <user> $rhost
mirror # download all files
```
