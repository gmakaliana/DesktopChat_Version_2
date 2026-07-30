# client/gui/home_window.py


import tkinter as tk

from modules.utils.window_utils import center_window



def open_home_window(login_window):

    """
    Main application dashboard.
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

        text="Home Dashboard"

    )


    label.pack(
        pady=50
    )


    def logout():

        window.destroy()

        login_window.deiconify()


    logout_button = tk.Button(

        window,

        text="Logout",

        command=logout

    )


    logout_button.pack()