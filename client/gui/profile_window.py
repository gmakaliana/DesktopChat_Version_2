# client/gui/profile_window.py


"""
Profile Window

Handles user profile information.

Future features:
- Profile picture
- Display name
- Password management
- Personal information
"""


import tkinter as tk

from client.modules.utils.window_utils import center_window



def open_profile_window(parent_window):

    """
    Opens profile window.
    """


    parent_window.withdraw()


    window = tk.Toplevel()


    window.title(
        "Profile"
    )


    center_window(
        window,
        500,
        450
    )


    title = tk.Label(

        window,

        text="User Profile",

        font=(
            "Arial",
            16,
            "bold"
        )

    )


    title.pack(
        pady=40
    )


    profile_label = tk.Label(

        window,

        text="Profile information will appear here."

    )


    profile_label.pack()



    def back():

        """
        Return to previous window.
        """

        window.destroy()

        parent_window.deiconify()



    back_button = tk.Button(

        window,

        text="Back",

        command=back

    )


    back_button.pack(
        pady=20
    )