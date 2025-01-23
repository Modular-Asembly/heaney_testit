from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.services.user.register_user import register_user

router = APIRouter()

class UserRegistrationRequest(BaseModel):
    email: EmailStr
    password: str

class UserRegistrationResponse(BaseModel):
    status: str
    message: str

@router.post("/register", response_model=UserRegistrationResponse)
def user_registration_endpoint(user_data: UserRegistrationRequest) -> UserRegistrationResponse:
    """
    Endpoint to register a new user.

    - **user_data**: UserRegistrationRequest object containing email and password.

    Returns a UserRegistrationResponse object with the status and message.
    """
    try:
        register_user(user_data.dict())
        return UserRegistrationResponse(status="success", message="User registered successfully.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
