# methodology
1. check all sites for usefull informations -> grep -iE "(user|password)" files
2. check all sites for usefull function
    - login
    - create account
    - forgot password
    - reset password
    - sqli
    - template injection
    - command injection
    - analyse webpage with zaproxy or via source-code view
3. reuse combination of users and passwords
4. CHECK EVERY FUCKING FUNCTION WITH SEARCHSPLOIT!!!
5. check password files from linpeas, linenum

# recon
sslscan --show-certificate "$rhost:443"
nikto -ask=no -h "http://$rhost$rport"
nth --text 'hash'
sth --text 'hash'
sqlmap --batch -a --forms -u "http://$rhost" --output-dir="."
sqlmap --batch -a --dump-all --forms -u "http://$rhost" --output-dir="."
cewl -d 5 -m 4 -w pot-password.txt --with-numbers -a -e "$rhost"
wpscan --url "http://$rhost$rport"
ftp $rhost             user: ftp, anonymous

# exploiting

## flaws
check if programs (with sui,gui) execute system commands without absolute path -> replace executable with binary in your path

## commands
use post/multi/manage/shell_to_meterpreter
hashcat -a 0 -m 0 hash.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
hashcat -a 0 -m 0 -r /usr/share/hashcat/rules/best64.rule hash.hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
find / -perm -u=s -type f 2> /dev/null
find / -perm -g=s -type f 2> /dev/null

## file upload
file upload could be exploited with a php, asp, jsp, coldfusion, flash, perl or yaws reverse shell

## webserver flaws create html
read files via iframe: <iframe src='/root/.ssh/id_rsa'>

# Stable shell
python3 -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
background; stty raw -echo && stty size; fg
stty rows 58 cols 212

