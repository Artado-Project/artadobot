from core.service import IService
from helpers.LoggerHelper import LoggerHelper
from helpers.requestHelper import RequestHelper
from .robotsScannerService import RobotsReaderService
from helpers.pageHelper import PageHelper


class CrawlService(IService):

    def __init__(self, logger: LoggerHelper, robotsService: RobotsReaderService) -> None:
        super().__init__(logger)
        self.__counter = 0
        self.__subUrls = []
        self.__differentPageUrls = []
        self.__crawledPages = []
        self.__base_url = None
        self.__robotsService = robotsService
        self.SetToDefault()

    def __CheckCanContinueToCrawl(self, counter: int, array: list) -> bool:
        return self.__counter < len(array)

    def SetToDefault(self):
        self.__crawledPages.clear()
        self.__subUrls.clear()
        self.__counter = 0

    def ExecuteCrawl(self, site: str):
        # site aldın
        # robots.txt dosyasını okudun
        # website verilerini kaydet // varsa tekrar kontrol edip update et
        # sonra __CrawlPage fonksiyonunu çalıştır
        # burada bütün işlemler tamamlandıktan sonra
        # pageRank servisi ile bir page rank oluşturulmalı
        # ve bu siteye bu pagerank Skoru dahil edilmeli.
        try:
            self.__base_url = site
            self.__robotsService.ScanRobotsFile(site)
            self._logger.Info("Crawler initializing proccess")
            self.__subUrls.append(self.__base_url + '/')
            while True:
                if self.__CheckCanContinueToCrawl(self.__counter, self.__subUrls):
                    self.__Crawl(self.__subUrls[self.__counter])
                    self.__counter += 1
                else:
                    self._logger.Warning("CRAWL COMPLETED")
                    self.SetToDefault()
                    break
        except Exception as e:
            self._logger.Error(f"Message: {e}")
        pass

    def __Crawl(self, sub_url: str):
        if sub_url not in self.__crawledPages:
            self.__CrawlCurrentPage(sub_url)
            self.__crawledPages.append(sub_url)

    def __CrawlCurrentPage(self, sub_url):
        if self.__robotsService.CanFetchUrl("*", sub_url):
            # self.__GetImages(sub_url)
            # self.__GetPageContents(sub_url)
            self._logger.Info(f"Current Page {sub_url}")
            response = RequestHelper.GetResponseContent(sub_url)
            links = PageHelper.GetLinkInsidePage(response, self._logger)
            for link in links:
                self.__LinkHandler(link)

        else:
            self._logger.Warning(f"Crawler has not permission to crawl this url => {sub_url}")

    def __GetImages(self, sub_url):
        self._logger.Info(f"Getting Images from {sub_url}")
        images = PageHelper.GetImageLinksPage(sub_url)
        print(images)
        pass

    def __GetPageContents(self, sub_url):
        self._logger.Info(f"Getting contents from {sub_url}")
        contents = PageHelper.GetContentType(sub_url)
        print(contents)
        pass

    def __LinkHandler(self, link):
        href_link: str = link.get('href')
        if href_link is not None:
            configured_url = PageHelper.ConfigureUrl(self.__base_url, href_link)
            if configured_url == "":
                if href_link not in self.__differentPageUrls and not href_link.startswith("#"):
                    self.__differentPageUrls.append(href_link)
                    self._logger.Warning(f"Different WebSite = {href_link}")
            else:
                if configured_url not in self.__subUrls:
                    self._logger.Info(f"Sub url {configured_url}")
                    self.__subUrls.append(configured_url)
