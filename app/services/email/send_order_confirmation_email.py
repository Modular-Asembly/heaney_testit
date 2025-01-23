import os
from app.modassembly.email.get_email_client import get_email_client
from app.models.Order import Order

def send_order_confirmation_email(order: Order, user_email: str) -> bool:
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ["SMTP_PORT"])
    username = os.environ["SMTP_USERNAME"]
    password = os.environ["SMTP_PASSWORD"]

    email_client = get_email_client(smtp_server, smtp_port, username, password)
    
    subject = f"Order Confirmation - Order #{order.order_id.__str__()}"
    body = (
        f"Dear Customer,\n\n"
        f"Thank you for your order #{order.order_id.__str__()}.\n"
        f"Total Amount: ${order.total_amount.__str__()}\n"
        f"Status: {order.status.__str__()}\n\n"
        f"Best regards,\n"
        f"Your E-commerce Team"
    )

    return email_client.send_email(to_email=user_email, subject=subject, body=body)
