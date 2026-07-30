# client/gui/login_window.py


import tkinter as tk



def open_login_window():

    """
    Opens the application login window.

    Authentication will be added later.
    """


    window = tk.Tk()


    window.title(
        "Desktop Chat System"
    )


    window.geometry(
        "450x350"
    )


    label = tk.Label(

        window,

        text="Desktop Chat System\nLogin Window",

        font=(
            "Arial",
            16
        )

    )


    label.pack(
        pady=100
    )


    window.mainloop()

    