# client/gui/login_window.py


"""
Login Window

Responsible for:
- collecting username/password
- sending login request
- opening home window after success

Authentication logic is handled
inside client/auth/login.py.
"""



import tkinter as tk

from tkinter import messagebox



from client.modules.utils.gui_theme import (

    BACKGROUND_COLOR,

    TITLE_FONT,

    NORMAL_FONT

)



from client.modules.utils.window_utils import (

    center_window,

    exit_application

)



from client.auth.login import login_user


from client.modules.users.users import set_current_user


from client.gui.home_window import open_home_window





def open_login_window():

    """
    Creates and opens the login window.
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





    # =====================================
    # Application Title
    # =====================================


    title = tk.Label(

        window,

        text="Desktop Chat System",

        font=TITLE_FONT,

        bg=BACKGROUND_COLOR

    )


    title.pack(

        pady=40

    )





    # =====================================
    # Username
    # =====================================


    username_label = tk.Label(

        window,

        text="Username",

        font=NORMAL_FONT,

        bg=BACKGROUND_COLOR

    )


    username_label.pack()



    username_entry = tk.Entry(

        window,

        font=NORMAL_FONT

    )


    username_entry.pack(

        pady=5

    )





    # =====================================
    # Password
    # =====================================


    password_label = tk.Label(

        window,

        text="Password",

        font=NORMAL_FONT,

        bg=BACKGROUND_COLOR

    )


    password_label.pack()



    password_entry = tk.Entry(

        window,

        show="*",

        font=NORMAL_FONT

    )


    password_entry.pack(

        pady=5

    )





    # =====================================
    # Login Action
    # =====================================


    def login_action():

        """
        Sends login request
        to authentication module.
        """



        username = username_entry.get()

        password = password_entry.get()




        if username == "" or password == "":


            messagebox.showwarning(

                "Missing Information",

                "Please enter username and password."

            )


            return





        response = login_user(

            username,

            password

        )





        if response is None:


            messagebox.showerror(

                "Connection Error",

                "Unable to communicate with server."

            )


            return





        if response.get("event") == "LOGIN_SUCCESS":



            user_data = response.get(

                "data"

            )



            set_current_user(

                user_data

            )



            open_home_window(

                window

            )





        else:


            messagebox.showerror(

                "Login Failed",

                "Invalid username or password."

            )







    # =====================================
    # Login Button
    # =====================================


    login_button = tk.Button(

        window,

        text="Login",

        command=login_action

    )


    login_button.pack(

        pady=20

    )





    # =====================================
    # Register Window
    # =====================================


    def open_register():

        """
        Opens registration window.
        """


        from client.gui.register_window import open_register_window



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