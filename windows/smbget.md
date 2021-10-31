# download all files from smb share as Anonymous

```bash
smbget -R smb://<rhost>/<share> -U Anonymous
```

# download all files from smb share as user + password

```bash
smbget -R smb://<rhost>/share/ -U <User>%<Password>
```
