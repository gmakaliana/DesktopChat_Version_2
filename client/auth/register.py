# client/auth/register.py


"""
Client registration module.

Responsible for:
- Collecting registration data
- Sending registration request
"""


from modules.network.connection import send_request



def register_user(
        username,
        password,
        full_name
):

    """
    Sends registration request
    to server.
    """


    request = {

        "event": "REGISTER",

        "data": {

            "username": username,

            "password": password,

            "full_name": full_name

        }

    }


    response = send_request(
        request
    )


    return response