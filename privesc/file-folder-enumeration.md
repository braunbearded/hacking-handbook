# linux victim

## find set group/user bit files

```bash
find / -perm -u=s -type f 2> /dev/null
find / -perm -g=s -type f 2> /dev/null
```

## search thru all binary with strings and grep

```bash
find . -type f | xargs strings | grep -i "passwo"
```

## list files which are modifyed by user

```bash
ls -lt --time-style=full-iso | grep -v "000000000"
find . -type f 2> /dev/null | xargs -I "{}" sh -c "stat -c '%n|%y' '{}' 2> /dev/null" | grep -v "000000000"
```

## interesting files

```bash
find / -name "*user*" -not \( -path "/proc/*" -or -path "/sys/*" -or -path "/usr/share/icons/*" -or -path "/usr/share/man/*" -or -path "/usr/share/locale/*" -or -path "/usr/share/help/*" -or -path "/usr/src/linux-headers*"  -or -path "/usr/share/help-langpack/*" -or -path "/var/lib/dpkg/info/*" -or -path "/usr/share/doc/*" -or -path "/usr/share/locale-langpack/*" -or -path "/var/lib/app-info/icons/*" \) 2> /dev/null
find / -user <user>
find / -mtime -60 # find files with are modified in last 60 days
find / -perm 0777
find / -type f -mmin -5 ! -path "/proc/*" ! -path "/sys/*" ! -path "/run/*" ! -path "/dev/*" ! -path "/var/lib/*" 2>/dev/null # edit in last 5min
find / -newermt "2020-08-13" 2> /dev/null
```

## find docker files

```bash
find / -type f -name "*env"
find / -type f -name "Dockerfile"
find / -type f -name "*docker-compose*"
```

## check files content

```bash
grep -ir "password" / 2> /dev/null
grep -ir "pass" / 2> /dev/null
grep -ir "username" / 2> /dev/null
grep -ir "user" / 2> /dev/null
grep -ir "comm=\"su" /var/log/audit
```

# windows victim

## list all files including hidden

```cmd
gci -Force
```

## list files matching regex (hide errors)

```cmd
gci -force -recurse -filter regex* -ErrorAction SilentlyContinue
```

## list folders (recursivly)

```cmd
dir <file*> /S /B
```

## files for automating windows installations

```cmd
dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml *unattend.txt 2>nul
```
