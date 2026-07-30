# client/modules/network/connection.py


"""
High level networking interface.

Other parts of the client
use this file.

GUI and authentication modules
do not communicate directly
with websocket_client.py.
"""


from modules.network.websocket_client import connect

from modules.network.websocket_client import send

from modules.network.websocket_client import receive



SERVER_URL = "ws://127.0.0.1:8000/ws"



def initialize_network():

    """
    Initializes WebSocket communication.
    """


    try:

        connect(
            SERVER_URL
        )


    except Exception as error:


        print(
            "Network initialization failed:",
            error
        )



def send_request(data):

    """
    Send request and wait for response.
    """


    send(
        data
    )


    response = receive()


    return response