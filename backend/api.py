from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from backend.data_base import SessionLocal
from backend.models import GetDog, PostDog, GetRegistration
from backend.schemas import Registration, Dogs

app = FastAPI(title="Veterinary clinic")

def get_session():
    with SessionLocal() as session:
        return session

@app.get('/')
def get_start():
    return "Hi, this is a veterinary clinic"

@app.get('/dogs', response_model=List[GetDog])
def get_all_dogs(limit: int = 5, db: Session = Depends(get_session)):
    return db.query(Dogs).limit(limit).all()

@app.post('/dog', response_model=PostDog)
def create_new_dog(new_dog: PostDog, db: Session = Depends(get_session)):
    dog = Dogs(name_=new_dog.name_, kind_=new_dog.kind_.value)
    db.add(dog)
    db.commit()
    return new_dog

@app.get('/dog/{dog_id}')
def get_dog_by_id(dog_id: int, db: Session = Depends(get_session)):
    return db.query(Dogs).filter_by(dog_id=dog_id).all()


