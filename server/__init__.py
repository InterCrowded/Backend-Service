from http.server import BaseHTTPRequestHandler
import json

class WebRouter:
    def get(self, path: str):
        # I know it's messy, but just add a new if statement per path
        if path == "/api":
            return json.dumps(
                {
                    'message': 'Api path called'
                }
            )
        elif path == "/route":
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

class WebServer(BaseHTTPRequestHandler):
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
