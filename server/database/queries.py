# server/database/queries.py


"""
This file contains database query functions.

The server business logic will call these
functions instead of writing SQL directly.
"""


from database.db import get_connection



def check_database():
    """
    Test database connection.
    """

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )


    tables = cursor.fetchall()


    connection.close()


    return tables

