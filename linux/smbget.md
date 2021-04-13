# download all files from smb share as Anonymous

```
smbget -R smb://<rhost>/<share> -U Anonymous
```

# download all files from smb share as user + password

```
smbget -R smb://<rhost>/share/ -U <User>%<Password>
```
