# server/database/queries.py


"""
Database query functions.

Authentication and server logic
use these functions instead of
writing SQL directly.
"""


from server.database.db import get_connection


def create_user(
        username,
        password_hash,
        full_name
):
    """
    Creates a new user.
    """

    connection = get_connection()

    cursor = connection.cursor()

    try:

        cursor.execute("""

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
        ))

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

    cursor.execute("""

        SELECT *

        FROM users

        WHERE username = ?

    """,

    (
        username,
    ))

    user = cursor.fetchone()

    connection.close()

    return user


def update_user_status(
        user_id,
        status
):
    """
    Updates user's online status.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""

        UPDATE users

        SET status = ?

        WHERE user_id = ?

    """,

    (
        status,
        user_id
    ))

    connection.commit()

    connection.close()

    return True


def update_last_seen(user_id):
    """
    Updates last seen timestamp.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""

        UPDATE users

        SET last_seen = CURRENT_TIMESTAMP

        WHERE user_id = ?

    """,

    (
        user_id,
    ))

    connection.commit()

    connection.close()

    return True