"""
Low-level WebSocket client.

Handles:
- connect
- disconnect
- send
- receive
"""


import websocket



connection = None



def connect(url):

    """
    Creates WebSocket connection.
    """

    global connection


    connection = websocket.WebSocket()


    connection.connect(
        url
    )


    print(
        "Connected to server."
    )



def disconnect():

    """
    Closes WebSocket connection.
    """

    global connection


    if connection:

        connection.close()


        print(
            "Disconnected."
        )



def send(message):

    """
    Sends data to server.
    """

    if connection:

        connection.send(
            message
        )



def receive():

    """
    Receives server response.
    """

    if connection:

        return connection.recv()


    return None