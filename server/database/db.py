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
