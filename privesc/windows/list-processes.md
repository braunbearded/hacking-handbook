# list running processes with username

Requires admin permission:

```cmd
Get-Process -IncludeUserName | Select-Object Id,Name,Username,Path | Format-List
```
