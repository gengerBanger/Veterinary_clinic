from enum import Enum
from pydantic import BaseModel, Field
import datetime

class GetRegistration(BaseModel):
    post_id: int
    dog_id: int
    created_at: datetime.datetime

class DogType(Enum):
    terrier = 'terrier'
    bulldog = 'bulldog'
    dalmatian = 'dalmatian'

class GetDog(BaseModel):
    dog_id: int
    name_: str = Field(max_length=10)
    kind_: DogType

class PostDog(BaseModel):
    name_: str = Field(max_length=10)
    kind_: DogType

