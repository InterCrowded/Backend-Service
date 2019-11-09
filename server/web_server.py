from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
from threading import Thread


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class WebRouter:
    def get(self, path: str):
        # I know it's messy, but just add a new if statement per path
        if path == "/api/routes":
            return json.dumps(
                {
                    "routes": [
                        {
                            "route_id": "00001a",
                            "paths": [
                                {
                                    "timespan": 300,
                                    "start_point": {
                                        "lat": 0,
                                        "long": 0
                                    },
                                    "end_point": {
                                        "lat": 1,
                                        "long": 1
                                    },
                                    "occupancy": 43,
                                    "rating": 4.5,
                                    "vehicle_type": "Bus_Lijn_808"
                                },
                                {
                                    "timespan": 540,
                                    "start_point": {
                                        "lat": 1.2,
                                        "long": 1.2
                                    },
                                    "end_point": {
                                        "lat": 2,
                                        "long": 2
                                    },
                                    "occupancy": 0,
                                    "rating": 3.4,
                                    "vehicle_type": "Scooter_Lime_10a4b"
                                },
                            ]
                        },
                        {
                            "route_id": "00001b",
                            "paths": [
                                {
                                    "timespan": 120,
                                    "start_point": {
                                        "lat": 5,
                                        "long": 3.74
                                    },
                                    "end_point": {
                                        "lat": 6,
                                        "long": 8
                                    },
                                    "occupancy": 21,
                                    "rating": 2,
                                    "vehicle_type": "Bus_GoGo_112"
                                },
                                {
                                    "timespan": 600,
                                    "start_point": {
                                        "lat": 7,
                                        "long": 8
                                    },
                                    "end_point": {
                                        "lat": 7.1,
                                        "long": 8.1
                                    },
                                    "occupancy": 0,
                                    "rating": 3.4,
                                    "vehicle_type": "Scooter_Oceania_bca77"
                                },
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
        
__router__ = WebRouter()

class WebHandler(BaseHTTPRequestHandler):
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


class WebServer(Thread):
    def __init__(self, host: str, port: int, server_name: str):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.name = server_name
        self.webServer = None

    def run(self):
        try:
            print("Starting {}...".format(self.name))
            self.webServer = ThreadingHTTPServer((self.host, self.port), WebHandler)
            print("{} listening on http://{}:{}".format(self.name, self.host, self.port))
            self.webServer.serve_forever()
        except Exception as e:
            print("Something went wrong in {}: {}".format(self.name, e))

    def end(self):
        if self.webServer:
            self.webServer.shutdown()
            self.webServer.server_close()
        self.join()
    