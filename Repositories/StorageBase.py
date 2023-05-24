from abc import ABC
from sqlalchemy.orm import sessionmaker,DeclarativeBase as Base
from . import DbContext
from Core import Repositories
from typing import List, Type, TypeVar

T = TypeVar('T', bound=Base)


class StorageBase(Repositories.IStorageBase[T], ABC):
    def __init__(self, context: DbContext):
        self.__context: DbContext = context

    def FindByCondition(self, expression: callable) -> Type[List[T]]:
        print("Find item by condition")
        return List[T]

    def CreateModel(self, model: Type[T]) -> Type[T]:
        self.__context.Create(model)
        return model

    def UpdateModel(self, model: Type[T]) -> Type[T]:

        return model

    def DeleteModel(self, id: int) -> None:
        print("Delete model")

    def FindAll(self, trackChanges: bool) -> Type[List[T]]:
        print("FindAll")
        return List[T]
