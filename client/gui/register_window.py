# client/gui/register_window.py


import tkinter as tk

from modules.utils.window_utils import center_window



def open_register_window(parent):

    """
    Opens registration window.

    Parent window is hidden while
    this window is active.
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


    label = tk.Label(

        window,

        text="Register New User"

    )


    label.pack(
        pady=50
    )


    def back():

        window.destroy()

        parent.deiconify()


    button = tk.Button(

        window,

        text="Back",

        command=back

    )


    button.pack()
