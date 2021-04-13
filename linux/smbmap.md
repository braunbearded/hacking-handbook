# login as guest to host

```
smbmap -u guest -H "$rhost"
```

# login as anonymous to host

```
smbmap -H "$rhost"
```

# print shares recursivly

```
smbmap -u <user> -p <password> -H <rhost> -R
```
