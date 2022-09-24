# start service

sudo service tor start

# edit proxy

sudoedit /etc/proxychains.conf

# hide proxychain message 

uncomment: quiet_mode

# nmap scan via proxychains

proxychains is using tcp so make sure to use tcp scan like -sT
