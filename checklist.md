# checklist

1. passiv
  1. Did you get any information like names, company, positions, software, etc. -> create a wordlist

2. port scan
  1. full tcp portscan
  2. full udp portscan
  3. Did you wait long enought so that every service have time to start up
  4. Do you know what every port does? 
  5. Did you check searchsploit for every service?
  6. Did you google every service version for vulnerbilities?

3. hostname
  1. Did you find any hostname -> put in /etc/hosts

4. general
  1. did you check hacking tricks for ports?
  99. check https://github.com/nomi-sec/PoC-in-GitHub

5. web server
  1. Does the server respect vhosts?
    1. Bruteforce common sub domains
    2. content discovery for every vhost
  2. Check ssl certificate 
  3. content discovery with default wordlist
  4. nikto
  5. Do you know what function the webapp provide?
  6. Do you know what programming language was used?
  7. Does it have a backend ?
  8. Does it connect to a database? If so which ? -> SQL injection, NOSQL injection
  9. Is a popular CMS used?
    1. use cms scanner (wpcan)
    2. searchsploit theme, plugin and cms version
    3. google theme, plugin and cms version
  10. Does it do templating ? Which templating engine is used ? -> template injection
  11. Can you reuse credentials? Check default creds
  12. Does it contain alot of content? -> create wordlist (cewl)
  13. Did you check the size of every valid response? Maybe there is a html comment.
  14. Did you check every url, param, input field, post request? 
    1. command injection
    2. ssrf -> check for service only accessiable by localhost
    3. sql and nosql injection
    4. lfi
    5. path traversal
    6. xss
  15. Can you enumerate users with login panel / reset password ?
  16. Are there predictable ids?
  17. Can you upload data ? Deserialzation, XXE
  18. Is it connected to any other service on the server?
  19. Is there any form of redirect available? -> enum localhost, bypass authentication (jwt)
  20. Did you check your cookies ? Can you decode them ? JWT
  19. content discovery with custom wordlist

# windows

1. smb 
  1. use all default user/passwords
  2. Run extensive nmap scan
2. run enum4linux-ng
3. creds available
  1. Check printnightmare
4. check ethernalblue -> autoblue
5. can you upload files?
  1. some file types allows to capture hashes -> ntlm_theft
6. check https://github.com/SecWiki/windows-kernel-exploits

# linux privesc

1. check starting dir for credentials
2. Are you in a docker container
3. Which users looks interesting
4. Are there other services running on localhost only?
5. Check sudo -l
6. Are special files writeable?
  1. Files in sudo -l
  2. /etc/passwd or /etc/shadow
  3. Binarys 
7. Are there core dumps? check /var/crash. Can you otherwise extract data in memory?
6. su with previously found credentials
8. Which processes are running under high privileged user?
  1. Are they vulnerable/outdated? -> Google version
  2. Can you exploit it ? check hacking-tricks and exploitdb

# windows privesc
1. check priv: whoami /priv
2. check groups: whoami /groups
3. check version: cmd /c ver
4. run wesng
5. run winPEAS
6. check https://github.com/SecWiki/windows-kernel-exploits
98. check https://book.hacktricks.xyz/windows/windows-local-privilege-escalation
99. check https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md

