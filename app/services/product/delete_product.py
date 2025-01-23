from sqlalchemy.orm import Session
from google.cloud import storage
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.modassembly.storage.get_gcs_bucket import get_gcp_bucket
from app.models.Product import Product


def delete_product(product_id: int) -> None:
    # Delete product data from CloudSQL
    with next(get_sql_session()) as session:  # type: Session
        product: Product = session.query(Product).filter(Product.product_id == product_id).first()
        if product:
            session.delete(product)
            session.commit()

    # Delete product image from CloudStorage
    bucket = get_gcp_bucket()
    blob = bucket.blob(f"products/{product_id}")
    if blob.exists():
        blob.delete()
