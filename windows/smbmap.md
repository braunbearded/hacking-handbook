# login as guest to host

```bash
smbmap -u guest -H "$rhost"
```

# login as anonymous to host

```bash
smbmap -H "$rhost"
```

# print shares recursivly

```bash
smbmap -u <user> -p <password> -H <rhost> -R
```
