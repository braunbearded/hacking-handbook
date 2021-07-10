# search thru all binary with strings and grep

```bash
find . -type f | xargs strings | grep -i "passwo"
```

# list files which are modifyed by user

```bash
ls -lt --time-style=full-iso | grep -v "000000000"
find . -type f 2> /dev/null | xargs -I "{}" sh -c "stat -c '%n|%y' '{}' 2> /dev/null" | grep -v "000000000"
```
