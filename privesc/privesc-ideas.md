# checklist

- linenum, linux-exploit-suggester, lynis, postenum, linux-smart-enumeration, linpeas
- check for easy passwords
- go back to port scan
- run programs which are in usuall places, maybe there is a bug
- are the hidden programs periodicaly running -> pspy
- read files via iframe: <iframe src='/root/.ssh/id_rsa'>

# interesting files

## search thru all binary with strings and grep

```bash
find . -type f | xargs strings | grep -i "passwo"
```

## list files which are modifyed by user

```bash
ls -lt --time-style=full-iso | grep -v "000000000"
find . -type f 2> /dev/null | xargs -I "{}" sh -c "stat -c '%n|%y' '{}' 2> /dev/null" | grep -v "000000000"
```

# permissions

## add user to group

```cmd
net localgroup <group> <user> /add
```

## set full permission to file

```cmd
CACLS file_path /e /p <user>:F
```
