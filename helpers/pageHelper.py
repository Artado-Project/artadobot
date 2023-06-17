from typing import List
from bs4 import BeautifulSoup
import requests
from requests import Response

from helpers.LoggerHelper import LoggerHelper


class PageHelper:

    @staticmethod
    def GetLinkInsidePage(response: Response) -> List:
        soup = BeautifulSoup(response.content, features="html.parser")
        links = soup.findAll("a")
        return links

    @staticmethod
    def GetImageLinksPage(response: Response) -> List:
        soup = BeautifulSoup(response.content, features="html.parser")
        images = soup.findAll("img")
        return images

    @staticmethod
    def FindPageContents(response: Response):
        soup = BeautifulSoup(response.content, features="html.parser")
        title = soup.title.string
        description = soup.find('meta', attrs={'name': 'description'})['content']
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        print(keywords)

    @staticmethod
    def ConfigureUrl(base_url: str, a_link_url: str) -> str:
        if a_link_url.startswith("/"):
            return base_url + a_link_url
        elif a_link_url.startswith(base_url):
            return a_link_url
        else:
            return ""
