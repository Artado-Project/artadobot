from typing import List, Type
from zope.interface import implementer
from models.webSites import WebSites
from .StorageBase import StorageBase
from repositories.dbContext import DbContext



class WebSiteRespository(StorageBase):

    def __init__(self, context: DbContext):
        self.__context = context
