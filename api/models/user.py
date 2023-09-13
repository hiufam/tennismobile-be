"""Declare models and relationships."""
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

from ..database import engine

Base = declarative_base()

"""User Model"""
class User(Base):
    __tablename__ ='users'

    id = Column(Integer, primary_key=True)
    phone_number = Column(Integer, nullable=False)
    facebook_account = Column(String(50), nullable=True)
    google_account = Column(String(50), nullable=True)
    full_name = Column(String(50), nullable=False)
    date_of_birth = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    singles_skill = Column(Integer, nullable=False, default=0)
    doubles_skill = Column(Integer, nullable=False, default=0)
    registration_otp = Column(Integer, nullable=True)
    registration_otp_expiration = Column(DateTime, nullable=True)
    avatar = Column(String, nullable=True)
    is_verify = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<User ID={self.id}, full_name={self.full_name}>'


Base.metadata.create_all(engine)