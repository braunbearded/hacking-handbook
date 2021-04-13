# tunnel local port 8001 to remote 8000

```
ssh -g -L 8001:localhost:8000 -N user@$rhost
```
