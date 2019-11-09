from . import Server
from http.server import HTTPServer
import time


host = "localhost"
port = 8081

try:
    print("Starting Server...")
    webServer = HTTPServer((host, port), Server())
    print("Server listening on http://{}:{}".format(host, port))
except KeyboardInterrupt:
    print("Exiting server...")
finally:
    webServer.server_close()
    print("Server stopped")
