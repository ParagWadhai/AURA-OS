from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.auth import LoginRequest
from app.schemas.auth import RegisterResponse
from app.schemas.auth import Token
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService
from app.api.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    auth_service = AuthService(db)

    try:
        created_user, token = auth_service.register(user)

        return RegisterResponse(
            id=created_user.id,
            full_name=created_user.full_name,
            email=created_user.email,
            access_token=token.access_token,
            refresh_token=token.refresh_token,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.post(
    "/login",
    response_model=Token,
)

def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    auth_service = AuthService(db)

    try:
        return auth_service.login(
            request.email,
            request.password,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        )
    
@router.post(
    "/token",
    response_model=Token,
)
def login_for_swagger(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    auth_service = AuthService(db)

    try:
        return auth_service.login(
            form_data.username,   # username contains the email
            form_data.password,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        )
    
@router.get(
    "/me",
    response_model=UserResponse,
)
def me(
    current_user: User = Depends(get_current_user),
):
    return current_user