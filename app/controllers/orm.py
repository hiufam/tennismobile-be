"""Create users with SQLAlchemy's ORM."""
from sqlalchemy.orm import Session
from app.models.user import User


""" Create instance of "User" model """
def create_user(session: Session, user: User) -> User:
    try:
        session.add(user)
        session.commit()
        
        print(f"Created new user: {user}")
        return user
    except Exception as e:
        print(f"Unexpected error when creating user: {e}")
