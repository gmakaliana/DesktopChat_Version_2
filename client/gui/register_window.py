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

    # Window title

    title = tk.Label(
        window,
        text="Register New User"
    )

    title.pack(
        pady=30
    )

    # Username label

    username_label = tk.Label(
        window,
        text="Username"
    )

    username_label.pack()

    # Username input

    username = tk.Entry(window)

    username.pack(
        pady=5
    )

    # Full name label

    full_name_label = tk.Label(
        window,
        text="Full Name"
    )

    full_name_label.pack()

    # Full name input

    full_name = tk.Entry(window)

    full_name.pack(
        pady=5
    )

    # Password label

    password_label = tk.Label(
        window,
        text="Password"
    )

    password_label.pack()

    # Password input

    password = tk.Entry(
        window,
        show="*"
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

        # No response received

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



    # Register button

    register_button = tk.Button(

        window,

        text="Register",

        command=register_action

    )

    register_button.pack(

        pady=20

    )



    def back():

        """
        Returns to login window.
        """

        window.destroy()

        parent.deiconify()



    # Back button

    back_button = tk.Button(

        window,

        text="Back",

        command=back

    )

    back_button.pack()