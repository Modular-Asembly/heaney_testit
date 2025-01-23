from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.services.payment.process_payment import process_payment
from app.services.order.create_order import create_order
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class PaymentDetails(BaseModel):
    amount: int
    currency: str
    source: str
    description: str

class CartItem(BaseModel):
    product_id: int
    quantity: int

class OrderRequest(BaseModel):
    user_id: int
    payment_details: PaymentDetails
    cart_details: List[CartItem]

class OrderResponse(BaseModel):
    status: str
    message: str

@router.post("/process_order", response_model=OrderResponse)
def order_processing_endpoint(order_request: OrderRequest, db: Session = Depends(get_sql_session)) -> OrderResponse:
    """
    Endpoint to process an order.
    
    - **order_request**: OrderRequest object containing user ID, payment details, and cart details.
    
    Returns an OrderResponse object with the status and message.
    """
    # Process payment
    payment_result = process_payment(order_request.payment_details.dict())
    if payment_result["status"] != "success":
        raise HTTPException(status_code=400, detail=payment_result["message"])

    # Create order
    create_order(order_request.user_id, [item.dict() for item in order_request.cart_details])

    return OrderResponse(status="success", message="Order processed successfully.")
