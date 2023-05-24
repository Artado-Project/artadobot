from typing import List, Type, Generic, TypeVar
from sqlalchemy.orm import DeclarativeBase as Base
from abc import ABC, abstractmethod

T = TypeVar('T', bound=Base)


class IStorageBase(Generic[T], ABC):
    @abstractmethod
    def FindAll(self, trackChanges: bool) -> List:
        pass

    @abstractmethod
    def FindById(self, id: int) -> Type[T]:
        pass

    @abstractmethod
    def FindByCondition(self, expression: callable) -> List:
        pass

    @abstractmethod
    def CreateModel(self, model: Type[T]) -> Type[T]:
        pass

    @abstractmethod
    def UpdateModel(self, model: Type[T]) -> Type[T]:
        pass

    @abstractmethod
    def DeleteModel(self, id: int) -> None:
        pass
