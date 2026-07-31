# client/main.py


"""
Desktop Chat Client

Application entry point.

Startup sequence:

1. Create required folders
2. Initialize local database
3. Initialize networking
4. Open login window
"""


from client.modules.utils.app_paths import create_client_folders


from client.database.create_tables import create_tables


from client.modules.network.connection import initialize_network


from client.gui.login_window import open_login_window





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



    # Initialize networking

    network_started = initialize_network()

    if not network_started:

        print(
            "Could not connect to server."
        )

        return



    # Launch login window

    open_login_window()





if __name__ == "__main__":


    start_application()