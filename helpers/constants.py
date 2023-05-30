from enum import Enum


class TableNames(Enum):
    CrawLog = "CrawlLog"
    CrawRules = "CrawRules"
    PageContents = "PageContents"
    PageImages = "PageImages"
    PageLinks = "PageLinks"
    Pages = "Pages"
    WebSites = "WebSites"

class AppTypes(Enum):
    BotApplication = 0
    RestApplication = 1