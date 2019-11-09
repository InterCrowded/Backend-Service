from http.server import HTTPServer
import time
from . import WebServer


host = "localhost"
port = 8081
webServer = None

try:
    print("Starting Server...")
    webServer = HTTPServer((host, port), WebServer)
    print("Server listening on http://{}:{}".format(host, port))
    webServer.serve_forever()
except KeyboardInterrupt:
    print("Exiting server...")
finally:
    if webServer:
        webServer.server_close()
        print("Server stopped")
