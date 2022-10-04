# bypass localhost filer 

See [localhost bypass](https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery#basic-bypass-localhost for more)

- http://[::]:80/
- http://0

# bypass via redirect

Server connects to your Webserver which will send a redirect to any domain we want for example.
See this script: [python redirect example](https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery#bypass-via-redirect)
