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
                    "modality": "Bus",
                    "places": [
                        {
                            "place_name": "Tilburg",
                            "stops": [
                                {
                                    "stop_name": "First Straat",
                                    "timestamp": "2019-01-01 00:01:00",
                                    "lat": 4.21,
                                    "lat": 44.1
                                },
                                {
                                    "stop_name": "Second Straat",
                                    "timestamp": "2019-01-01 00:02:00",
                                    "lat": 5.21,
                                    "lat": 55.1
                                },
                                {
                                    "stop_name": "Third Straat",
                                    "timestamp": "2019-01-01 00:03:00",
                                    "lat": 6.21,
                                    "lat": 66.1
                                },
                                {
                                    "stop_name": "Fourth Straat",
                                    "timestamp": "2019-01-01 00:04:00",
                                    "lat": 7.21,
                                    "lat": 77.1
                                }
                            ]
                        },
                        {
                            "place_name": "Neighbourburg",
                            "stops": [
                                {
                                    "stop_name": "Fifth Straat",
                                    "timestamp": "2019-01-01 00:05:00",
                                    "lat": 7.211,
                                    "lat": 77.11
                                },
                                {
                                    "stop_name": "Sixth Straat",
                                    "timestamp": "2019-01-01 00:06:00",
                                    "lat": 7.2111,
                                    "lat": 77.111
                                },
                                {
                                    "stop_name": "Seventh Straat",
                                    "timestamp": "2019-01-01 00:03:00",
                                    "lat": 6.21,
                                    "lat": 66.1
                                },
                                {
                                    "stop_name": "Eigth Straat",
                                    "timestamp": "2019-01-01 00:04:00",
                                    "lat": 7.21,
                                    "lat": 77.1
                                }
                            ]
                        }
                    ],
                    "line": 404,
                    "provider": "Connexxion"
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
    