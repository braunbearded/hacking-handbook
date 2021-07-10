# generate wordlist from website

```
cewl --meta -e -c --with-numbers -w cewl-"$rhost".txt http://$rhost
```

# cleanup wordlist

Dont forget to make a copy befor and delete emails at end of the file.

```
sed -i 's/, [0-9]*$//g' cewl.txt
```
