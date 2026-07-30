# client/modules/network/event_handler.py


"""
Processes incoming server events.
"""


from shared.events import PONG



def handle_event(packet):

    """
    Handles received events.
    """


    event = packet["event"]



    if event == PONG:


        print(
            "Heartbeat received."
        )