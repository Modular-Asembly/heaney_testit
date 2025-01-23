import os
from typing import Dict, Any
import stripe

stripe.api_key = os.environ["STRIPE_API_KEY"]

def process_payment(payment_details: Dict[str, Any]) -> Dict[str, Any]:
    """
    Processes a payment using Stripe.

    Args:
        payment_details (Dict[str, Any]): A dictionary containing payment details such as amount, currency, and source.

    Returns:
        Dict[str, Any]: A dictionary containing the payment confirmation or error details.
    """
    try:
        charge = stripe.Charge.create(
            amount=payment_details["amount"],
            currency=payment_details["currency"],
            source=payment_details["source"],
            description=payment_details.get("description", "E-commerce transaction")
        )
        return {"status": "success", "charge_id": charge.id}
    except stripe.error.StripeError as e:
        return {"status": "error", "message": str(e)}
