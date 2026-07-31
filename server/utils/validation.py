"""
Server validation utilities.

Responsible for validating:

- username
- password
- full name

These validations protect the
server from invalid data even if
client-side validation is bypassed.
"""


import re


def validate_username(username):
    """
    Validates username.

    Rules:
    - Required
    - 3 to 20 characters
    - Letters, numbers and underscores only

    Returns:
        (True, "")
        (False, error_message)
    """

    username = username.strip()

    if username == "":

        return (
            False,
            "Username is required."
        )

    if len(username) < 3:

        return (
            False,
            "Username must be at least 3 characters."
        )

    if len(username) > 20:

        return (
            False,
            "Username cannot exceed 20 characters."
        )

    if not re.fullmatch(
        r"[A-Za-z0-9_]+",
        username
    ):

        return (
            False,
            "Username may contain only letters, numbers and underscores."
        )

    return (
        True,
        ""
    )


def validate_full_name(full_name):
    """
    Validates full name.

    Rules:
    - Required
    - 3 to 100 characters
    - Letters and spaces only

    Returns:
        (True, "")
        (False, error_message)
    """

    full_name = full_name.strip()

    if full_name == "":

        return (
            False,
            "Full name is required."
        )

    if len(full_name) < 3:

        return (
            False,
            "Full name must be at least 3 characters."
        )

    if len(full_name) > 100:

        return (
            False,
            "Full name cannot exceed 100 characters."
        )

    if not re.fullmatch(
        r"[A-Za-z ]+",
        full_name
    ):

        return (
            False,
            "Full name may contain only letters and spaces."
        )

    return (
        True,
        ""
    )


def validate_password(password):
    """
    Validates password.

    Rules:
    - Required
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character

    Returns:
        (True, "")
        (False, error_message)
    """

    if password == "":

        return (
            False,
            "Password is required."
        )

    if len(password) < 8:

        return (
            False,
            "Password must be at least 8 characters long."
        )

    if not re.search(
        r"[A-Z]",
        password
    ):

        return (
            False,
            "Password must contain at least one uppercase letter."
        )

    if not re.search(
        r"[a-z]",
        password
    ):

        return (
            False,
            "Password must contain at least one lowercase letter."
        )

    if not re.search(
        r"[0-9]",
        password
    ):

        return (
            False,
            "Password must contain at least one number."
        )

    if not re.search(
        r"[!@#$%^&*()_\-+=\[\]{}|\\:;\"'<>,.?/`~]",
        password
    ):

        return (
            False,
            "Password must contain at least one special character."
        )

    return (
        True,
        ""
    )