# wpscan

## default options

```bash
wpscan --url "http://$rhost$rport"
```

## bruteforce with wordlist

```bash
wpscan --url "http://$rhost$rport" --passwords wordlist-password --username wordlist-usernames
```

## detailed scan

```bash
wpscan --url "http://$rhost$rport" -e at,ap,cb,dbe,u,m
```

# check via nikto

```bash
nikto -ask=no -h "http://$rhost$rport"
```
