from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import requests

from helpers.LoggerHelper import LoggerHelper


class RequestHelper:

    @staticmethod
    def GetResponseContent(complete_page_url: str, logger: LoggerHelper):
        response = requests.get(complete_page_url)
        if response.status_code == 200:
            return response
        else:
            logger.Error(f" Request warning, Status Code = {response.status_code}, URL: {response.url}")
            return None

    pass
