from typing import List
from models.webSites import WebSites
from .StorageBase import StorageBase
from repositories.dbContext import DbContext



class WebSiteRespository(StorageBase):

    def __init__(self, context: DbContext):
        super().__init__(context)

    def GetAllWebSite(self) -> List:
        return self.FindAll()
    
    def GetWebsiteById(self, id: int):
        return self.FindById(id)
    
    def GetWebsiteByCondition(self, expression) -> List:
        return self.FindByCondition(expression)
    
    def CreateWebSite(self, website: WebSites):
        return self.Create(website)
    
    def UpdateWebSite(self, website: WebSites):
        return self.Update(website)
    
    def DeleteWebSite(self, id: int):
        self.Delete(id)