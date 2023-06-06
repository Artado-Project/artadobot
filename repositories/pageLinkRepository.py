from typing import List
from models.pageLinks import PageLinks
from repositories.dbContext import DbContext
from .dbContext import DbContext
from .StorageBase import StorageBase


class PageLinkRepository(StorageBase):
    def __init__(self, context: DbContext) -> None:
        super().__init__(context)

    def GetAllLinks(self) -> List:
        return self.FindAll()

    def GetLinkById(self, id: int):
        return self.FindById(id)

    def GetLinkByCondition(self, expression) -> List:
        return self.FindByCondition(expression)

    def CreateLink(self, link: PageLinks):
        return self.Create(link)

    def UpdateLink(self, link: PageLinks):
        return self.Update(link)

    def DeleteLink(self, id: int):
        self.Delete(id)
