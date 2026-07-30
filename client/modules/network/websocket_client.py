"""
Low-level WebSocket client.

Responsibilities:
- create WebSocket connection
- disconnect from server
- send data
- receive data

This file communicates directly
with the WebSocket library.

Other client modules should NOT
import this file directly.
"""


import websocket



# Stores the active WebSocket connection
connection = None





def connect(url):

    """
    Creates WebSocket connection.

    Parameters:
        url:
            Server WebSocket address.

    Returns:
        True  - connection successful
        False - connection failed
    """

    global connection


    try:

        # Create WebSocket object
        connection = websocket.WebSocket()


        # Connect to server
        connection.connect(
            url
        )


        print(
            "Connected to server."
        )


        return True



    except Exception as error:


        print(
            "WebSocket connection failed:",
            error
        )


        connection = None


        return False








def disconnect():

    """
    Closes WebSocket connection.
    """

    global connection



    if connection:


        connection.close()


        connection = None


        print(
            "Disconnected from server."
        )








def send(message):

    """
    Sends data to server.

    Parameters:
        message:
            Data to send.

    Returns:
        True  - sent successfully
        False - failed
    """


    if connection:


        try:


            connection.send(
                message
            )


            return True



        except Exception as error:


            print(
                "Send error:",
                error
            )


            return False



    return False








def receive():

    """
    Receives response from server.

    Returns:
        Server response
        None if failed
    """


    if connection:


        try:


            return connection.recv()



        except Exception as error:


            print(
                "Receive error:",
                error
            )


            return None



    return None