# server/auth/password_utils.py


"""
Server password security module.

Responsible for:
- hashing passwords
- verifying passwords

Passwords are never stored
as plain text.
"""


import bcrypt



def hash_password(password):

    """
    Converts plain password into
    secure bcrypt hash.

    Returns:
        hashed password
    """


    password_bytes = password.encode(
        "utf-8"
    )


    salt = bcrypt.gensalt()


    hashed_password = bcrypt.hashpw(

        password_bytes,

        salt

    )


    return hashed_password.decode(
        "utf-8"
    )



def verify_password(
        password,
        hashed_password
):

    """
    Checks if entered password
    matches stored bcrypt hash.

    Returns:
        True  - password correct
        False - password incorrect
    """


    password_bytes = password.encode(
        "utf-8"
    )


    stored_hash_bytes = hashed_password.encode(
        "utf-8"
    )


    return bcrypt.checkpw(

        password_bytes,

        stored_hash_bytes

    )