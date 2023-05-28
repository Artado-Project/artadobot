from .crawlLogRepository import CrawlLogRepository
from .crawlRulesRepository import CrawRulesRepository
from .pageContentsRepository import PageContentRepository
from .pageImageRespository import PageImageRepository
from .pageLinkRepository import PageLinkRepository
from .pageRepository import PageRepository
from .webSiteRepository import WebSiteRespository


class RepositoryManager:
    
    def __init__(self, 
                 crawLogRepo:CrawlLogRepository,
                 crawlRuleRepo: CrawRulesRepository,
                 pageContentRepo: PageContentRepository,
                 pageImageRepo: PageImageRepository,
                 pageLinkRepo: PageLinkRepository,
                 pageRepo: PageRepository,
                 webSiteRepo: WebSiteRespository) -> None:
        self.crawlLogRepo = crawLogRepo
        self.crawlRulesRepo = crawlRuleRepo
        self.pageContentRepo = pageContentRepo
        self.pageImageRepo = pageImageRepo
        self.pageLinkRepo = pageLinkRepo
        self.pageRepo = pageRepo
        self.websiteRepo = webSiteRepo
        
    
        