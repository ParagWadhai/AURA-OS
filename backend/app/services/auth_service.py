from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import Token
from app.schemas.user import UserCreate


class AuthService:
    """
    Handles authentication business logic.
    """

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(
        self,
        user_data: UserCreate,
    ) -> tuple[User, Token]:

        existing_user = self.user_repository.get_by_email(
            user_data.email
        )

        if existing_user:
            raise ValueError(
                "Email already registered."
            )

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hash_password(
                user_data.password
            ),
        )

        user = self.user_repository.create(user)

        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
            }
        )

        refresh_token = create_refresh_token(
            {
                "sub": str(user.id),
            }
        )

        token = Token(
            access_token=access_token,
            refresh_token=refresh_token,
        )

        return user, token

    def login(
        self,
        email: str,
        password: str,
    ) -> Token:

        user = self.user_repository.get_by_email(
            email
        )

        if not user:
            raise ValueError(
                "Invalid credentials."
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid credentials."
            )

        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
            }
        )

        refresh_token = create_refresh_token(
            {
                "sub": str(user.id),
            }
        )

        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
        )