from typing import List
from bs4 import BeautifulSoup
import requests


class PageHelper:

    @staticmethod
    def GetLinkInsidePage(complete_page_url: str) -> List:
        response = requests.get(complete_page_url)
        soup = BeautifulSoup(response.content, features="html.parser")
        links = soup.findAll("a")
        return links
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


