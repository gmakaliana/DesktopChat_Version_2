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




    logout_button = tk.Button(

        window,

        text="Logout",

        command=logout

    )


    logout_button.pack(

        pady=20

    )