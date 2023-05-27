from abc import ABC, abstractmethod
from typing import List, Type
from .model import Model

class IStorageBase(ABC):
    
    @abstractmethod
    def FindAll(self) -> List[Model]:
        pass
    
    @abstractmethod
    def FindById(self, id: int) -> Model:
        pass
    @abstractmethod
    def FindByCondition(self, expression) -> List[Model]:
        pass
    @abstractmethod
    def Create(self, model: Model) -> Model:
        pass
    @abstractmethod
    def Update(self, model: Model) -> Model:
        pass
    @abstractmethod
    def Delete(self, id: int) -> None:
        pass