from http.server import BaseHTTPRequestHandler
import json

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = json.dumps(
            {
                "message": "hi"
            }
        )
        self.send_response(code=200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(payload))
        self.end_headers()
        # Return response
        self.wfile.write(bytes(payload, encoding="utf-8"))

