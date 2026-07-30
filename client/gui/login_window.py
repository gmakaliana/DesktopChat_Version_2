# client/gui/login_window.py


import tkinter as tk

from modules.utils.gui_theme import (
    BACKGROUND_COLOR,
    TITLE_FONT,
    NORMAL_FONT
)

from modules.utils.window_utils import (
    center_window,
    exit_application
)



def open_login_window():

    """
    Opens the login window.

    Authentication will be added
    in Phase 6.
    """


    window = tk.Tk()


    window.title(
        "Desktop Chat System"
    )


    center_window(
        window,
        450,
        350
    )


    window.configure(
        bg=BACKGROUND_COLOR
    )


    window.protocol(
        "WM_DELETE_WINDOW",
        lambda: exit_application(window)
    )


    title = tk.Label(

        window,

        text="Desktop Chat System",

        font=TITLE_FONT,

        bg=BACKGROUND_COLOR

    )


    title.pack(
        pady=40
    )


    username = tk.Entry(
        window,
        font=NORMAL_FONT
    )

    username.pack(
        pady=5
    )


    password = tk.Entry(
        window,
        show="*",
        font=NORMAL_FONT
    )

    password.pack(
        pady=5
    )


    login_button = tk.Button(

        window,

        text="Login"

    )


    login_button.pack(
        pady=20
    )


    register_button = tk.Button(

        window,

        text="Register"

    )


    register_button.pack()


    window.mainloop()