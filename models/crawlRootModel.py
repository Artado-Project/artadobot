from datetime import datetime, date


class Page:
    CanCrawl: bool
    Links: []
    Images: []
    Contents: {}
    Date: date

    def __init__(self):
        self.CanCrawl = False
        self.Images = []
        self.Links = []
        self.Contents = {}
        self.Date = datetime.now().date()


class SiteInfo:
    base_url: str
    using_js: bool
    using_php: bool
    using_dotnet: bool
    is_support_ios: bool
    is_support_android: bool


class Root:
    SiteInfo: SiteInfo
    Pages: dict[str, Page]

    def __init__(self):
        self.SiteInfo = SiteInfo()
        self.Pages = dict[str, Page]()

    pass
