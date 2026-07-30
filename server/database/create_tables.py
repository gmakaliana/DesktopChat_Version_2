# server/database/create_tables.py


"""
Creates all server database tables.

The server database is the permanent
source of truth for:
- users
- contacts
- chats
- files
"""


from server.database.db import get_connection



def create_tables():

    """
    Creates required database tables.
    """


    connection = get_connection()


    cursor = connection.cursor()



    # ================================
    # USERS TABLE
    # ================================


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            user_id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password_hash TEXT NOT NULL,

            full_name TEXT NOT NULL,

            profile_picture TEXT,

            status TEXT DEFAULT 'Offline',

            last_seen DATETIME,

            created_at DATETIME DEFAULT CURRENT_TIMESTAMP

        )
    """)



    # ================================
    # CONTACTS TABLE
    # ================================


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (

            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            contact_user_id INTEGER NOT NULL,


            FOREIGN KEY(user_id)
            REFERENCES users(user_id),


            FOREIGN KEY(contact_user_id)
            REFERENCES users(user_id)

        )
    """)



    # ================================
    # CHATS TABLE
    # ================================


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (

            chat_id INTEGER PRIMARY KEY AUTOINCREMENT,

            sender_id INTEGER NOT NULL,

            receiver_id INTEGER NOT NULL,

            message TEXT,

            message_type TEXT DEFAULT 'text',

            file_name TEXT,

            sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            is_read INTEGER DEFAULT 0,


            FOREIGN KEY(sender_id)
            REFERENCES users(user_id),


            FOREIGN KEY(receiver_id)
            REFERENCES users(user_id)

        )
    """)



    # ================================
    # FILES TABLE
    # ================================


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (

            file_id INTEGER PRIMARY KEY AUTOINCREMENT,

            sender_id INTEGER NOT NULL,

            receiver_id INTEGER NOT NULL,

            original_name TEXT,

            stored_name TEXT,

            file_type TEXT,

            file_size INTEGER,

            uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,


            FOREIGN KEY(sender_id)
            REFERENCES users(user_id),


            FOREIGN KEY(receiver_id)
            REFERENCES users(user_id)

        )
    """)



    connection.commit()


    connection.close()


    print(
        "Server database tables created successfully."
    )