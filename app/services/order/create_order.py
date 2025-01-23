from sqlalchemy.orm import Session
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.Order import Order
from app.models.ShoppingCart import ShoppingCart
from typing import List, Dict


def create_order(user_id: int, cart_details: List[Dict[str, int]]) -> None:
    with next(get_sql_session()) as session:  # type: Session
        total_amount = 0.0

        # Calculate total amount and create order items
        for item in cart_details:
            product_id = item["product_id"]
            quantity = item["quantity"]

            # Assuming price is fetched from the product model
            product_price = session.query(ShoppingCart).filter_by(product_id=product_id).first().product.price.__float__()
            total_amount += product_price * quantity

        # Create the order
        new_order = Order(
            user_id=user_id,
            total_amount=total_amount,
            status="Pending"
        )
        session.add(new_order)
        session.commit()

        # Clear the shopping cart
        session.query(ShoppingCart).filter_by(user_id=user_id).delete()
        session.commit()
