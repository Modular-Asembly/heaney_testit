from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.modassembly.database.sql.get_sql_session import Base
from app.models.User import User
from app.models.Product import Product


class ShoppingCart(Base):
    __tablename__ = "shopping_carts"

    cart_id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey(User.user_id), nullable=False)
    product_id: int = Column(Integer, ForeignKey(Product.product_id), nullable=False)
    quantity: int = Column(Integer, nullable=False)

    user = relationship("User", back_populates="shopping_carts")
    product = relationship("Product", back_populates="shopping_carts")
