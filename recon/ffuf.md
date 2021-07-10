# default webdiscovery

## all

```
ffuf -c -u "http://$rhost$rport/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -o ffuf-root.txt -recursion -e ".htm,.py,.sh,.php,.txt,.md,.html,.asp,.aspx,.jsp" -od ffuf-root -mc "200,204,301,302,307,401,403,405"
```

## linux

```
ffuf -c -u "http://$rhost$rport/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -o ffuf-root-$rhost.txt -recursion -e ".htm,.py,.sh,.php,.txt,.md,.html" -od ffuf-root-$rhost -mc "200,204,301,302,307,401,403,405"
```

## proxy

```
ffuf -c -u "http://$rhost$rport/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -o ffuf-root-$rhost.txt -recursion -e ".htm,.py,.sh,.php,.txt,.md,.html" -od ffuf-root-$rhost -mc "200,204,301,302,307,401,403,405 -replay-proxy http://127.0.0.1:8080"
```

## vhost

```
ffuf -c -u "http://$rhost$rport" -w pot-vhosts.txt -o ffuf-vhost-$rhost.txt -od ffuf-vhost-$rhost -H "Host: FUZZ.$rhost" -fs <filter size>
```

## all improved

```bash
output="http-80"; ffuf -c -u "http://$rhost/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/raft-small-words-lowercase.txt -o "ffuf-$output.txt" -recursion -e ".htm,.py,.sh,.php,.txt,.md,.html,.asp,.aspx,.jsp" -od "ffuf-$output" -mc "200,204,301,302,307,401,405,403"
```
