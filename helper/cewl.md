# generate wordlist from website

```bash
cewl --meta --count --with-numbers --email -w cewl-"$rhost".txt http://$rhost
```

# remove count from cewl wordlist

Dont forget to make a copy befor and delete emails at end of the file.

```bash
sed -i 's/, [0-9]*$//g' cewl-$rhost.txt
```
# generate wordlist from website max 5 level deep

```bash
cewl -d 5 -m 4 -w pot-password.txt --with-numbers --meta --email "cewl-$rhost.txt"
```
