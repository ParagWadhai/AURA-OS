from app.repositories.user_repository import UserRepository


class UserService:
    """
    User business logic.
    """

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)

    def get_user_by_email(self, email: str):
        return self.repository.get_by_email(email)

    def get_all_users(self):
        return self.repository.get_all()

    def create_user(self, user):
        return self.repository.create(user)