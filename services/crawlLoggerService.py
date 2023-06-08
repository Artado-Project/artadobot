from core.service import IService
from helpers.LoggerHelper import LoggerHelper


class CrawlLoggerService(IService):
    def __init__(self, logger: LoggerHelper) -> None:
        super().__init__(logger)
