from abc import ABC
from sqlalchemy.orm import DeclarativeBase as Base
from . import DbContext
from Core import Repositories
from typing import List, Type, TypeVar

T = TypeVar('T', bound=Base)


class StorageBase(Repositories.IStorageBase[T], ABC):
    def __init__(self, context: DbContext.DbContext[T]):
        self.__context: DbContext.DbContext[T] = context

    def FindByCondition(self, expression: callable) -> List:
        return self.__context.GetObjectsWithCondition(expression)

    def CreateModel(self, model: Type[T]) -> Type[T]:
        self.__context.Create(model)
        return model

    def UpdateModel(self, model: Type[T]) -> Type[T]:
        self.__context.Update(model)
        return model

    def DeleteModel(self, id: int) -> None:
        self.__context.Delete(id)

    def FindAll(self, trackChanges: bool) -> List:
        return self.__context.GetAll()
