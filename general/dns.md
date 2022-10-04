# linux attack

## zone transfer

```bash
dig axfr @nameserver domain.tld
```

## every record

```bash
dig ANY @nameserver domain.tld
```

## enumerate dns with specific dns server

```bash
dnsrecon -d domain.to.enum -n some.nameserver/ip
```

## enumerate dns with wordlist

```bash
dnsenum --dnsserver some.dns.server -f /usr/share/seclists/Discovery/DNS/shubs-subdomains.txt -t 2 '*.sub.domain'
```
