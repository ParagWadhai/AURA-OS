from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """
    Common user fields.
    """

    full_name: str = Field(
        ...,
        min_length=2,
        max_length=255,
        description="Full name of the user",
    )

    email: EmailStr


class UserCreate(UserBase):
    """
    Schema used during user registration.
    """

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="User password",
    )


class UserUpdate(BaseModel):
    """
    Schema for updating user details.
    """

    full_name: str | None = Field(default=None, min_length=2, max_length=255)
    email: EmailStr | None = None


class UserResponse(UserBase):
    """
    Response returned by the API.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    is_active: bool
    created_at: datetime