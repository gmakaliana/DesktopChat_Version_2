# client/auth/login.py


"""
Client login module.

Sends login request
to server.
"""


from shared.protocol import create_packet

from shared.events import LOGIN

from client.modules.network.connection import send_request



def login_user(username, password):

    """
    Authenticate user with server.
    """


    packet = create_packet(

        LOGIN,

        {

            "username": username,

            "password": password

        }

    )


    response = send_request(

        packet

    )


    return response