# server/auth/authentication.py


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

    Data received:

    {
        username,
        password,
        full_name
    }

    Password is hashed before storage.
    """


    password_hash = hash_password(

        data["password"]

    )


    result = create_user(

        data["username"],

        password_hash,

        data["full_name"]

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

    Checks:
    - username exists
    - password matches hash
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