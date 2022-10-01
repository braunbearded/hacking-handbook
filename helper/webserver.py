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
        print("+++++++++++++++++++++++++++++++++REQUEST START++++++++++++++++++++++++++++++++++")
        print(self.headers)
        print("+++++++++++++++++++++++++++++++++REQUEST END++++++++++++++++++++++++++++++++++++")
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = GetHandler
with SocketServer.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server on listen on {PORT}")
    print(f"Visit: http://{IP}:{PORT}/")
    httpd.serve_forever()

# TODO
# taken from https://gist.github.com/bradmontgomery/2219997
#from http.server import BaseHTTPRequestHandler, HTTPServer
#import logging
#import sys
#
#COLOR = "\033[1;32m"
#RESET_COLOR = "\033[00m"
#
#class S(BaseHTTPRequestHandler):
#    def _set_response(self):
#        self.send_response(200)
#        self.send_header('Content-type', 'text/html')
#        self.end_headers()
#
#    def do_log(self, method):
#        content_length = self.headers['Content-Length']
#        content_length = 0 if (content_length is None) else int(content_length)
#        post_data = self.rfile.read(content_length)
#        logging.info(COLOR + method + " request,\n" + RESET_COLOR + "Path: %s\nHeaders:\n%sBody:\n%s\n",
#                str(self.path), str(self.headers), post_data.decode('utf-8'))
#        self._set_response()
#        self.wfile.write((method + " request for {}".format(self.path)).encode('utf-8'))
#
#    def do_GET(self):
#        self.do_log("GET")
#
#    def do_POST(self):
#        self.do_log("POST")
#
#    def do_PUT(self):
#        self.do_log("PUT")
#
#    def do_DELETE(self):
#        self.do_log("DELETE")
#
#def run(address, port, server_class=HTTPServer, handler_class=S):
#    logging.basicConfig(level=logging.INFO)
#    server_address = (address, port)
#    httpd = server_class(server_address, handler_class)
#    logging.info('Starting httpd...\n')
#    try:
#        httpd.serve_forever()
#    except KeyboardInterrupt:
#        pass
#    httpd.server_close()
#    logging.info('Stopping httpd...\n')
#
#if __name__ == '__main__':
#    if len(sys.argv) != 3:
#        print("Usage:\n" + sys.argv[0] + " [address] [port]")
#        sys.exit(1)
#
#    run(sys.argv[1], int(sys.argv[2]))
