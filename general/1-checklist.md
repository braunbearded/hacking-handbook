# passiv

- create wordlist with osint, domain specific language

# general

- check every open port at least once manualy!!!
- searchsploit for technologies used
- msfconsole search for technologies used
- search for alternatives to programs
- check hacktricks for ports
- try software, service and other words as user and password
- run programs which are in unusual places, maybe there is a bug
- check application dir for configs, enviroments and other important files
- check if you are in an container (lxc, docker)
- check if other exploits with lower or higher version number works

# CVE

- check https://github.com/nomi-sec/PoC-in-GitHub

# portscan

- reset box/rerun scan
- check nmap scripts: /usr/share/nmap/scripts/
- udp
- adjust scan speed espeacialy when running a udp scan

# bruteforce/discovery/cracking

- create custom wordlists with stuff like users, shares, company jargon and cewl
- bruteforce/discover every service with your custom wordlist
- crack hashes offline and online (with sth etc)

# shares/ftp

- check folders(names) in ftp/samba also on webservers or other services

# webservers

- urlencode your shit
- check special path like http://localhost:3000/~user/file
- check website with zaproxy/burp
    - intercept redirects
- check for usefull web functionality
    - login
    - create account
    - forgot password
    - reset password
- check special header like
    - X-Originating-IP: 127.0.0.1
    - X-Forwarded-For: 127.0.0.1
    - X-Remote-IP: 127.0.0.1
    - X-Remote-Addr: 127.0.0.1
- bruteforce
    - username (with login form)
    - virtual hosts
    - generate wordlist with cewl
- check for sqli/nosqli
- does the site contains any relevant infos (e.g. domains) -> use this for registing users or any other functionality
- check vhost
- check ssl
- read files via iframe: <iframe src='/root/.ssh/id_rsa'>
- nikto
- find which programming language is used
- check if templating engine is used
- check the size of every valid response
- check every url, param, input field, post request
- check for command injection, ssrf, xss, lfi (e.g. localhost), rfi, path traversal, xxe, xpath
- check for predictable ids
- check if the webserver is connected to any other service
- check if different proxys are used
- check cookie
- bruteforce with custom wordlist (e.g. cewl)

# database

- use keywords from other sources like shares, webpage
- check sql injection
- check nosql injection

# bof

- encode payload

# linux

- check for hidden programs that run periodicaly (pspy) or service on local only
- sudo -l
- which files are writeable
- check /var/crash for core dumps
- test every credential with su
- run linenum, linux-exploit-suggester, linpeas

# windows

- check kernel exploits: https://github.com/SecWiki/windows-kernel-exploits
- run wesng
- run winPEAS
- check common priv esc tricks: https://book.hacktricks.xyz/windows/windows-local-privilege-escalation https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md

# smb

- run enum4linux, enumsmb, special nmap scan
- check for printnightmare, ethernalblue
- check permission for folders and if possible upload a file
- capture ntlm hash (ntlm_theft)

# todo
- lynis, postenum, linux-smart-enumeration
