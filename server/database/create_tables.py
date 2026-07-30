# server/database/create_tables.py

from database.db import get_connection


def create_tables():
    """
    Creates all required database tables
    for the Desktop Chat Server.
    """

    connection = get_connection()

    cursor = connection.cursor()


    # =====================================
    # Users Table
    # Stores all registered users
    # =====================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            user_id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password_hash TEXT NOT NULL,

            full_name TEXT,

            profile_picture TEXT,

            status TEXT DEFAULT 'Offline',

            last_seen DATETIME,

            created_at DATETIME DEFAULT CURRENT_TIMESTAMP

        )
    """)



    # =====================================
    # Contacts Table
    # Stores user relationships
    # =====================================

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



    # =====================================
    # Chats Table
    # Stores messages
    # =====================================

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



    # =====================================
    # Files Table
    # Stores uploaded file information
    # =====================================

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


    # Save changes
    connection.commit()


    # Close connection
    connection.close()


    print("Server database tables created successfully.")
    