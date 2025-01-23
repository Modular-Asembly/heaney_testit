from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.modassembly.database.sql.get_sql_session import Base
from app.models.User import User


class Order(Base):
    __tablename__ = "orders"

    order_id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey(User.user_id), nullable=False)
    total_amount: float = Column(Float, nullable=False)
    status: str = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="orders")
