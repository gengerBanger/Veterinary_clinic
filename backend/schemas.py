from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.data_base import Base

class Registration(Base):
    __tablename__ = "registration"
    __table_args__ = {'schema': 'vc'}

    post_id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey("vc.dogs.dog_id"))
    created_at = Column(TIMESTAMP)
    dog = relationship("Dogs")

class Dogs(Base):
    __tablename__ = "dogs"
    __table_args__ = {'schema': 'vc'}

    dog_id = Column(Integer, primary_key=True)
    name_ = Column(String)
    kind_ = Column(String)




