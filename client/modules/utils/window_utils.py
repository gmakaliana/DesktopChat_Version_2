# client/utils/window_utils.py


import tkinter as tk



def center_window(window, width, height):
    """
    Centers a window on the screen.
    """

    screen_width = window.winfo_screenwidth()

    screen_height = window.winfo_screenheight()


    x = int(
        (screen_width - width) / 2
    )


    y = int(
        (screen_height - height) / 2
    )


    window.geometry(
        f"{width}x{height}+{x}+{y}"
    )



def close_window(window):
    """
    Closes a specific window.
    """

    window.destroy()



def hide_window(window):
    """
    Temporarily hides a window.
    """

    window.withdraw()



def show_window(window):
    """
    Shows a hidden window.
    """

    window.deiconify()



def exit_application(window):
    """
    Completely closes application.
    """

    window.destroy()
    