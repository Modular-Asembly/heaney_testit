from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.modassembly.database.sql.get_sql_session import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
