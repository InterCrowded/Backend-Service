from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
from threading import Thread
from . import util


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class TransportRouter:
    def get(self, path: str):
        request = util.parseRequest(path)
        # I know it's messy, but just add a new if statement per path
        if request["path"] == "/api/schedules":
            return json.dumps(
                {
                    "modality": "Bus",
                    "occupancy": 43,
                    "line": 404,
                    "provider": "Connexxion",
                    "rating": 3.4,
                    "places": [
                        {
                            "place_name": "Tilburg",
                            "stops": [
                                {
                                    "stop_name": "First Straat",
                                    "timestamp": "2019-01-01 00:01:00",
                                    "latitude": 4.21,
                                    "longitude": 44.1
                                },
                                {
                                    "stop_name": "Second Straat",
                                    "timestamp": "2019-01-01 00:02:00",
                                    "latitude": 5.21,
                                    "longitude": 55.1
                                },
                                {
                                    "stop_name": "Third Straat",
                                    "timestamp": "2019-01-01 00:03:00",
                                    "latitude": 6.21,
                                    "longitude": 66.1
                                },
                                {
                                    "stop_name": "Fourth Straat",
                                    "timestamp": "2019-01-01 00:04:00",
                                    "latitude": 7.21,
                                    "longitude": 77.1
                                }
                            ]
                        },
                        {
                            "place_name": "Neighbourburg",
                            "stops": [
                                {
                                    "stop_name": "Fifth Straat",
                                    "timestamp": "2019-01-01 00:05:00",
                                    "latitude": 7.211,
                                    "longitude": 77.11
                                },
                                {
                                    "stop_name": "Sixth Straat",
                                    "timestamp": "2019-01-01 00:06:00",
                                    "latitude": 7.2111,
                                    "longitude": 77.111
                                },
                                {
                                    "stop_name": "Seventh Straat",
                                    "timestamp": "2019-01-01 00:03:00",
                                    "latitude": 6.21,
                                    "longitude": 66.1
                                },
                                {
                                    "stop_name": "Eigth Straat",
                                    "timestamp": "2019-01-01 00:04:00",
                                    "latitude": 7.21,
                                    "longitude": 77.1
                                }
                            ]
                        }
                    ],
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
    