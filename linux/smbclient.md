# list shares

```
smbclient -L <computer-name/ip>
```

# connect as anonymous (dont ask for pw)

```
smbclient -N //"$rhost"/SomeDir
```

# connect as guest

```
smbclient -U guest //"$rhost"/SomeDir
```

# recursive download via smbclient

1. connect
2. cd folder
3. type: mask
4. type: recurse
5. type: prompt
6. mget *

