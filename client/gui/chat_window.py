# client/gui/chat_window.py


"""
Chat Window

Responsible for displaying
conversations between users.

Future functionality:
- Load chat history
- Send messages
- Receive messages
- Upload files
"""


import tkinter as tk

from modules.utils.window_utils import center_window



def open_chat_window(parent_window):

    """
    Opens chat window.
    """


    parent_window.withdraw()


    window = tk.Toplevel()


    window.title(
        "Chat"
    )


    center_window(
        window,
        700,
        600
    )


    title = tk.Label(

        window,

        text="Chat Window",

        font=(
            "Arial",
            16,
            "bold"
        )

    )


    title.pack(
        pady=20
    )


    # Message display area

    message_area = tk.Text(

        window,

        height=20

    )


    message_area.pack(

        expand=True,

        fill="both",

        padx=20,

        pady=10

    )



    # Message input area

    message_input = tk.Entry(
        window
    )


    message_input.pack(

        fill="x",

        padx=20

    )



    send_button = tk.Button(

        window,

        text="Send"

    )


    send_button.pack(
        pady=10
    )



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


    back_button.pack()