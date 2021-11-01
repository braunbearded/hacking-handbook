# check reg

```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

If they are "0x1" you can install an .msi file as NT AUTHORITY\System

# reverse shell

check msfvenom in general to generate msi reverse shell
