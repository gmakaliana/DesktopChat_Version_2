# client/gui/register_window.py


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


from modules.utils.window_utils import center_window


from auth.register import register_user



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



    title = tk.Label(

        window,

        text="Register New User"

    )


    title.pack(

        pady=30

    )



    username = tk.Entry(window)

    username.pack(
        pady=5
    )



    full_name = tk.Entry(window)

    full_name.pack(
        pady=5
    )



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



        if response["success"]:


            messagebox.showinfo(

                "Success",

                "Account created successfully."

            )


            window.destroy()

            parent.deiconify()



        else:


            messagebox.showerror(

                "Error",

                "Registration failed."

            )



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



    back_button = tk.Button(

        window,

        text="Back",

        command=back

    )


    back_button.pack()