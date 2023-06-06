from typing import List
from models.crawlLog import CrawlLog
from repositories.dbContext import DbContext
from .dbContext import DbContext
from .StorageBase import StorageBase


class CrawlLogRepository(StorageBase):
    def __init__(self, context: DbContext) -> None:
        super().__init__(context)

    def GetAllLogs(self) -> List:
        return self.FindAll()

    def GetLogById(self, id: int):
        return self.FindById(id)

    def GetLogsByCondition(self, expression) -> List:
        return self.FindByCondition(expression)

    def CreateLog(self, log: CrawlLog):
        return self.Create(log)

    def UpdateLog(self, log: CrawlLog):
        return self.Update(log)

    def DeleteLog(self, id: int):
        self.Delete(id)
