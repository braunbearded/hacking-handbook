# fake systemtime

## installation

```bash
git clone https://github.com/wolfcw/libfaketime.git
cd libfaketime/src
sudo make install
```

## example

```bash
export FAKETIME="2020-01-01 12:12:12"
LD_PRELOAD=/usr/local/lib/faketime/libfaketime.so.1 date
```
