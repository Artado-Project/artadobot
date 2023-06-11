from core.service import IService
from helpers.LoggerHelper import LoggerHelper
from .robotsScannerService import RobotsReaderService
import requests
from bs4 import BeautifulSoup


class CrawlService(IService):

    def __init__(self, logger: LoggerHelper, robotsService: RobotsReaderService) -> None:
        super().__init__(logger)
        self.__robotsService = robotsService

    def ExecuteCrawl(self, site: str):
        # sitenin robots.txt dosyasını okuduktan sonra. index.html'deki bütün urlleri çekip
        # bu urller üzerinden gezmeye başlamalı.
        # her defasında robots servisi üzerinden o url'i gezip gezmeyeceğini belirlemeli
        # gezebiliyorsa gezip istenilen veriler çekmesi gerekiyor.
        # gezemiyorsa ona göre işlem yaptırıp bu şekilde veri tabanına uygun düzende kayıt etmelidir.
        self.__robotsService.ScanRobotsFile(site)
        if self.__robotsService.CanFetchUrl("*", "/login/"):
            self._logger.Info(f"Crawling {site}/login/ url")
            response = requests.get(site + "/login")

        else:
            self._logger.Error(f"Can't crawl {site}/login")

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
