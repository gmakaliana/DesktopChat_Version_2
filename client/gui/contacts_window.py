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


from client.modules.utils.gui_theme import (

    BACKGROUND_COLOR,

    TITLE_FONT,

    NORMAL_FONT,

    BUTTON_FONT,

    BACK_BUTTON_COLOR

)





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



    window.configure(

        bg=BACKGROUND_COLOR

    )





    # =====================================
    # Window Title
    # =====================================


    title = tk.Label(

        window,

        text="Contacts",

        font=TITLE_FONT,

        bg=BACKGROUND_COLOR

    )


    title.pack(

        pady=30

    )





    # =====================================
    # Contact List
    # =====================================


    contact_list = tk.Listbox(

        window,

        font=NORMAL_FONT

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





    # =====================================
    # Back Button
    # =====================================


    back_button = tk.Button(

        window,

        text="Back",

        command=back,

        width=12,

        font=BUTTON_FONT,

        bg=BACK_BUTTON_COLOR,

        fg="white",

        activebackground=BACK_BUTTON_COLOR

    )


    back_button.pack(

        pady=10

    )





    # =====================================
    # Prevent application exit
    # =====================================


    window.protocol(

        "WM_DELETE_WINDOW",

        back

    )