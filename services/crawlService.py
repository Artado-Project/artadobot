from core.service import IService
from helpers.LoggerHelper import LoggerHelper


class CrawlService(IService):

    def __init__(self, logger: LoggerHelper) -> None:
        super().__init__(logger)

    def ExecuteCrawl(self):
        pass

    def __CrawlSite(self, main_url):
        pass

    def __GetLinks(self, sub_url):
        pass

    def __GetImages(self, sub_url):
        pass

    def __GetKeywords(self, sub_url):
        pass

    def __GetFavIcon(self, sub_url):
        pass
