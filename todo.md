# windows stuff

- https://www.hackingarticles.in/a-little-guide-to-smb-enumeration/
- https://0xdf.gitlab.io/2018/12/02/pwk-notes-smb-enumeration-checklist-update1.html#smbmap
- nmblookup -A "$rhost"

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
