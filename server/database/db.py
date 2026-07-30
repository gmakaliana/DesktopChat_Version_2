# server/database/db.py

import sqlite3


# Name of the server database file
DATABASE_NAME = "server_chat.db"


def get_connection():
    """
    Creates and returns a connection
    to the server SQLite database.
    """

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    # Allows accessing columns by name
    connection.row_factory = sqlite3.Row

    return connection

# server/database/queries.py


"""
Server database query functions.

The server uses this module
instead of writing SQL directly.
"""


#from server.database.db import get_connection



def create_user(
        username,
        password_hash,
        full_name
):

    """
    Creates a new user account.
    """


    connection = get_connection()

    cursor = connection.cursor()


    try:

        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                password_hash,
                full_name
            )

            VALUES (?, ?, ?)

            """,

            (
                username,
                password_hash,
                full_name
            )
        )


        connection.commit()


        return True


    except Exception as error:


        print(
            "Create user error:",
            error
        )


        return False


    finally:

        connection.close()



def get_user_by_username(username):

    """
    Finds user by username.
    """


    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?

        """,

        (
            username,
        )
    )


    user = cursor.fetchone()


    connection.close()


    return user



def update_user_status(
        user_id,
        status
):

    """
    Updates user online status.
    """


    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        """
        UPDATE users

        SET status = ?

        WHERE user_id = ?

        """,

        (
            status,
            user_id
        )
    )


    connection.commit()


    connection.close()


    return True