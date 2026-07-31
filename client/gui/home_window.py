"""
Home Window

Main application dashboard.
"""


import tkinter as tk


from client.modules.utils.window_utils import center_window


from client.modules.utils.gui_theme import (

    BACKGROUND_COLOR,

    TITLE_FONT,

    BUTTON_FONT,

    LOGOUT_BUTTON_COLOR

)


from client.modules.users.users import (

    clear_current_user,

    get_current_user

)


from client.modules.users.status import set_offline





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



    window.configure(

        bg=BACKGROUND_COLOR

    )





    title = tk.Label(

        window,

        text="Home Dashboard",

        font=TITLE_FONT,

        bg=BACKGROUND_COLOR

    )


    title.pack(

        pady=50

    )





    def logout():

        """
        Logout current user.
        """


        current_user = get_current_user()



        if current_user:


            set_offline(

                current_user["user_id"]

            )



        clear_current_user()



        window.destroy()



        login_window.deiconify()



        login_window.lift()



        login_window.focus_force()





    # =====================================
    # Logout Button
    # =====================================


    logout_button = tk.Button(

        window,

        text="Logout",

        command=logout,

        width=12,

        font=BUTTON_FONT,

        bg=LOGOUT_BUTTON_COLOR,

        fg="white",

        activebackground=LOGOUT_BUTTON_COLOR

    )


    logout_button.pack(

        pady=20

    )





    # =====================================
    # Prevent application exit
    # X behaves like Logout
    # =====================================


    window.protocol(

        "WM_DELETE_WINDOW",

        logout

    )