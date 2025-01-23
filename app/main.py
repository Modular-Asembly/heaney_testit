from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers

from app.models.Product import Product
from app.models.ShoppingCart import ShoppingCart
from app.models.User import User
from app.models.Order import Order
from app.endpoints.user_registration_endpoint import router
app.include_router(router)
from app.endpoints.user_login_endpoint import router
app.include_router(router)
from app.endpoints.product_management_endpoint import router
app.include_router(router)
from app.endpoints.shopping_cart_endpoint import router
app.include_router(router)
from app.endpoints.order_processing_endpoint import router
app.include_router(router)
from app.endpoints.order_email_endpoint import router
app.include_router(router)

# Database

from app.modassembly.database.sql.get_sql_session import Base, engine
Base.metadata.create_all(engine)
