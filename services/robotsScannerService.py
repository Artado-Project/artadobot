from core.service import IService
from helpers.LoggerHelper import LoggerHelper
from helpers.requestHelper import RobotsHelper
from models.RobotsTxt import RobotsTxt


class RobotsReaderService(IService):

    def __init__(self, logger: LoggerHelper) -> None:
        super().__init__(logger)
        self.__injectedRobotsPath = ""
        self.__robotsObject = RobotsTxt()
        self.__current_user = ""
        self.__current_disallow_rule = ""
        self.__current_allow_rule = ""

    def InjectRobotPath(self, url: str):
        self.__injectedRobotsPath = url

    def __ConvertTextToObject(self, text: str):
        self._logger.Info("ROBOTS RULES CONVERTING AN OBJECT")
        lines = text.split('\n')
        for line in lines:
            if line.startswith('User-agent:'):
                self.__current_user = line.split(': ')[1]
            elif line.startswith('Disallow'):
                self.__current_disallow_rule = line.split(': ')[1:]
                self.__robotsObject.AddRule(self.__current_user, self.__current_disallow_rule, None)
            elif line.startswith('Allow:'):
                self.__current_allow_rule = line.split(': ')[1:]
                self.__robotsObject.AddRule(self.__current_user, None, self.__current_allow_rule)
            elif line.startswith('Crawl-delay:') or line.startswith("crawl-delay:"):
                self.__robotsObject.set_rate_limit(user_agent=self.__current_user, rate_limit=line.split(': ')[1:])
            elif line.startswith('Sitemap:'):
                self.__robotsObject.add_sitemap(line.split(': ')[1:])
            else:
                continue

    def ExecuteOperation(self):
        try:
            if self.__injectedRobotsPath is not None or "":
                self._logger.Info("ROBOTS.TXT FILE READING...")
                text = RobotsHelper.ReadRobots(self.__injectedRobotsPath)
                self.__robotsObject.set_text(text)
                self.__ConvertTextToObject(text)
        except Exception as e:
            self._logger.Error(e)
            pass
        pass

    def ReturnObject(self):
        self._logger.Info("Robots Data Building...")
        self.__robotsObject.Build_Data()
        return self.__robotsObject
