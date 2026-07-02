from typing import Generic
from typing import Optional
from typing import Type
from typing import TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Generic repository implementing common CRUD operations.
    """

    def __init__(
        self,
        model: Type[ModelType],
        db: Session,
    ):
        self.model = model
        self.db = db

    def get_by_id(
        self,
        obj_id: int,
    ) -> Optional[ModelType]:
        return (
            self.db.query(self.model)
            .filter(self.model.id == obj_id)
            .first()
        )

    def get_all(self):
        return self.db.query(self.model).all()

    def create(self, obj: ModelType):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj: ModelType):
        self.db.delete(obj)
        self.db.commit()

    def update(self):
        self.db.commit()