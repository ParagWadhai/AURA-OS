from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Any

from jose import JWTError
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

# JWT Configuration
SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES = (
    settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
)

REFRESH_TOKEN_EXPIRE_DAYS = (
    settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS
)


def hash_password(password: str) -> str:
    """
    Hash a plain-text password.
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verify a password.
    """
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(
    data: dict[str, Any],
) -> str:
    """
    Generate JWT access token.
    """
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire,
        }
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def create_refresh_token(
    data: dict[str, Any],
) -> str:
    """
    Generate refresh token.
    """
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        days=REFRESH_TOKEN_EXPIRE_DAYS
    )

    to_encode.update(
        {
            "exp": expire,
        }
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_token(
    token: str,
) -> dict:
    """
    Decode JWT token.
    """
    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

    except JWTError:
        return {}
    
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/token"
)