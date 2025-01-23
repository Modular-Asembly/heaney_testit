from typing import Dict
from sqlalchemy.orm import Session
from app.auth.hash_password import hash_password
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.User import User


def register_user(user_data: Dict[str, str]) -> None:
    with next(get_sql_session()) as session:  # type: Session
        # Hash the user's password
        password_hash = hash_password(user_data["password"])

        # Create a new User instance
        new_user = User(
            email=user_data["email"],
            password_hash=password_hash.decode('utf-8')
        )

        # Add the new user to the session and commit
        session.add(new_user)
        session.commit()
