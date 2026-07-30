# client/auth/password_utils.py


"""
Client password validation utilities.

This module does not store passwords.

The server is responsible for:
- bcrypt hashing
- password verification
"""


def validate_password(password):
    """
    Checks basic password requirements.
    """


    if password is None:
        return False


    if len(password) < 6:

        return False


    return True