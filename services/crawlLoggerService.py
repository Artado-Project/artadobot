from core.service import IService

class CrawlLoggerService(IService):
    def __init__(self, logger) -> None:
        super().__init__(logger)