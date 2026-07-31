"""
Register Window

Responsible for:
- collecting new user details
- sending registration request

Registration logic is handled
inside client/auth/register.py.
"""


import tkinter as tk

from tkinter import messagebox


from client.modules.utils.window_utils import center_window


from client.modules.utils.gui_theme import (

    BACKGROUND_COLOR,

    TITLE_FONT,

    NORMAL_FONT,

    BUTTON_FONT,

    LOGIN_BUTTON_COLOR,

    REGISTER_BUTTON_COLOR

)


from client.auth.register import register_user


from shared.events import (

    REGISTER_SUCCESS,

    REGISTER_FAILED

)





def open_register_window(parent):

    """
    Opens registration window.
    """


    parent.withdraw()



    window = tk.Toplevel()



    window.title(
        "Register"
    )



    center_window(

        window,

        450,

        400

    )



    window.configure(

        bg=BACKGROUND_COLOR

    )





    title = tk.Label(

        window,

        text="Register New User",

        font=TITLE_FONT,

        bg=BACKGROUND_COLOR

    )


    title.pack(

        pady=30

    )





    username_label = tk.Label(

        window,

        text="Username",

        font=NORMAL_FONT,

        bg=BACKGROUND_COLOR

    )


    username_label.pack()



    username = tk.Entry(

        window,

        font=NORMAL_FONT

    )


    username.pack(

        pady=5

    )





    full_name_label = tk.Label(

        window,

        text="Full Name",

        font=NORMAL_FONT,

        bg=BACKGROUND_COLOR

    )


    full_name_label.pack()



    full_name = tk.Entry(

        window,

        font=NORMAL_FONT

    )


    full_name.pack(

        pady=5

    )





    password_label = tk.Label(

        window,

        text="Password",

        font=NORMAL_FONT,

        bg=BACKGROUND_COLOR

    )


    password_label.pack()



    password = tk.Entry(

        window,

        show="*",

        font=NORMAL_FONT

    )


    password.pack(

        pady=5

    )





    def register_action():

        """
        Handles registration.
        """



        response = register_user(

            username.get(),

            password.get(),

            full_name.get()

        )



        if response is None:


            messagebox.showerror(

                "Connection Error",

                "No response received from the server."

            )


            return



        event = response.get(

            "event"

        )


        data = response.get(

            "data",

            {}

        )



        if event == REGISTER_SUCCESS:


            messagebox.showinfo(

                "Success",

                data.get(

                    "message",

                    "Account created successfully."

                )

            )



            window.destroy()



            parent.deiconify()



        elif event == REGISTER_FAILED:


            messagebox.showerror(

                "Registration Failed",

                data.get(

                    "message",

                    "Registration failed."

                )

            )



        else:


            messagebox.showerror(

                "Server Error",

                "Unexpected response received from the server."

            )





    def back():

        """
        Returns to login window.
        """



        window.destroy()



        parent.deiconify()



        parent.lift()



        parent.focus_force()





    # =====================================
    # Buttons
    # =====================================


    button_frame = tk.Frame(

        window,

        bg=BACKGROUND_COLOR

    )


    button_frame.pack(

        pady=25

    )





    # Register button LEFT


    register_button = tk.Button(

        button_frame,

        text="Register",

        command=register_action,

        width=12,

        font=BUTTON_FONT,

        bg=REGISTER_BUTTON_COLOR,

        fg="white",

        activebackground=REGISTER_BUTTON_COLOR

    )


    register_button.pack(

        side="left",

        padx=10

    )





    # Login button RIGHT


    login_button = tk.Button(

        button_frame,

        text="Login",

        command=back,

        width=12,

        font=BUTTON_FONT,

        bg=LOGIN_BUTTON_COLOR,

        fg="white",

        activebackground=LOGIN_BUTTON_COLOR

    )


    login_button.pack(

        side="right",

        padx=10

    )





    # =====================================
    # Prevent application exit
    # =====================================


    window.protocol(

        "WM_DELETE_WINDOW",

        back

    )