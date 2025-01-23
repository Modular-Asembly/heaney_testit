from typing import Optional
from sqlalchemy.orm import Session
from google.cloud import storage
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.modassembly.storage.get_gcs_bucket import get_gcp_bucket
from app.models.Product import Product


def update_product(
    db: Session, product_id: int, name: Optional[str] = None, description: Optional[str] = None,
    price: Optional[float] = None, stock: Optional[int] = None, image_data: Optional[bytes] = None
) -> None:
    # Fetch the product from the database
    product: Optional[Product] = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise ValueError("Product not found")

    # Update product fields if new values are provided
    if name is not None:
        product.name = name
    if description is not None:
        product.description = description
    if price is not None:
        product.price = price
    if stock is not None:
        product.stock = stock

    # Commit the changes to the database
    db.commit()

    # Update image in CloudStorage if provided
    if image_data is not None:
        bucket = get_gcp_bucket()
        blob = bucket.blob(f"product_images/{product_id}.jpg")
        blob.upload_from_string(image_data, content_type="image/jpeg")
