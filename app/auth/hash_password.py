import bcrypt
from typing import Union


def hash_password(plain_password: Union[str, bytes]) -> bytes:
    """
    Takes a plain text password and returns a hashed version of the password.
    """
    if isinstance(plain_password, str):
        plain_password = plain_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password, salt)
    return hashed_password
