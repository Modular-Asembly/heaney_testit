from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Dict
from app.services.cart.add_to_cart import add_to_cart
from app.services.cart.view_cart import view_cart

router = APIRouter()

class AddToCartRequest(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class CartItemResponse(BaseModel):
    product_id: int
    name: str
    description: str
    price: float
    quantity: int

@router.post("/cart/add", response_model=dict)
def add_to_cart_endpoint(request: AddToCartRequest) -> dict:
    """
    Add a product to the shopping cart.

    - **user_id**: ID of the user
    - **product_id**: ID of the product to add
    - **quantity**: Quantity of the product to add
    """
    add_to_cart(request.user_id, request.product_id, request.quantity)
    return {"status": "success", "message": "Product added to cart"}

@router.get("/cart/view", response_model=List[CartItemResponse])
def view_cart_endpoint(user_id: int) -> List[CartItemResponse]:
    """
    View the contents of the shopping cart for a user.

    - **user_id**: ID of the user
    """
    cart_contents = view_cart(user_id)
    if not cart_contents:
        raise HTTPException(status_code=404, detail="Cart is empty")
    return cart_contents
