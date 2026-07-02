from typing import Generic
from typing import TypeVar

from app.repositories.base_repository import BaseRepository

ModelType = TypeVar("ModelType")


class BaseService(Generic[ModelType]):
    """
    Base service providing reusable CRUD operations.
    """

    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_by_id(self, obj_id: int):
        return self.repository.get_by_id(obj_id)

    def get_all(self):
        return self.repository.get_all()

    def create(self, obj):
        return self.repository.create(obj)

    def update(self):
        return self.repository.update()

    def delete(self, obj):
        return self.repository.delete(obj)