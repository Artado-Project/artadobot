from urllib.parse import urlparse
import requests


class RobotsHelper:
    @staticmethod
    def ReadRobots(full_url: str):
        parsed_url = urlparse(full_url)
        robots_url = parsed_url.scheme + "://" + parsed_url.netloc + "/robots.txt"
        response = requests.get(robots_url)
        if response.status_code == 200:
            content = response.text
            return str(content)
        return None


class RequestHelper:
    pass
