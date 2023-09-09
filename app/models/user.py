"""Declare models and relationships."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from app.database import engine

Base = declarative_base()

"""User Model"""
class User(Base):
    __tablename__ ='user'

    id = Column(Integer, primary_key=True)
    phone_number = Column(Integer)
    facebook_account = Column(String(50))
    google_account = Column(String(50))
    username = Column(String(50), nullable=False)
    dot = Column(String)
    gender = Column(String(50))
    singles_skill = Column(Integer)
    doubles_skill = Column(Integer)
    club = Column(String(100))

    def __repr__(self):
        return f'<User ID={self.id}, username={self.username}>'


Base.metadata.create_all(engine)