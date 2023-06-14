from core.service import IService
from helpers.LoggerHelper import LoggerHelper
from .robotsScannerService import RobotsReaderService
from helpers.pageHelper import PageHelper


class CrawlService(IService):

    def __init__(self, logger: LoggerHelper, robotsService: RobotsReaderService) -> None:
        super().__init__(logger)
        self.__base_url = None
        self.__robotsService = robotsService
        self.__crawledPages = []
        self.__subUrls = []
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
            self.__Crawl(self.__subUrls[0])
        except Exception as e:
            self._logger.Error(f"Message: {e}")
        pass

    def __Crawl(self, sub_url: str):
        if not self.__crawledPages.__contains__(sub_url):
            self.__CrawlCurrentPage(sub_url)
            self.__crawledPages.append(sub_url)
            self.__counter += 1
            if self.__CheckCanContinueToCrawl(self.__counter, self.__subUrls):
                self.__Crawl(self.__subUrls[self.__counter])
            else:
                self._logger.Warning("CRAWL COMPLETED")

    def __CheckCanContinueToCrawl(self, counter: int, array: list) -> bool:
        return self.__counter < len(array)

    def __CrawlCurrentPage(self, sub_url):
        if self.__robotsService.CanFetchUrl("*", sub_url):
            # self.__GetImages(sub_url)
            # self.__GetPageContents(sub_url)
            self._logger.Info(f"Current Page {sub_url}")
            links = PageHelper.GetLinkInsidePage(sub_url)
            for link in links:
                if link.get('href') is not None:
                    configured_url = PageHelper.ConfigureUrl(self.__base_url, link.get('href'))
                    if configured_url is "":
                        pass
                    else:
                        if not self.__subUrls.__contains__(configured_url):
                            # self._logger.Info(f"Sub url {configured_url}")
                            self.__subUrls.append(configured_url)
        else:
            self._logger.Warning(f"Crawler has not permission to crawl site url => {sub_url}")

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
