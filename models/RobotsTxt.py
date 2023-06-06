class RobotsTxt:
    def __init__(self):
        self.__user_agents = {}
        self.__rate_limit = None
        self.__sitemaps = []
        self.__root = {}

    def AddRule(self, user_agent, disallow, allow):
        if user_agent not in self.__user_agents:
            self.__user_agents[user_agent] = {"Disallow": [], "Allow": []}
        if disallow is not None:
            self.__user_agents[user_agent]["Disallow"].extend(disallow)
        if allow is not None:
            self.__user_agents[user_agent]["Allow"].extend(allow)

    def set_rate_limit(self, rate_limit):
        if rate_limit is not None:
            self.__rate_limit = rate_limit

    def add_sitemap(self, sitemap):
        if sitemap is not None:
            self.__sitemaps.append(sitemap)

    def get_data(self):
        self.__root['RULES'] = self.__user_agents
        self.__root['SITEMAPS'] = self.__sitemaps
        self.__root['CRAWL-DELAY'] = self.__rate_limit
        return self.__root
