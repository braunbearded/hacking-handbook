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
```

## improved ftp

```bash
lftp -u <user> $rhost
mget * # download all files
```
