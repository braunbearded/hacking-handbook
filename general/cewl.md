# generate wordlist from website

```bash
cewl -d 5 -m 4 -w "cewl-$rhost.txt" --with-numbers --meta --count --email "http://$rhost"
```

# remove count from cewl wordlist

Dont forget to make a copy befor and delete emails at end of the file.

```bash
sed -i 's/, [0-9]*$//g' cewl-$rhost.txt
```
