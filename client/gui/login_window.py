# client/gui/login_window.py


"""
Login Window

Responsible for:
- collecting username and password
- sending login request
- opening home window after success

Authentication logic is handled
inside client/auth/login.py.
"""


import tkinter as tk

from tkinter import messagebox


from modules.utils.gui_theme import (

    BACKGROUND_COLOR,

    TITLE_FONT,

    NORMAL_FONT

)


from modules.utils.window_utils import (

    center_window,

    exit_application

)


from auth.login import login_user


from modules.users.users import set_current_user


from gui.home_window import open_home_window



def open_login_window():

    """
    Opens the main login window.
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



    def login_action():

        """
        Handles login button click.
        """


        username_value = username.get()

        password_value = password.get()



        response = login_user(

            username_value,

            password_value

        )



        if response["success"]:


            # Save logged-in user

            set_current_user(

                response["user"]

            )


            # Open dashboard

            open_home_window(

                window

            )



        else:


            messagebox.showerror(

                "Login Failed",

                "Invalid username or password."

            )



    login_button = tk.Button(

        window,

        text="Login",

        command=login_action

    )


    login_button.pack(

        pady=20

    )



    def open_register():

        """
        Opens registration window.
        """


        from gui.register_window import open_register_window


        open_register_window(

            window

        )



    register_button = tk.Button(

        window,

        text="Register",

        command=open_register

    )


    register_button.pack()



    window.mainloop()