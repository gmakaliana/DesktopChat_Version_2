# client/gui/home_window.py


"""
Home Window

Main application dashboard.
"""


import tkinter as tk

from client.modules.utils.window_utils import center_window

from client.modules.users.users import (
    clear_current_user,
    get_current_user
)


def open_home_window(login_window):
    """
    Opens dashboard.
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
        text="Home Dashboard",
        font=(
            "Arial",
            16,
            "bold"
        )
    )

    label.pack(
        pady=50
    )

    def logout():
        """
        Logout current user.
        """

        from client.modules.network.connection import send_request

        from shared.protocol import create_packet

        from shared.events import LOGOUT

        current_user = get_current_user()

        packet = create_packet(

            LOGOUT,

            {
                "user_id": current_user["user_id"]
            }

        )

        send_request(
            packet
        )

        clear_current_user()

        window.destroy()

        login_window.deiconify()

    logout_button = tk.Button(

        window,

        text="Logout",

        command=logout

    )

    logout_button.pack()