from pydantic import BaseModel, ConfigDict, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RegisterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    email: EmailStr
    access_token: str
    refresh_token: str