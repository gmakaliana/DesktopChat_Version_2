# client/database/create_tables.py


from client.database.db import get_connection



def create_tables():
    """
    Creates local client database tables.
    """

    connection = get_connection()

    cursor = connection.cursor()



    # Stores locally cached users

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cached_users (

            user_id INTEGER PRIMARY KEY,

            username TEXT,

            full_name TEXT,

            status TEXT,

            last_seen DATETIME

        )
    """)



    # Stores local application settings

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (

            setting_id INTEGER PRIMARY KEY AUTOINCREMENT,

            setting_name TEXT UNIQUE,

            setting_value TEXT

        )
    """)



    connection.commit()

    connection.close()


    print("Client database initialized.")
    