# client/gui/settings_window.py


"""
Settings Window

Application preferences.

Future features:
- Theme
- Notifications
- Download folder
- Font size
"""


import tkinter as tk

from client.modules.utils.window_utils import center_window



def open_settings_window(parent_window):

    """
    Opens settings window.
    """


    parent_window.withdraw()


    window = tk.Toplevel()


    window.title(
        "Settings"
    )


    center_window(
        window,
        500,
        400
    )


    title = tk.Label(

        window,

        text="Application Settings",

        font=(
            "Arial",
            16,
            "bold"
        )

    )


    title.pack(
        pady=40
    )


    settings_label = tk.Label(

        window,

        text="Settings will be implemented later."

    )


    settings_label.pack()



    def back():

        """
        Return to previous window.
        """

        window.destroy()

        parent_window.deiconify()



    back_button = tk.Button(

        window,

        text="Back",

        command=back

    )


    back_button.pack(
        pady=20
    )