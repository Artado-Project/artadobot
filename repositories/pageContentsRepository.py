from repositories.dbContext import DbContext
from .dbContext import DbContext
from .StorageBase import StorageBase
from typing import List
from models.pageContents import PageContents


class PageContentRepository(StorageBase):
    def __init__(self, context: DbContext) -> None:
        super().__init__(context)

    def GetAllContents(self) -> List:
        return self.FindAll()

    def GetContentById(self, id: int):
        return self.FindById(id)

    def GetContentByCondition(self, expression) -> List:
        return self.FindByCondition(expression)

    def CreateContent(self, content: PageContents):
        return self.Create(content)

    def UpdateContent(self, content: PageContents):
        return self.Update(content)

    def DeleteContent(self, id: int):
        self.Delete(id)
