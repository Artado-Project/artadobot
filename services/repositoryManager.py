from core.service import IService
from helpers.LoggerHelper import LoggerHelper
from repositories.crawlLogRepository import CrawlLogRepository
from repositories.crawlRulesRepository import CrawlRulesRepository
from repositories.pageContentsRepository import PageContentRepository
from repositories.pageImageRespository import PageImageRepository
from repositories.pageLinkRepository import PageLinkRepository
from repositories.pageRepository import PageRepository
from repositories.webSiteRepository import WebSiteRepository


class RepositoryManager(IService):
    def __init__(self,
                 logger: LoggerHelper,
                 crawlLogRepo: CrawlLogRepository,
                 crawlRulesRepo: CrawlRulesRepository,
                 pageContentsRepo: PageContentRepository,
                 pageImageRepo: PageImageRepository,
                 pageLinkRepo: PageLinkRepository,
                 pageRepo: PageRepository,
                 webSiteRepo: WebSiteRepository) -> None:
        self.CrawlLogRepo = crawlLogRepo
        self.CrawlRulesRepo = crawlRulesRepo
        self.PageContentRepo = pageContentsRepo
        self.PageImageRepo = pageImageRepo
        self.PageLinkRepo = pageLinkRepo
        self.PageRepo = pageRepo
        self.WebSiteRepo = webSiteRepo
        super().__init__(logger)
