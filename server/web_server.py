from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
from threading import Thread
from . import util
import requests
import re
import math


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
            # pattern = "{(\w+):\'*([0-9\.a-zA-Z\- :]+)\'*,\s*(\w+):\'*([0-9\.a-zA-Z\- :]+)\'*}"

            # # Retrieve data
            # user_id = request['params']['user_id'][0]
            # _start = re.match(pattern, request['params']['start_point'][0])
            # _end = re.match(pattern, request['params']['end_point'][0])
            # _time = re.match(pattern, request['params']['timestamp'][0])

            # start_point = (float(_start.group(2)), float(_start.group(4)))
            # end_point = (float(_end.group(2)), float(_end.group(4)))
            # times = (_time.group(2), _time.group(4))
            
            # # Get data from APIs
            # bus_schedule = json.loads(requests.get("http://localhost:8081/api/schedules").text)
            # mobility_points = json.loads(requests.get("http://localhost:8082/api/scooters").text)

            # # Calculate journeys, per provider
            # routes = []

            # for schedule in bus_schedule['schedules']:
            #     # Differences per coordinate
            #     closest_bus_stops = []

            #     # Check closest bus starting point within threshold
            #     place_index = 0
            #     for place in schedule['places']:
            #         stop_index = 0
            #         for stop in place['stops']:
            #             lat = stop['latitude']
            #             long = stop['longitude']
            #             closest_bus_stops.append({
            #                 "place": place_index,
            #                 "stop": stop_index,
            #                 "distance_to_start": math.sqrt(math.pow(start_point[0] - lat, 2) + math.pow(start_point[1] - long, 2)),
            #                 "distance_to_end": math.sqrt(math.pow(end_point[0] - lat, 2) + math.pow(end_point[1] - long, 2))
            #             })
            #             stop_index += 1
            #         place_index += 1

            #     # Sort by smallest distance from start point
            #     closest_bus_stops = sorted(closest_bus_stops, key=lambda tuple: tuple["distance_to_start"] )
            #     print("Closest Starting Bus Stops for {}: {}".format(schedule['provider'], closest_bus_stops))

            #     # Now take closest bus stop on that route to destination
            #     closest_bus_stops = sorted(closest_bus_stops, key=lambda tuple: tuple["distance_to_end"] )
            #     print("Closest Ending Bus Stops for {}: {}".format(schedule['provider'], closest_bus_stops))



            # Return result
            return json.dumps(
                {
                    "routes": [
                        {
                            "route_id": "00001a",
                            "paths": [
                                {
                                    "timespan": {
                                        "start": "2019-11-10 09:27:00",
                                        "end": "2019-11-10 09:43:00",
                                    },
                                    "startpoint": {
                                        "name": "Berkel-Enschot, Zwaanstraat",
                                        "latitude": 51.5565,
                                        "longitude": 5.0901
                                    },
                                    "endpoint": {
                                        "name": "Tilburg, Centraal Station",
                                        "latitude": 51.5614,
                                        "longitude": 5.081
                                    },
                                    "occupancy": 43,
                                    "rating": 3.9,
                                    "vehicle_type": "Bus_Connexxion_9"
                                },
                                {
                                    "timespan": {
                                        "start": "2019-11-10 09:43:00",
                                        "end": "2019-11-10 09:50:00",
                                    },
                                    "startpoint": {
                                        "name": "Tilburg, Centraal Station",
                                        "latitude": 51.5614,
                                        "longitude": 5.081
                                    },
                                    "endpoint": {
                                        "name": "Tilburg, Universiteit van Tilburg",
                                        "latitude": 51.5652,
                                        "longitude": 5.0516
                                    },
                                    "occupancy": 50,
                                    "rating": 3.4,
                                    "vehicle_type": "Train_Sprinter_4"
                                },
                                {
                                    "timespan": {
                                        "start": "2019-11-10 09:50:00",
                                        "end": "2019-11-10 09:57:00",
                                    },
                                    "startpoint": {
                                        "name": "Tilburg, Universiteit van Tilburg",
                                        "latitude": 51.5652,
                                        "longitude": 5.0516
                                    },
                                    "endpoint": {
                                        "name": "Tilburg University",
                                        "latitude": 51.5701,
                                        "longitude": 5.0816
                                    },
                                    "occupancy": 0,
                                    "rating": 2.9,
                                    "vehicle_type": "Scooter_Lime_10a4b"
                                },
                            ]
                        },
                        {
                            "route_id": "00001b",
                            "paths": [
                                {
                                    "timespan": {
                                        "start": "2019-11-10 09:29:11",
                                        "end": "2019-11-10 09:45:30",
                                    },
                                    "startpoint": {
                                        "name": "Berkel-Enschot, Zwaanstraat",
                                        "latitude": 51.5565,
                                        "longitude": 5.0901
                                    },
                                    "endpoint": {
                                        "name": "Tilburg, Centraal Station",
                                        "latitude": 51.5614,
                                        "longitude": 5.081
                                    },
                                    "occupancy": 80,
                                    "rating": 3.9,
                                    "vehicle_type": "Bus_Connexxion_44"
                                },
                                {
                                    "timespan": {
                                        "start": "2019-11-10 09:45:30",
                                        "end": "2019-11-10 09:56:00",
                                    },
                                    "startpoint": {
                                        "name": "Tilburg, Centraal Station",
                                        "latitude": 51.5614,
                                        "longitude": 5.081
                                    },
                                    "endpoint": {
                                        "name": "Vijverpad",
                                        "latitude": 51.5652,
                                        "longitude": 5.0516
                                    },
                                    "occupancy": 20,
                                    "rating": 3.4,
                                    "vehicle_type": "Bus_Connexxion_36"
                                },
                                {
                                    "timespan": {
                                        "start": "2019-11-10 09:50:00",
                                        "end": "2019-11-10 09:57:00",
                                    },
                                    "startpoint": {
                                        "name": "Vijverpad",
                                        "latitude": 51.5652,
                                        "longitude": 5.0516
                                    },
                                    "endpoint": {
                                        "name": "Tilburg University",
                                        "latitude": 51.5701,
                                        "longitude": 5.0816
                                    },
                                    "occupancy": 0,
                                    "rating": 1,
                                    "vehicle_type": "Scooter_Tier_0x345"
                                },
                            ]
                        },
                        {
                            "route_id": "00001b",
                            "paths": [
                                {
                                    "timespan": {
                                        "start": "2019-11-10 09:27:50",
                                        "end": "2019-11-10 09:52:00",
                                    },
                                    "startpoint": {
                                        "name": "Berkel-Enschot, Zwaanstraat",
                                        "latitude": 51.5565,
                                        "longitude": 5.0901
                                    },
                                    "endpoint": {
                                        "name": "Spoorlaan",
                                        "latitude": 51.5614,
                                        "longitude": 5.081
                                    },
                                    "occupancy": 80,
                                    "rating": 3.9,
                                    "vehicle_type": "Bus_Connexxion_12"
                                },
                                {
                                    "timespan": {
                                        "start": "2019-11-10 09:45:30",
                                        "end": "2019-11-10 09:56:00",
                                    },
                                    "startpoint": {
                                        "name": "Spoorlaan",
                                        "latitude": 51.5614,
                                        "longitude": 5.081
                                    },
                                    "endpoint": {
                                        "name": "Tilburg University",
                                        "latitude": 51.5652,
                                        "longitude": 5.0516
                                    },
                                    "occupancy": 20,
                                    "rating": 3.4,
                                    "vehicle_type": "Scooter_Tier_0x444"
                                }
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
    