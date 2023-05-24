from typing import List, Type, Generic, TypeVar
from sqlalchemy.orm import DeclarativeBase as Base
from zope.interface import interface


T = TypeVar('T', bound=Base)


class IStorageBase(Generic[T], interface):
    def FindAll(self, trackChanges: bool) -> Type[List[T]]:
        pass

    def FindById(self, id: int) -> Type[T]:
        pass

    def FindByCondition(self, expression: callable) -> Type[List[T]]:
        pass

    def CreateModel(self, model: Type[T]) -> Type[T]:
        pass

    def UpdateModel(self, model: Type[T]) -> Type[T]:
        pass

    def DeleteModel(self, id: int) -> None:
        pass
