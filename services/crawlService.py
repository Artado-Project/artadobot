from core.service import IService
from helpers.LoggerHelper import LoggerHelper
from helpers.requestHelper import RequestHelper
from .robotsScannerService import RobotsReaderService
from helpers.pageHelper import PageHelper


class CrawlService(IService):

    def __init__(self, logger: LoggerHelper,
                 robotsService: RobotsReaderService) -> None:
        super().__init__(logger)
        self.__counter = 0
        self.__subUrls = []  # sub domain urls
        self.__differentPageUrls = []  # links
        self.__crawledPages = []
        self.__base_url = None
        self.__images = {}
        self.__pageContents = {}
        self.__robotsService = robotsService
        self.SetToDefault()

    def __CheckCanContinueToCrawl(self, counter: int, array: list) -> bool:
        return counter < len(array)

    def SetToDefault(self):
        self.__crawledPages.clear()
        self.__differentPageUrls.clear()
        self.__base_url = ""
        self.__subUrls.clear()
        self.__counter = 0

    def ExecuteCrawl(self, site: str):
        try:
            self.__base_url = site
            self.__robotsService.ScanRobotsFile(site)
            self._logger.Info("Crawler initializing process")
            self.__subUrls.append(self.__base_url + '/')
            while True:
                if self.__CheckCanContinueToCrawl(self.__counter, self.__subUrls):
                    self.__Crawl(self.__subUrls[self.__counter])
                    self.__counter += 1
                else:
                    self._logger.Warning("CRAWL COMPLETED")
                    print(self.__images)
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
            response = RequestHelper.GetResponseContent(sub_url, self._logger)
            if response is not None:
                self.__GetImages(response, sub_url)
                self.__GetPageContents(response, sub_url)
                self._logger.Info(f"Current Page {sub_url}")
                links = PageHelper.GetLinkInsidePage(response)
                for link in links:
                    self.__HandleLinks(link)
        else:
            self._logger.Warning(f"Crawler has not permission to crawl this url => {sub_url}")

    def __GetImages(self, response, sub_url: str):
        self._logger.Info(f"Getting Images from {sub_url}")
        images = PageHelper.GetImageLinksPage(response)
        self.__images[sub_url] = []
        for image in images:
            obj = {}
            if image.get('alt') is not None:
                obj['alt'] = image.get('alt')
            if image.get('src') is not None:
                obj['src'] = image.get('src')
            self.__images[sub_url].append(obj)

    def __GetPageContents(self, response, sub_url):
        self._logger.Info(f"Getting contents from {sub_url}")
        contents = PageHelper.FindPageContents(response)
        self.__pageContents[sub_url] = contents

    def __HandleLinks(self, link):
        href_link: str = link.get('href')
        if href_link is not None:
            configured_url = PageHelper.ConfigureUrl(self.__base_url, href_link)
            if configured_url == "":
                if href_link not in self.__differentPageUrls and not href_link.startswith("#"):
                    self.__differentPageUrls.append(href_link)
            else:
                if configured_url not in self.__subUrls:
                    self.__subUrls.append(configured_url)

    def GetLinks(self):
        return self.__differentPageUrls

    def GetPages(self):
        return self.__crawledPages

    def GetImages(self):
        return self.__images

    def GetContents(self):
        return self.__pageContents
