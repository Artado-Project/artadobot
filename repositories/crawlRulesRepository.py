from typing import List
from models.crawlRules import CrawlRules
from repositories.dbContext import DbContext
from .dbContext import DbContext
from .StorageBase import StorageBase

class CrawRulesRepository(StorageBase):
    def __init__(self, context: DbContext) -> None:
        super().__init__(context)
        
    def GetAllRules(self) -> List:
        return self.FindAll()
    
    def GetRuleById(self, id: int):
        return self.FindById(id)
    
    def GetRuleByCondition(self, expression) -> List:
        return self.FindByCondition(expression)
    
    def CreateRule(self, rule: CrawlRules):
        return self.Create(rule)
    
    def UpdateRule(self, rule: CrawlRules):
        return self.Update(rule)
    
    def DeleteRule(self, id: int):
        self.Delete(id)