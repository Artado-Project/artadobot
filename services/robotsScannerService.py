from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
from core.service import IService
from helpers.LoggerHelper import LoggerHelper


class RobotsReaderService(IService):

    def __init__(self, logger: LoggerHelper, robotsHelper: RobotFileParser) -> None:
        super().__init__(logger)
        self.__text = ""
        self.__robotsHelper: RobotFileParser = robotsHelper

    def ScanRobotsFile(self, url: str):
        self._logger.Info(f"Scanning robots file for {url}")
        parsed_url = urlparse(url)
        robots_url = parsed_url.scheme + "://" + parsed_url.netloc + "/robots.txt"
        self.__robotsHelper.set_url(robots_url)
        self.__robotsHelper.read()

    def CanFetchUrl(self, agent: str, sub_url: str) -> bool:
        return self.__robotsHelper.can_fetch(agent, sub_url)

    def GetAgentDelay(self, agent: str):
        return self.__robotsHelper.crawl_delay(agent)

    def GetAgentRequestRate(self, agent: str):
        return self.__robotsHelper.request_rate(agent)

    def BuildDataAsText(self) -> str | None:
        if self.__robotsHelper is not None:
            self.__text = str(self.__robotsHelper)
            return self.__text
        else:
            return None
