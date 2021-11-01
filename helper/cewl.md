# generate wordlist from website

```bash
cewl --meta -e -c --with-numbers -w cewl-"$rhost".txt http://$rhost
```

# cleanup wordlist

Dont forget to make a copy befor and delete emails at end of the file.

```bash
sed -i 's/, [0-9]*$//g' cewl.txt
```
# generate wordlist from website max 5 level deep

```bash
cewl -d 5 -m 4 -w pot-password.txt --with-numbers -a -e "$rhost"
```
