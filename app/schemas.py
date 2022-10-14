from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint


class PostBase(BaseModel):
  title: str
  content: str
  published: bool = True
  # rating: Optional[int] = None

class PostMake(PostBase):
    pass

class UserOut(BaseModel):
  id: int
  email: EmailStr
  made_at: datetime

  class Config:
    orm_mode = True
    
# response
class Post(PostBase):
  id: int
  made_at: datetime
  owner_id: int
  owner: UserOut

  class Config:
    orm_mode = True


class PostOut(BaseModel):
  Post: Post
  votes: int

  class Config:
    orm_mode = True



class UserMake(BaseModel):
  email: EmailStr
  password: str




class UserLogin(BaseModel):
  email: EmailStr
  password: str


class Token(BaseModel):
  access_token: str
  token_type: str


class TokenData(BaseModel):
  id: Optional[str] = None



class Vote(BaseModel):
  post_id: int
  dir: conint(le=1)


class TokenData(BaseModel):
  id: Optional[str] = None




