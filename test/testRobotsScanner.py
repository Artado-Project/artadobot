from helpers.LoggerHelper import LoggerHelper
from services.robotsScannerService import RobotsReaderService
from urllib.robotparser import RobotFileParser


def run_test():
    # service = RobotsReaderService(LoggerHelper())
    # service.InjectRobotPath('https://github.com')
    # service.ExecuteOperation()
    # variable = service.ReturnObject()
    url = "https://www.youtube.com"
    service = RobotsReaderService(LoggerHelper(), RobotFileParser())
    service.ScanRobotsFile(url)
    if service.CanFetchUrl("*", url + "/account"):
        print("ALLOWED")
    else:
        print("DISALLOWED")

    text = service.BuildDataAsText()
    print(text)