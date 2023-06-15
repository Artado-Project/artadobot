from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import requests

from helpers.LoggerHelper import LoggerHelper


class RequestHelper:

    @staticmethod
    def GetResponseContent(complete_page_url: str):
        return requests.get(complete_page_url)
    pass
