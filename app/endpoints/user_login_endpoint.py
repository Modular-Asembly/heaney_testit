from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.user.login_user import login_user

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    token: Optional[str] = None
    status: str
    message: str

@router.post("/login", response_model=LoginResponse)
def user_login_endpoint(login_request: LoginRequest) -> LoginResponse:
    """
    Endpoint for user login.

    - **email**: User's email address.
    - **password**: User's password.

    Returns a LoginResponse object with the authentication token if successful.
    """
    token = login_user(login_request.email, login_request.password)
    if token:
        return LoginResponse(token=token, status="success", message="Login successful.")
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")
