from .web_server import WebServer
from .transport_server import TransportServer
from .mobility_server import MobilityServer

def getWebServer():
    return WebServer(host="0.0.0.0", port=8080, server_name="WebServer")

def getTransportServer():
    return TransportServer(host="0.0.0.0", port=8081, server_name="TransportServer")

def getMobilityServer():
    return MobilityServer(host="0.0.0.0", port=8082, server_name="MobilityServer")
