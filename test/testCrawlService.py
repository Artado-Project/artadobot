from helpers.LoggerHelper import LoggerHelper
from services.crawlService import CrawlService
from services.repositoryManager import RepositoryManager
from services.robotsScannerService import RobotsReaderService
from urllib.robotparser import RobotFileParser

from repositories.pageRepository import PageRepository, Pages
from repositories.pageContentsRepository import PageContentRepository, PageContents
from repositories.crawlLogRepository import CrawlLogRepository, CrawlLog
from repositories.crawlRulesRepository import CrawlRulesRepository, CrawlRules
from repositories.pageImageRespository import PageImageRepository, PageImages
from repositories.pageLinkRepository import PageLinkRepository, PageLinks
from repositories.webSiteRepository import WebSiteRepository, WebSites
from repositories.dbContext import DbContext

from helpers.envConfigurator import EnvConfigurator
from dotenv import load_dotenv


def run_test():
    load_dotenv()
    env_configurator = EnvConfigurator()
    logger = LoggerHelper()
    repo_manager = RepositoryManager(
        logger=logger,
        pageRepo=PageRepository(DbContext(db_url=env_configurator.MigrateConfiguration("MYSQL_DB"), model_class=Pages)),
        webSiteRepo=WebSiteRepository(
            DbContext(db_url=env_configurator.MigrateConfiguration("MYSQL_DB"), model_class=WebSites)),
        crawlLogRepo=CrawlLogRepository(
            DbContext(db_url=env_configurator.MigrateConfiguration("MYSQL_DB"), model_class=CrawlLog)),
        pageLinkRepo=PageLinkRepository(
            DbContext(db_url=env_configurator.MigrateConfiguration("MYSQL_DB"), model_class=PageLinks)),
        crawlRulesRepo=CrawlRulesRepository(
            DbContext(db_url=env_configurator.MigrateConfiguration("MYSQL_DB"), model_class=CrawlRules)),
        pageImageRepo=PageImageRepository(
            DbContext(db_url=env_configurator.MigrateConfiguration("MYSQL_DB"), model_class=PageImages)),
        pageContentsRepo=PageContentRepository(
            DbContext(db_url=env_configurator.MigrateConfiguration("MYSQL_DB"), model_class=PageContents))
    )

    service = CrawlService(
        logger=logger,
        robotsService=RobotsReaderService(logger=logger, robotsHelper=RobotFileParser()),
        repositoryManager=repo_manager
    )
    service.ExecuteCrawl("https://www.urhoba.net")
