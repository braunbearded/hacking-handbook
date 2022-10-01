# tunnel local port 8001 to remote 8000

```
ssh -g -L 8001:localhost:8000 -N user@$rhost
```

# tunnel local port 445 to remote 445

```bash
ssh -N -L 0.0.0.0:445:"$rhost":445 user@$rhost
```
