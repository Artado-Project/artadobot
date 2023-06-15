from typing import List
from bs4 import BeautifulSoup
import requests
from requests import Response

from helpers.LoggerHelper import LoggerHelper


class PageHelper:

    @staticmethod
    def GetLinkInsidePage(response: Response, logger: LoggerHelper) -> List:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, features="html.parser")
            links = soup.findAll("a")
            return links
        else:
            logger.Error(f" Request warning, Status Code = {response.status_code}, URL: {response.url}")
            return []
        pass

    @staticmethod
    def GetImageLinksPage(complete_page_url: str) -> List:
        pass

    @staticmethod
    def GetFavIcon(complete_page_url: str) -> str:
        pass

    @staticmethod
    def FindKeywords(complete_page_url: str) -> List:
        pass

    @staticmethod
    def GetContentType(page_uri: str) -> bool:
        pass

    @staticmethod
    def ConfigureUrl(base_url: str, a_link_url: str) -> str:
        if a_link_url.startswith("/"):
            return base_url + a_link_url
        elif a_link_url.startswith(base_url):
            return a_link_url
        else:
            return ""



