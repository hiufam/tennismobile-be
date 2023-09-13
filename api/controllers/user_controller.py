from ..database import session
from ..models.user import User

def create_user(user : User) -> User:

    session.add(user)
    session.commit()
    return user
