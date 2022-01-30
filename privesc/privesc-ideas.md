# checklist

- linenum, linux-exploit-suggester, lynis, postenum, linux-smart-enumeration, linpeas
- check for easy passwords
- go back to port scan
- run programs which are in usuall places, maybe there is a bug
- are the hidden programs periodicaly running -> pspy
- read files via iframe: <iframe src='/root/.ssh/id_rsa'>

# permissions

## add user to group

```cmd
net localgroup <group> <user> /add
```

## set full permission to file

```cmd
CACLS file_path /e /p <user>:F
```
