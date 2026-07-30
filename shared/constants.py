# shared/constants.py


"""
Global communication constants.

Used by both client and server.
"""


SERVER_HOST = "127.0.0.1"


SERVER_PORT = 8000


WEBSOCKET_URL = (

    f"ws://{SERVER_HOST}:{SERVER_PORT}/ws"

)


HEARTBEAT_INTERVAL = 30