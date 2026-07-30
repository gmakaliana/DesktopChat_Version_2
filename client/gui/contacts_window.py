# client/gui/contacts_window.py


"""
Contacts Window

Responsible for displaying and managing
user contacts.

Future functionality:
- Search users
- Add contacts
- Remove contacts
- Display online status
"""


import tkinter as tk

from client.modules.utils.window_utils import center_window



def open_contacts_window(parent_window):

    """
    Opens the contacts window.

    The parent window is hidden while
    this window is active.
    """


    parent_window.withdraw()


    window = tk.Toplevel()


    window.title(
        "Contacts"
    )


    center_window(
        window,
        500,
        500
    )


    title = tk.Label(

        window,

        text="Contacts",

        font=(
            "Arial",
            16,
            "bold"
        )

    )


    title.pack(
        pady=30
    )


    # Placeholder contact list

    contact_list = tk.Listbox(
        window
    )


    contact_list.pack(
        expand=True,
        fill="both",
        padx=20,
        pady=20
    )


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
        pady=10
    )