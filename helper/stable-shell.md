# python shell

```
python3 -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
background; stty raw -echo && stty size; fg
stty rows 58 cols 212
```
