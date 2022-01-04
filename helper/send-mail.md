# send a mail via curl 

```bash
curl --url 'smtp://localhost' --mail-from 'root@some.tld' --mail-rcpt 'kyle@some.tld' -F subject="subject" -F text="body"
```
