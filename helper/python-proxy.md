# forward request from python to proxy

```python
proxies = {
  "http": "http://127.0.0.1:8080",
  "https": "http://127.0.0.1:8080",
}

requests.get("http://example.org", proxies=proxies)
```
