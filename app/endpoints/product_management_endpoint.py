from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from typing import Optional
from app.services.product.add_product import add_product
from app.services.product.update_product import update_product
from app.services.product.delete_product import delete_product
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

class ResponseModel(BaseModel):
    status: str
    message: str

@router.post("/product", response_model=ResponseModel)
async def create_product(product: ProductCreate, image: UploadFile = File(...)) -> ResponseModel:
    try:
        image_data = await image.read()
        add_product(product.dict(), image_data)
        return ResponseModel(status="success", message="Product added successfully.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/product/{product_id}", response_model=ResponseModel)
async def update_product_endpoint(product_id: int, product: ProductUpdate, image: Optional[UploadFile] = None) -> ResponseModel:
    try:
        image_data = await image.read() if image else None
        with next(get_sql_session()) as db:
            update_product(db, product_id, **product.dict(), image_data=image_data)
        return ResponseModel(status="success", message="Product updated successfully.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/product/{product_id}", response_model=ResponseModel)
async def delete_product_endpoint(product_id: int) -> ResponseModel:
    try:
        delete_product(product_id)
        return ResponseModel(status="success", message="Product deleted successfully.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
