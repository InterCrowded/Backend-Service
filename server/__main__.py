from . import getWebServer, getTransportServer, getMobilityServer
import time


try:
    # Allocate servers
    web_server = getWebServer()
    transport_server = getTransportServer()
    mobility_server = getMobilityServer()
    # Start
    web_server.start()
    transport_server.start()
    mobility_server.start()
    while True:
        command = input()
        if command == 'r':
            print("Restarting servers...")
            # Stop
            web_server.end()
            transport_server.end()
            mobility_server.end()
            # Reset
            web_server = getWebServer()
            transport_server = getTransportServer()
            mobility_server = getMobilityServer()
            # Start
            web_server.start()
            transport_server.start()
            mobility_server.start()
        elif command == 's':
            print("Exiting servers...")
            web_server.end()
            transport_server.end()
            mobility_server.end()
            break
except KeyboardInterrupt:
    print("Exiting servers...")
    if web_server:
        web_server.end()
        transport_server.end()
        mobility_server.end()
