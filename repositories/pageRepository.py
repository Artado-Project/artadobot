from typing import List
from models.pages import Pages
from .StorageBase import StorageBase
from .dbContext import DbContext

class PageRepository(StorageBase):
    
    def __init__(self, context: DbContext) -> None:
        super().__init__(context)
        
    def GetAllPages(self) -> List:
        return self.FindAll()
    
    def GetPageById(self, id: int):
        return self.FindById(id)
    
    def GetPageByCondition(self, expression) -> List:
        return self.FindByCondition(expression)
    
    def CreatePage(self, page: Pages):
        return self.Create(page)
    
    def UpdatePage(self, page: Pages):
        return self.Update(page)
    
    def DeletePage(self, id: int):
        self.Delete(id)
    