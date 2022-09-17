#!/usr/bin/env python

import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging
import sys
import netifaces as ni

IP = "0.0.0.0"
PORT = 8000 # default

if len(sys.argv) >= 2:
    PORT = int(sys.argv[1])

if len(sys.argv) >= 3:
    IP = ni.ifaddresses(sys.argv[2])[ni.AF_INET][0]['addr']

class GetHandler(
        SimpleHTTPServer.SimpleHTTPRequestHandler
        ):

    def do_GET(self):
        #logging.error(self.headers)
        print("+++++++++++++++++++++++++++++++++REQUEST START++++++++++++++++++++++++++++++++++")
        print(self.headers)
        print("+++++++++++++++++++++++++++++++++REQUEST END++++++++++++++++++++++++++++++++++++")
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print(f"Server on listen on {PORT}")
print(f"Visit: http://{IP}:{PORT}/")
httpd.serve_forever()
