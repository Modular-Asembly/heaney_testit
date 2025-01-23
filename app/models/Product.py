from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.modassembly.database.sql.get_sql_session import Base


class Product(Base):
    __tablename__ = "products"

    product_id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True, nullable=False)
    description: str = Column(String, nullable=True)
    price: float = Column(Float, nullable=False)
    stock: int = Column(Integer, nullable=False)

    # Relationships can be added here if needed, for example:
    # orders = relationship("Order", back_populates="product")
