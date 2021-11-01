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
chisel.exe client 10.9.133.175:1337 R:135:localhost:9999
```

# start server

```
chisel server -p 8888 --reverse --host 0.0.0.0
```