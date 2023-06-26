from typing import List
from bs4 import BeautifulSoup
from requests import Response
from collections import Counter
import re


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
    def FindPageContents(response: Response) -> {}:
        content_tuple = {}
        total_keywords = []
        soup = BeautifulSoup(response.content, features="html.parser")
        title = soup.find('title')
        description = soup.find('meta', attrs={'name': 'description'})
        keyword = soup.find('meta', attrs={'name': 'keywords'})
        words = re.sub(r'\W+', ' ', soup.get_text().lower()).split()
        word_counts = Counter(words)
        common_keywords = word_counts.most_common(10)
        if keyword is not None:
            total_keywords.append(keyword)
        for key, value in common_keywords:
            total_keywords.append(key)

        content_tuple['title'] = title.string if title is not None else ""
        content_tuple['description'] = description if title is not None else ""
        content_tuple['keywords'] = total_keywords if total_keywords is not None and len(total_keywords) > 0 else []
        return content_tuple

    @staticmethod
    def ConfigureUrl(base_url: str, a_link_url: str) -> str:
        if a_link_url.startswith("/"):
            return base_url + a_link_url
        elif a_link_url.startswith(base_url):
            return a_link_url
        else:
            return ""
