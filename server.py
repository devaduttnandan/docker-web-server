from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

PORT = 8000
DIRECTORY = "static"

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        os.chdir(DIRECTORY)  # Change to the static directory
        super().__init__(*args, **kwargs)

with TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

