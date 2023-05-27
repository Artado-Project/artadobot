from core.repositories import IStorageBase
from repositories.dbContext import DbContext

class StorageBase(IStorageBase):
    def __init__(self, context: DbContext) -> None:
        self.__context = context
        super().__init__()
    def FindAll(self):
        pass
    def FindById(self, id: int):
        pass
    def FindByCondition(self, expression):
        pass
    def Create(self, model):
        pass
    def Update(self, model):
        pass
    def Delete(self, id: int) -> None:
        pass