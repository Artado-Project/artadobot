class RobotsTxt:
    def __init__(self):
        self.__user_agents = {}
        self.__sitemaps = []
        self.__root = {}
        self.__text = ""

    def AddRule(self, user_agent, disallow, allow):
        if user_agent not in self.__user_agents:
            self.__user_agents[user_agent] = {"Disallow": [], "Allow": [], "Crawl-Delay": []}
        if disallow is not None:
            self.__user_agents[user_agent]["Disallow"].extend(disallow)
        if allow is not None:
            self.__user_agents[user_agent]["Allow"].extend(allow)

    def CheckIsAllowed(self, user_agent, url) -> bool:
        if user_agent in self.__root["RULES"]:
            if url in self.__root["RULES"][user_agent]["Disallow"]:
                return False
            elif url in self.__root["RULES"][user_agent]["Allow"]:
                return True
            else:
                return True
        raise Exception("INVALID USER-AGENT")

    def set_rate_limit(self, user_agent, rate_limit):
        if user_agent not in self.__user_agents:
            self.__user_agents[user_agent] = {"Disallow": [], "Allow": [], "Crawl-Delay": []}
        if rate_limit is not None:
            self.__user_agents[user_agent]["Crawl-Delay"].extend(rate_limit)

    def add_sitemap(self, sitemap):
        if sitemap is not None:
            self.__sitemaps.append(sitemap)

    def set_text(self, text: str):
        self.__text = text

    def get_as_text(self) -> str:
        return self.__text

    def Build_Data(self):
        self.__root['RULES'] = self.__user_agents
        self.__root['SITEMAPS'] = self.__sitemaps
        return self.__root

