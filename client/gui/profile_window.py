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


from client.modules.utils.gui_theme import (

    BACKGROUND_COLOR,

    TITLE_FONT,

    NORMAL_FONT,

    BUTTON_FONT,

    BACK_BUTTON_COLOR

)





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



    window.configure(

        bg=BACKGROUND_COLOR

    )





    # =====================================
    # Window Title
    # =====================================


    title = tk.Label(

        window,

        text="User Profile",

        font=TITLE_FONT,

        bg=BACKGROUND_COLOR

    )


    title.pack(

        pady=40

    )





    # =====================================
    # Profile Information
    # =====================================


    profile_label = tk.Label(

        window,

        text="Profile information will appear here.",

        font=NORMAL_FONT,

        bg=BACKGROUND_COLOR

    )


    profile_label.pack()





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

        pady=20

    )





    # =====================================
    # Prevent application exit
    # =====================================


    window.protocol(

        "WM_DELETE_WINDOW",

        back

    )