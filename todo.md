# wordlist

## check tool

html2dic
https://github.com/D4Vinci/CWFF
https://github.com/shellhunter/gocewl
https://github.com/Zarcolio/wwwordlist
https://github.com/hakluke/haklistgen

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
