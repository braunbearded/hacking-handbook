# enum4linux (old)

## enumerate with empty user and password

```bash
enum4linux -a -u "" -p "" "$rhost"
```

## enumerate with guest account

```bash
enum4linux -a -u "guest" -p "" "$rhost"
```

## enumerate as guest with all options

```bash
enum4linux -U -M -S -P -G -d -a -r -l -o -i "$rhost"
```

# enum4line4linux-ng

## fast

```bash
enum4line4linux-ng.py "$rhost"
```

## extensive and detailed

```bash
enum4line4linux-ng.py -A -Gm -C -R -d "$rhost"
```
