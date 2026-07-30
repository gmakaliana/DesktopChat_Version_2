# client/main.py


"""
Desktop Chat Client

Application entry point.

Startup sequence:

1. Create folders
2. Initialize database
3. Initialize networking
4. Open login window
"""


from modules.utils.app_paths import create_client_folders

from database.create_tables import create_tables

from modules.network.connection import initialize_network

from gui.login_window import open_login_window



def start_application():
    """
    Starts the Desktop Chat Client.
    """


    print(
        "Starting Desktop Chat Client..."
    )


    # Create required folders

    create_client_folders()



    # Initialize local database

    create_tables()



    # Prepare networking

    initialize_network()



    # Launch GUI

    open_login_window()




if __name__ == "__main__":

    start_application()
