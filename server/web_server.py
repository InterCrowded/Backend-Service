from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
from threading import Thread
from . import util


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class WebRouter:
    def get(self, path: str):
        request = util.parseRequest(path)
        print("Request:", request)
        # I know it's messy, but just add a new if statement per path
        if request["path"] == "/api/routes/confirm":
            return json.dumps(
                {
                    "code": 200
                }
            )
        elif request["path"] == "/api/routes":
            return json.dumps(
                {
                    "routes": [
                        {
                            "route_id": "00001a",
                            "paths": [
                                {
                                    "timespan": {
                                        "start": "2019-01-02 00:00:00",
                                        "end": "2019-01-02 01:30:00",
                                    },
                                    "startpoint": {
                                        "name": "Centralest Central Station",
                                        "lattitude": 0,
                                        "longitude": 0
                                    },
                                    "endpoint": {
                                        "name": "Willy Wonka's Chocolate Factory",
                                        "lattitude": 1,
                                        "longitude": 1
                                    },
                                    "occupancy": 43,
                                    "rating": 4.5,
                                    "vehicle_type": "Bus_Lijn_808"
                                },
                                {
                                    "timespan": {
                                        "start": "2019-01-01 05:00:00",
                                        "end": "2019-01-01 12:00:00",
                                    },
                                    "startpoint": {
                                        "name": "Centre of a Dying Star",
                                        "lattitude": 1.2,
                                        "longitude": 1.2
                                    },
                                    "endpoint": {
                                        "name": "Crab Nebula",
                                        "lattitude": 2,
                                        "longitude": 2
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
                                    "timespan": {
                                        "start": "2019-01-01 00:00:00",
                                        "end": "2019-01-01 01:00:00",
                                    },
                                    "startpoint": {
                                        "name": "Never gonna give you up",
                                        "lattitude": 5,
                                        "longitude": 3.74
                                    },
                                    "endpoint": {
                                        "name": "Never gonna let you down",
                                        "lattitude": 6,
                                        "longitude": 8
                                    },
                                    "occupancy": 21,
                                    "rating": 2,
                                    "vehicle_type": "Bus_GoGo_112"
                                },
                                {
                                    "timespan": {
                                        "start": "2019-01-03 00:00:00",
                                        "end": "2019-01-03 01:00:00",
                                    },
                                    "startpoint": {
                                        "name": "Never gonna turn around and",
                                        "lattitude": 7,
                                        "longitude": 8
                                    },
                                    "endpoint": {
                                        "name": "Desert you",
                                        "lattitudetitude": 7.1,
                                        "longitude": 8.1
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
    