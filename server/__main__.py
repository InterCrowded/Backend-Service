from http.server import HTTPServer
import time
from . import WebServer
import socket


# Server data
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
openHost = "0.0.0.0" # Allow all connections
port = 8081
webServer = None

try:
    print("Starting Server...")
    webServer = HTTPServer((openHost, port), WebServer)
    print("Server listening on http://{}:{}".format(host, port))
    webServer.serve_forever()
except KeyboardInterrupt:
    print("Exiting server...")
finally:
    if webServer:
        webServer.server_close()
        print("Server stopped")
