"""
User presence management.

Client side status communication.

The server owns user status.
"""


from client.modules.network.connection import send_event


from shared.protocol import create_packet


from shared.events import LOGOUT





def set_offline(user_id):

    """
    Sends logout event.

    Server will:
    - remove connection
    - update status Offline
    - update last seen
    """


    packet = create_packet(

        LOGOUT,

        {

            "user_id": user_id

        }

    )



    return send_event(

        packet

    )