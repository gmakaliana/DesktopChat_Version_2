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


from client.modules.utils.window_utils import center_window


from client.modules.utils.gui_theme import (

    BACKGROUND_COLOR,

    TITLE_FONT,

    NORMAL_FONT,

    BUTTON_FONT,

    SEND_BUTTON_COLOR,

    BACK_BUTTON_COLOR

)





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



    window.configure(

        bg=BACKGROUND_COLOR

    )





    title = tk.Label(

        window,

        text="Chat Window",

        font=TITLE_FONT,

        bg=BACKGROUND_COLOR

    )


    title.pack(

        pady=20

    )





    # =====================================
    # Message Display Area
    # =====================================


    message_area = tk.Text(

        window,

        height=20,

        font=NORMAL_FONT

    )


    message_area.pack(

        expand=True,

        fill="both",

        padx=20,

        pady=10

    )





    # =====================================
    # Message Input Area
    # =====================================


    message_input = tk.Entry(

        window,

        font=NORMAL_FONT

    )


    message_input.pack(

        fill="x",

        padx=20,

        pady=5

    )





    # =====================================
    # Send Button
    # =====================================


    send_button = tk.Button(

        window,

        text="Send",

        width=12,

        font=BUTTON_FONT,

        bg=SEND_BUTTON_COLOR,

        fg="white",

        activebackground=SEND_BUTTON_COLOR

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





    # =====================================
    # Back Button
    # =====================================


    back_button = tk.Button(

        window,

        text="Back",

        command=back,

        width=12,

        font=BUTTON_FONT,

        bg=BACK_BUTTON_COLOR,

        fg="white",

        activebackground=BACK_BUTTON_COLOR

    )


    back_button.pack(

        pady=10

    )





    # =====================================
    # Prevent application exit
    # =====================================


    window.protocol(

        "WM_DELETE_WINDOW",

        back

    )