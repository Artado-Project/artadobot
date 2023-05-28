from typing import List
from core.repositories import IStorageBase
from repositories.dbContext import DbContext

class StorageBase(IStorageBase):
    def __init__(self, context: DbContext) -> None:
        self.__context = context
        super().__init__()
    def FindAll(self) -> List:
        return self.__context.GetAll()
    def FindById(self, id: int):
        return self.__context.GetById(id)
    def FindByCondition(self, expression) -> List:
        return self.__context.GetObjectsWithCondition(expression=expression)
    def Create(self, model):
        return self.__context.Create(model)
    def Update(self, model):
        return self.__context.Update(model)
    def Delete(self, id: int) -> None:
        self.__context.Delete(id)