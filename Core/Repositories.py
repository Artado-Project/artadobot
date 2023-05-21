from typing import List, Type, Generic, TypeVar
from zope.interface import interface

from Core.Model import Model

T = TypeVar('T', bound=Model)


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
