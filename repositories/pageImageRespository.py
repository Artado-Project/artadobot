from typing import List
from models.pageImages import PageImages
from .dbContext import DbContext
from .StorageBase import StorageBase

class PageImageRepository(StorageBase):
    
    def __init__(self, context: DbContext) -> None:
        super().__init__(context)
        
    def GetAllImages(self) -> List:
        return self.FindAll()
    
    def GetImageById(self, id: int):
        return self.FindById(id)
    
    def GetImageByCondition(self, expression) -> List:
        return self.FindByCondition(expression)
    
    def CreateImage(self, image: PageImages):
        return self.Create(image)
    
    def UpdateImage(self, image: PageImages):
        return self.Update(image)
    
    def DeleteImage(self, id: int):
        self.Delete(id)