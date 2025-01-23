import os
from app.modassembly.email.get_email_client import get_email_client
from app.models.Order import Order

def send_order_update_email(order: Order, user_email: str) -> bool:
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ["SMTP_PORT"])
    username = os.environ["SMTP_USERNAME"]
    password = os.environ["SMTP_PASSWORD"]

    email_client = get_email_client(smtp_server, smtp_port, username, password)
    if email_client is None:
        raise ValueError("Failed to initialize EmailClient")

    subject = f"Order Update: {order.order_id.__str__()}"
    body = f"Dear Customer,\n\nYour order with ID {order.order_id.__str__()} has been updated.\n\nStatus: {order.status.__str__()}\nTotal Amount: {order.total_amount.__str__()}\n\nThank you for shopping with us!"

    return email_client.send_email(to_email=user_email, subject=subject, body=body, is_html=False)
