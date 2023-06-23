from helpers.LoggerHelper import LoggerHelper
from services.crawlService import CrawlService
from services.robotsScannerService import RobotsReaderService
from urllib.robotparser import RobotFileParser


def run_test():
    logger = LoggerHelper()
    """load_dotenv()
    env_configurator = EnvConfigurator()
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
    """
    service = CrawlService(
        logger=logger,
        robotsService=RobotsReaderService(logger=logger, robotsHelper=RobotFileParser())
    )
    service.ExecuteCrawl("https://www.urhoba.net")
