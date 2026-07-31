"""
Client registration module.

Responsible for:
- Validating user input
- Creating registration packet
- Sending registration request
- Returning server response
"""


from client.modules.utils.validation import validate_username
from client.modules.utils.validation import validate_password
from client.modules.utils.validation import validate_full_name

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

    username = username.strip()

    full_name = full_name.strip()

    # -------------------------
    # Username validation
    # -------------------------

    valid, message = validate_username(
        username
    )

    if not valid:

        return {

            "event": "REGISTER_FAILED",

            "data": {

                "message": message

            }

        }

    # -------------------------
    # Password validation
    # -------------------------

    valid, message = validate_password(
        password
    )

    if not valid:

        return {

            "event": "REGISTER_FAILED",

            "data": {

                "message": message

            }

        }

    # -------------------------
    # Full name validation
    # -------------------------

    valid, message = validate_full_name(
        full_name
    )

    if not valid:

        return {

            "event": "REGISTER_FAILED",

            "data": {

                "message": message

            }

        }

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