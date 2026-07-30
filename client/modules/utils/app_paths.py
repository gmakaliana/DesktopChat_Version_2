# client/utils/app_paths.py


import os


def get_application_path():
    """
    Returns the main client application folder.

    This function will later support
    PyInstaller installations.
    """

    return os.path.dirname(
        os.path.abspath(__file__)
    )



def create_client_folders():
    """
    Creates required client folders.
    """

    folders = [

        "uploads",

        "uploads/images",

        "uploads/documents",

        "uploads/others",


        "downloads",

        "downloads/images",

        "downloads/documents",

        "downloads/others",


        "assets",

        "assets/icons",

        "assets/images"

    ]


    for folder in folders:

        if not os.path.exists(folder):

            os.makedirs(folder)


    print("Client folders initialized.")
    