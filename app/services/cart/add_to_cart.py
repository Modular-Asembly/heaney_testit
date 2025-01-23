from sqlalchemy.orm import Session
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.ShoppingCart import ShoppingCart


def add_to_cart(user_id: int, product_id: int, quantity: int) -> None:
    with next(get_sql_session()) as db:  # type: Session
        cart_item = ShoppingCart(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )
        db.add(cart_item)
        db.commit()
