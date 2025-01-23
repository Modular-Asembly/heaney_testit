from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from app.services.email.send_order_confirmation_email import send_order_confirmation_email
from app.services.email.send_order_update_email import send_order_update_email

router = APIRouter()

class OrderEmailRequest(BaseModel):
    order_id: int
    user_email: str
    email_type: str  # "confirmation" or "update"
    order_details: Dict[str, Any]

class OrderEmailResponse(BaseModel):
    status: str
    message: str

@router.post("/order/email", response_model=OrderEmailResponse)
def order_email_endpoint(request: OrderEmailRequest) -> OrderEmailResponse:
    """
    Endpoint to send order emails.

    - **order_id**: The ID of the order.
    - **user_email**: The email address of the user.
    - **email_type**: The type of email to send ("confirmation" or "update").
    - **order_details**: Additional details about the order.
    """
    if request.email_type == "confirmation":
        success = send_order_confirmation_email(request.order_details, request.user_email)
    elif request.email_type == "update":
        success = send_order_update_email(request.order_details, request.user_email)
    else:
        raise HTTPException(status_code=400, detail="Invalid email type")

    if success:
        return OrderEmailResponse(status="success", message="Email sent successfully")
    else:
        raise HTTPException(status_code=500, detail="Failed to send email")
