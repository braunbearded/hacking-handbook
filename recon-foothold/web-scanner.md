# wpscan

## default options

```bash
wpscan --url "http://$rhost$rport"
```

## bruteforce with wordlist

```bash
wpscan --url "http://$rhost$rport" --passwords wordlist-password --usernames wordlist-usernames --random-user-agent
```

## detailed scan

```bash
wpscan --url "http://$rhost$rport" -e at,ap,cb,dbe,u,m,tt --random-user-agent -o wpscan-result.txt -f cli --detection-mode aggressive --plugins-detection aggressive --plugins-version-detection aggressive 
```

# check via nikto

```bash
nikto -ask=no -h "http://$rhost$rport"
```
