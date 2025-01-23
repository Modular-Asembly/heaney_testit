import bcrypt
from typing import Union


def verify_password(plain_password: str, hashed_password: Union[bytes, str]) -> bool:
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)
