"""
High level networking interface.

Other client modules use this file.

GUI and authentication modules
never communicate directly with
websocket_client.py.

Responsibilities:
- initialize connection
- send requests
- receive responses
"""



from client.modules.network.websocket_client import connect

from client.modules.network.websocket_client import send

from client.modules.network.websocket_client import receive





# Desktop Chat Server address
SERVER_URL = "ws://127.0.0.1:8000/ws"








def initialize_network():

    """
    Initializes WebSocket communication.

    Returns:
        True  - connected
        False - failed
    """



    result = connect(

        SERVER_URL

    )



    return result








def send_request(data):

    """
    Sends request to server
    and waits for response.

    Converts server JSON response
    into Python dictionary.
    """


    import json



    sent = send(

        data

    )



    # Stop if sending failed

    if not sent:


        return None




    response = receive()



    if response:


        try:


            return json.loads(

                response

            )


        except Exception as error:


            print(

                "Response decode error:",

                error

            )


            return None




    return None