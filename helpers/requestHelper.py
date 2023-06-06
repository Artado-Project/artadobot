from urllib import robotparser
from urllib.parse import urlparse


class RobotsHelper:
    @staticmethod
    def ReadRobots(full_url: str):
        parsed_url = urlparse(full_url)
        robots_url = parsed_url.scheme + "://" + parsed_url.netloc + "/robots.txt"
        rp = robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()

        return str(rp)


class RequestHelper:
    pass
