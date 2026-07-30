# client/gui/home_window.py


"""
Home Window

Main application dashboard.

Future features:
- contacts
- chat list
- settings
- profile
"""


import tkinter as tk


from modules.utils.window_utils import center_window


from modules.users.users import clear_current_user



def open_home_window(login_window):

    """
    Opens the main dashboard.
    """


    login_window.withdraw()



    window = tk.Toplevel()



    window.title(

        "Desktop Chat System"

    )



    center_window(

        window,

        900,

        600

    )



    label = tk.Label(

        window,

        text="Home Dashboard",

        font=(

            "Arial",

            16,

            "bold"

        )

    )


    label.pack(

        pady=50

    )



    def logout():

        """
        Logs out current user.

        Server status update will be
        added when WebSocket networking
        is implemented.
        """


        clear_current_user()



        window.destroy()



        login_window.deiconify()



    logout_button = tk.Button(

        window,

        text="Logout",

        command=logout

    )


    logout_button.pack()