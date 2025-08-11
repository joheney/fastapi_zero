from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: str
    id: int


class UserDb(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
