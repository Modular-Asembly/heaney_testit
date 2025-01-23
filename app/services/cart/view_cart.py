from typing import List, Dict
from sqlalchemy.orm import Session
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.ShoppingCart import ShoppingCart
from app.models.Product import Product


def view_cart(user_id: int) -> List[Dict[str, str]]:
    with get_sql_session() as session:
        cart_items = (
            session.query(ShoppingCart, Product)
            .join(Product, ShoppingCart.product_id == Product.product_id)
            .filter(ShoppingCart.user_id == user_id)
            .all()
        )

        cart_contents = [
            {
                "product_id": item.Product.product_id.__str__(),
                "name": item.Product.name.__str__(),
                "description": item.Product.description.__str__(),
                "price": item.Product.price.__str__(),
                "quantity": item.ShoppingCart.quantity.__str__(),
            }
            for item in cart_items
        ]

    return cart_contents
