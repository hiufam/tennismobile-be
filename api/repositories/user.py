from ..database import session
from ..models.user import User


class UserRepository:
    def add_user(id, args) -> User:
        user = User(
            id= id,
            phone_number=args['phone_number'],
            username=args['username'],
            dot=args['dot'],
            gender=args['gender'],
        )

        session.add(user)
        session.commit()
        return user