# client/auth/login.py


"""
Client login module.

Responsible for:
- Preparing login request
- Sending authentication request
"""


from modules.network.connection import send_request



def login_user(username, password):
    """
    Sends login request to server.
    """


    request = {

        "event": "LOGIN",

        "data": {

            "username": username,

            "password": password

        }

    }


    response = send_request(
        request
    )


    return response