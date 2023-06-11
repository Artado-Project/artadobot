from helpers.LoggerHelper import LoggerHelper
from services.crawlService import CrawlService
from services.robotsScannerService import RobotsReaderService
from urllib.robotparser import RobotFileParser


def run_test():
    logger = LoggerHelper()
    service = CrawlService(
        logger=logger,
        robotsService=RobotsReaderService(logger=logger, robotsHelper=RobotFileParser()))
    service.ExecuteCrawl("https://www.youtube.com")
