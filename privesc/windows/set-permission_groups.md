# add user to group

```cmd
net localgroup <group> <user> /add
```

# set full permission to file

```cmd
CACLS file_path /e /p <user>:F
```
