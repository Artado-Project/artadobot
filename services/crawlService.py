from core.service import IService

class CrawlService(IService):
    
    def __init__(self, logger) -> None:
        super().__init__(logger)