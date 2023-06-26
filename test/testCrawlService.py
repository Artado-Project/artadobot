from dotenv import load_dotenv

from helpers.LoggerHelper import LoggerHelper
from helpers.envConfigurator import EnvConfigurator
from models.crawlLog import CrawlLog
from models.crawlRules import CrawlRules
from models.pageContents import PageContents
from models.pageImages import PageImages
from models.pageLinks import PageLinks
from models.pages import Pages
from models.webSites import WebSites
from repositories.crawlLogRepository import CrawlLogRepository
from repositories.crawlRulesRepository import CrawlRulesRepository
from repositories.dbContext import DbContext
from repositories.pageContentsRepository import PageContentRepository
from repositories.pageImageRespository import PageImageRepository
from repositories.pageLinkRepository import PageLinkRepository
from repositories.pageRepository import PageRepository
from repositories.webSiteRepository import WebSiteRepository
from services.crawlService import CrawlService
from services.repositoryManager import RepositoryManager
from services.robotsScannerService import RobotsReaderService
from urllib.robotparser import RobotFileParser


def run_test():
    logger = LoggerHelper()
    load_dotenv()
    env_configurator = EnvConfigurator()
    db_link = env_configurator.MigrateConfiguration("MYSQL_DB")
    repo_manager = RepositoryManager(
        logger=logger,
        webSiteRepo=WebSiteRepository(
            DbContext(db_url=db_link, model_class=WebSites)),
        pageRepo=PageRepository(DbContext(db_url=db_link, model_class=Pages)),
        pageLinkRepo=PageLinkRepository(
            DbContext(db_url=db_link, model_class=PageLinks)),
        crawlRulesRepo=CrawlRulesRepository(
            DbContext(db_url=db_link, model_class=CrawlRules)),
        crawlLogRepo=CrawlLogRepository(
            DbContext(db_url=db_link, model_class=CrawlLog)),
        pageImageRepo=PageImageRepository(
            DbContext(db_url=db_link, model_class=PageImages)),
        pageContentsRepo=PageContentRepository(
            DbContext(db_url=db_link, model_class=PageContents))
    )

    service = CrawlService(
        logger=logger,
        robotsService=RobotsReaderService(logger=logger, robotsHelper=RobotFileParser())
    )
    service.ExecuteCrawl("https://tr.wikipedia.org")
    dict_value = service.GetResult()
