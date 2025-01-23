import os
from typing import Dict, Optional
import jwt
from sqlalchemy.orm import Session
from app.auth.verify_password import verify_password
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.User import User


def login_user(email: str, password: str) -> Optional[str]:
    with next(get_sql_session()) as session:  # type: Session
        user: Optional[User] = session.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.password_hash.__str__()):
            # Generate JWT token
            payload: Dict[str, str] = {"user_id": user.user_id.__str__(), "email": user.email.__str__()}
            token: str = jwt.encode(payload, os.environ["JWT_SECRET_KEY"], algorithm="HS256")
            return token
    return None
