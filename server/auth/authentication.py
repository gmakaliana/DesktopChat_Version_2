"""
Server authentication module.

Responsible for:
- registering users
- authenticating users

This module connects:
WebSocket events
        |
        v
Database queries
"""


from server.database.queries import create_user
from server.database.queries import get_user_by_username

from server.auth.password_utils import hash_password
from server.auth.password_utils import verify_password

from server.utils.validation import validate_username
from server.utils.validation import validate_password
from server.utils.validation import validate_full_name

from shared.protocol import create_packet

from shared.events import (

    LOGIN_SUCCESS,

    LOGIN_FAILED,

    REGISTER_SUCCESS,

    REGISTER_FAILED

)



def register(data):

    """
    Creates a new user account.
    """

    username = data["username"].strip()

    password = data["password"]

    full_name = data["full_name"].strip()

    # -------------------------
    # Username validation
    # -------------------------

    valid, message = validate_username(
        username
    )

    if not valid:

        return create_packet(

            REGISTER_FAILED,

            {
                "message": message
            }

        )

    # -------------------------
    # Password validation
    # -------------------------

    valid, message = validate_password(
        password
    )

    if not valid:

        return create_packet(

            REGISTER_FAILED,

            {
                "message": message
            }

        )

    # -------------------------
    # Full name validation
    # -------------------------

    valid, message = validate_full_name(
        full_name
    )

    if not valid:

        return create_packet(

            REGISTER_FAILED,

            {
                "message": message
            }

        )

    password_hash = hash_password(
        password
    )

    result = create_user(

        username,

        password_hash,

        full_name

    )

    if result:

        return create_packet(

            REGISTER_SUCCESS,

            {

                "message":
                "Account created successfully."

            }

        )

    return create_packet(

        REGISTER_FAILED,

        {

            "message":
            "Username already exists."

        }

    )



def login(data):

    """
    Authenticates user.
    """

    user = get_user_by_username(

        data["username"]

    )

    if user is None:

        return create_packet(

            LOGIN_FAILED,

            {

                "message":
                "Invalid username or password."

            }

        )

    password_correct = verify_password(

        data["password"],

        user["password_hash"]

    )

    if password_correct:

        return create_packet(

            LOGIN_SUCCESS,

            {

                "user_id":
                user["user_id"],

                "username":
                user["username"],

                "full_name":
                user["full_name"]

            }

        )

    return create_packet(

        LOGIN_FAILED,

        {

            "message":
            "Invalid username or password."

        }

    )
