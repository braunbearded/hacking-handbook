# folder enumeration

# list all files including hidden

```
gci -Force                                                       # list all files (also hidden)
```

# list files matching regex (hide errors)

```
gci -force -recurse -filter regex* -ErrorAction SilentlyContinue # list all files matching regex* and hide errors (permission denied)
```

# copy directory with content

```powershell
copy-item -force -recurse <source> <dest>
```

# list running processes with username 2

Requires admin permission:

```powershell
Get-Process -IncludeUserName | Select-Object Id,Name,Username,Path | Format-List
```

# curl webrequest

```powershell
(Invoke-WebRequest 'http://www.example.org/').Content
```

# listing ports

```powershell
netstat -a
```
