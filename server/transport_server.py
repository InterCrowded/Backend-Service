from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
from threading import Thread


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class TransportRouter:
    def get(self, path: str):
        # I know it's messy, but just add a new if statement per path
        if path == "/api/schedules":
            return json.dumps(
                {
                    'message': 'Api path called'
                }
            )
        else:
            return json.dumps(
                {
                    "message": "404"
                }
            )
        
__router__ = TransportRouter()

class TransportHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(code=200)
            self.send_header("Content-Type", "image/x-icon")
            self.end_headers()
        else:
            payload = __router__.get(self.path)
            self.send_response(code=200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(payload))
            self.end_headers()
            # Return response
            self.wfile.write(bytes(payload, encoding="utf-8"))


class TransportServer(Thread):
    def __init__(self, host: str, port: int, server_name: str):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.name = server_name
        self.transportServer = None

    def run(self):
        try:
            print("Starting {}...".format(self.name))
            self.transportServer = ThreadingHTTPServer((self.host, self.port), TransportHandler)
            print("{} listening on http://{}:{}".format(self.name, self.host, self.port))
            self.transportServer.serve_forever()
        except Exception as e:
            print("Something went wrong in {}: {}".format(self.name, e))

    def end(self):
        if self.transportServer:
            self.transportServer.shutdown()
            self.transportServer.server_close()
        self.join()
    