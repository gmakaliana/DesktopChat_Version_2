# shared/protocol.py


"""
Defines the communication format
between client and server.
"""


import json



def create_packet(event, data=None):

    """
    Creates a standard network packet.
    """


    packet = {

        "event": event,

        "data": data or {}

    }


    return json.dumps(packet)



def read_packet(message):

    """
    Converts received JSON
    into Python dictionary.
    """


    return json.loads(message)