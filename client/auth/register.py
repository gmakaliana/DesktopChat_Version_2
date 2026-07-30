# client/auth/register.py


"""
Client registration module.

Responsible for:
- Creating registration packet
- Sending registration request
- Returning server response
"""


from shared.protocol import create_packet


from shared.events import REGISTER


from client.modules.network.connection import send_request





def register_user(
        username,
        password,
        full_name
):

    """
    Sends registration request
    to server.
    """



    packet = create_packet(

        REGISTER,

        {

            "username": username,

            "password": password,

            "full_name": full_name

        }

    )



    response = send_request(

        packet

    )



    return response