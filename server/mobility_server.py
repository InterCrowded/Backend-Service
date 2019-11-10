from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
from threading import Thread
from . import util


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class MobilityRouter:
    def get(self, path: str):
        request = util.parseRequest(path)
        # I know it's messy, but just add a new if statement per path
        if request["path"] == "/api/scooters":
            return json.dumps(
                {
                    "transports": [
                        {
                            "modality": "Scooter",
                            "provider": "Lime",
                            "rating": 2.5,
                            "locations": [
                                {
                                    "charge": 57,
                                    "latitude": 5,
                                    "longitude": 5,
                                    "id": "10a4b"
                                },
                                {
                                    "charge": 58,
                                    "latitude": 5.1,
                                    "longitude": 5.1,
                                    "id": "10a4c"
                                },
                                {
                                    "charge": 59,
                                    "latitude": 5.2,
                                    "longitude": 5.2,
                                    "id": "10a4d"
                                },
                                {
                                    "charge": 60,
                                    "latitude": 5.3,
                                    "longitude": 5.3,
                                    "id": "10a4e"
                                },
                                {
                                    "charge": 61,
                                    "latitude": 5.4,
                                    "longitude": 5.4,
                                    "id": "10a4f"
                                },
                                {
                                    "charge": 62,
                                    "latitude": 5.5,
                                    "longitude": 5.5,
                                    "id": "10a4g"
                                },
                                {
                                    "charge": 63,
                                    "latitude": 5.6,
                                    "longitude": 5.6,
                                    "id": "10a4h"
                                }
                            ]
                        }
                    ]
                }
            )
        elif path == "/routes/confirm":
            return json.dumps(
                {
                    "message": "Route path called"
                }
            )
        else:
            return json.dumps(
                {
                    "message": "404"
                }
            )
        
__router__ = MobilityRouter()

class MobilityHandler(BaseHTTPRequestHandler):
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


class MobilityServer(Thread):
    def __init__(self, host: str, port: int, server_name: str):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.name = server_name
        self.mobilityServer = None

    def run(self):
        try:
            print("Starting {}...".format(self.name))
            self.mobilityServer = ThreadingHTTPServer((self.host, self.port), MobilityHandler)
            print("{} listening on http://{}:{}".format(self.name, self.host, self.port))
            self.mobilityServer.serve_forever()
        except Exception as e:
            print("Something went wrong in {}: {}".format(self.name, e))

    def end(self):
        if self.mobilityServer:
            self.mobilityServer.shutdown()
            self.mobilityServer.server_close()
        self.join()
    