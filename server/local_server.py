#!/usr/bin/env python3
# launch a simple python3 web server which allows COEP and COOP, exposing better timers
# ref: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/High_precision_timing#reduced_precision 
# ref: https://stackoverflow.com/questions/21956683/enable-access-control-on-simple-http-server
from http.server import SimpleHTTPRequestHandler, test
import sys

class CORSRequestHandler (SimpleHTTPRequestHandler):

    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy','same-origin');
        self.send_header('Cross-Origin-Embedder-Policy','require-corp');

        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(CORSRequestHandler, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
