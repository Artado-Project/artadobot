from core.service import IService
from helpers.LoggerHelper import LoggerHelper
from .robotsScannerService import RobotsReaderService
from helpers.pageHelper import PageHelper


class CrawlService(IService):

    def __init__(self, logger: LoggerHelper, robotsService: RobotsReaderService) -> None:
        super().__init__(logger)
        self.__base_url = None
        self.__robotsService = robotsService

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
            self.__CrawlPage(self.__base_url)
        except Exception as e:
            self._logger.Error(f"Message: {e}")
        pass

    def __CrawlPage(self, sub_url: str):
        # ilk önce bu site gezilebiliyor mu ? (robots.txt üzerinden bunu anla) gezilebiliyor ise page var mı yok mu
        # onu kontrol et. Yok ise yeni bir kayıt aç var ise var olan kayıt ile karşılaştırmasını yap. gezilebiliyor
        # ise __GetImages fonksiyonunu çalıştırıp bütün imageleri al ve duruma göre verileri işle __GetPageContents
        # fonksiyonunu çalıştır ve gerekli olan argümanları al ve veritabanına işle __GetLinksFonksiyonunu çalıştır.
        # Alınan veriler başka bir siteye yönlendirme yapıyorsa Veri tabanına bunları kaydet (pageLinks) pagelinks
        # alınan linkte eğer base'url'in bir yönlendirmesiyse yani aynı web sitesinin başka bir uzantısına gönderiyorsa
        # burada __CrawlPageFonksiyonunu tekrar çalıştır.
        # kendine bu işlemleri yapa yapa devam etsin.
        if self.__robotsService.CanFetchUrl("*", sub_url):
            self._logger.Info(f"Current Page => {sub_url}")
            # self.__GetImages(sub_url)
            # self.__GetPageContents(sub_url)
            links = PageHelper.GetLinkInsidePage(sub_url)
            for link in links:
                condition_str = PageHelper.ConfigureUrl(self.__base_url, link['href'])
                if condition_str is "":
                    print("Different web site")
                else:
                    print(condition_str)
                    if condition_str != self.__base_url + '/' and condition_str != sub_url:
                        self.__CrawlPage(condition_str)
                #if condition_str is "":
                #    self._logger.Info("Different web site")
                #else:
                #    if sub_url != self.__base_url + '/' and condition_str != sub_url:
                #        self.__CrawlPage(condition_str)
        else:
            self._logger.Warning(f"Crawler has not permission to crawl site url => {sub_url}")
        pass

    def __GetImages(self, sub_url):
        self._logger.Info("Getting Images")
        images = PageHelper.GetImageLinksPage(sub_url)
        print(images)
        pass

    def __GetPageContents(self, sub_url):
        self._logger.Info("Getting contents")
        contents = PageHelper.GetContentType(sub_url)
        print(contents)
        pass
