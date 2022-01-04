# enum4linux with empty user and password

```bash
enum4linux -a -u "" -p "" "$rhost"
```

# enum4linux with guest account

```bash
enum4linux -a -u "guest" -p "" "$rhost"
```

# enum4linux as guest with all options

```bash
enum4linux -U -M -S -P -G -d -a -r -l -o -i "$rhost"
```
