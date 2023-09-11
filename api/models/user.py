"""Declare models and relationships."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from ..database import engine

Base = declarative_base()

"""User Model"""
class User(Base):
    __tablename__ ='user'

    id = Column(Integer, primary_key=True)
    phone_number = Column(Integer)
    username = Column(String(50), nullable=False)
    dot = Column(String)
    gender = Column(String(50))

    def __repr__(self):
        return f'<User ID={self.id}, username={self.username}>'


Base.metadata.create_all(engine)