# client/database/db.py


import sqlite3


DATABASE_NAME = "client_data.db"



def get_connection():
    """
    Creates a connection to the
    local client database.
    """

    connection = sqlite3.connect(
        DATABASE_NAME
    )


    connection.row_factory = sqlite3.Row


    return connection
