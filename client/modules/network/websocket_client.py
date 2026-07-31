"""
Low-level WebSocket client.

Responsibilities:
- create WebSocket connection
- disconnect from server
- send data
- receive data
- maintain heartbeat
- separate heartbeat packets from application responses
"""


import websocket

import threading

import time

import queue



# Active WebSocket connection

connection = None



# Heartbeat control

heartbeat_running = False



# Receiver control

receiver_running = False



# Stores server responses

response_queue = queue.Queue()





def start_receiver():

    """
    Continuously receives messages
    from server.
    """


    global receiver_running


    from shared.events import PONG



    receiver_running = True



    def receiver():

        while receiver_running:


            try:


                message = connection.recv()



                if message:


                    import json


                    packet = json.loads(

                        message

                    )


                    event = packet.get(

                        "event"

                    )



                    # Ignore heartbeat response

                    if event == PONG:


                        continue



                    response_queue.put(

                        message

                    )



            except Exception as error:


                print(

                    "Receiver error:",

                    error

                )


                break



    thread = threading.Thread(

        target=receiver,

        daemon=True

    )


    thread.start()







def start_heartbeat():

    """
    Sends heartbeat packets.
    """


    global heartbeat_running


    from shared.protocol import create_packet

    from shared.events import PING



    heartbeat_running = True



    def heartbeat():


        while heartbeat_running:


            try:


                if connection:


                    packet = create_packet(

                        PING,

                        {}

                    )


                    connection.send(

                        packet

                    )


                    print(

                        "Heartbeat sent."

                    )



            except Exception as error:


                print(

                    "Heartbeat error:",

                    error

                )


                break



            time.sleep(20)



    thread = threading.Thread(

        target=heartbeat,

        daemon=True

    )


    thread.start()







def connect(url):

    """
    Creates WebSocket connection.
    """


    global connection



    try:


        connection = websocket.WebSocket()



        connection.connect(

            url

        )



        print(

            "Connected to server."

        )



        start_receiver()


        start_heartbeat()



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

    global heartbeat_running

    global receiver_running



    heartbeat_running = False

    receiver_running = False



    if connection:


        connection.close()



        connection = None



        print(

            "Disconnected from server."

        )







def send(message):

    """
    Sends data to server.
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
    Gets next application response.
    """


    try:


        return response_queue.get(

            timeout=10

        )



    except queue.Empty:


        return None