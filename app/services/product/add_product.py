import os
from typing import Dict
from sqlalchemy.orm import Session
from google.cloud import storage
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.modassembly.storage.get_gcs_bucket import get_gcp_bucket
from app.models.Product import Product


def add_product(product_data: Dict[str, str], image_path: str) -> None:
    # Store product data in CloudSQL
    with next(get_sql_session()) as session:  # type: Session
        new_product = Product(
            name=product_data["name"],
            description=product_data["description"],
            price=float(product_data["price"]),
            stock=int(product_data["stock"])
        )
        session.add(new_product)
        session.commit()

    # Upload image to CloudStorage
    bucket = get_gcp_bucket()
    blob = bucket.blob(f"product_images/{new_product.product_id.__str__()}.jpg")
    blob.upload_from_filename(image_path)
