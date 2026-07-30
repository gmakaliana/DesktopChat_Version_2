# client/modules/users/users.py


"""
Client user session manager.

Stores information about
the currently logged-in user.
"""


current_user = None



def set_current_user(user):

    """
    Saves logged-in user information.
    """

    global current_user

    current_user = user



def get_current_user():

    """
    Returns current logged-in user.
    """

    return current_user



def clear_current_user():

    """
    Removes current user session.
    """

    global current_user

    current_user = None