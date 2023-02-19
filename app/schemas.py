from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class UserSchema(BaseModel):
    id: Optional[int] = None
    fullname: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        orm_mode = True

class ProfileSchema(BaseModel):
    id: Optional[int] = None
    profile_picture: Optional[str] = None

    class Config:
        orm_mode = True

class RequestProfile(BaseModel):
    parameter: ProfileSchema = Field(...)

class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code:str
    status:str
    message:str
    result:Optional[T]


