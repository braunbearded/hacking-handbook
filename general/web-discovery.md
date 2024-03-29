# webdiscovery

## ffuf

### all

```bash
ffuf -c -u "http://$rhost$rport/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -o ffuf-root.txt -recursion -e ".htm,.py,.sh,.php,.txt,.md,.html,.asp,.aspx,.jsp" -od ffuf-root -mc "200,204,301,302,307,401,403,405"
```

### linux

```bash
ffuf -c -u "http://$rhost$rport/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -o ffuf-root-$rhost.txt -recursion -e ".htm,.py,.sh,.php,.txt,.md,.html" -od ffuf-root-$rhost -mc "200,204,301,302,307,401,403,405"
```

### proxy

```bash
ffuf -c -u "http://$rhost$rport/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -o ffuf-root-$rhost.txt -recursion -e ".htm,.py,.sh,.php,.txt,.md,.html" -od ffuf-root-$rhost -mc "200,204,301,302,307,401,403,405 -replay-proxy http://127.0.0.1:8080"
```

### all improved

```bash
ffuf_out="ffuf-http-80"; ffuf -c -u "http://$rhost/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/raft-small-words-lowercase.txt -o "$ffuf_out/summary.json" -recursion -e ".htm,.py,.sh,.php,.txt,.md,.html,.asp,.aspx,.jsp" -od "$ffuf_out" -mc "200,204,301,302,307,401,405,403" -H "Host: $rhost"
```

### analyze summary

```bash
cd into/fuff-result
jq -r '.results[] | [.status, .url, .resultfile] | @tsv' summary.txt | grep -v "^403"
```

### http with request file

```bash
ffuf -c -request file.req -w /usr/share/seclists/Discovery/Web-Content/raft-small-words-lowercase.txt -request-proto http
```
