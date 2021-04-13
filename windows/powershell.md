# folder enumeration

# list all files including hidden

```
gci -Force                                                       # list all files (also hidden)
```

# list files matching regex (hide errors)

```
gci -force -recurse -filter regex* -ErrorAction SilentlyContinue # list all files matching regex* and hide errors (permission denied)
```

