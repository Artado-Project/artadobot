from helpers.LoggerHelper import LoggerHelper
from services.robotsScannerService import RobotsReaderService


def run_test():
    service = RobotsReaderService(LoggerHelper())
    service.InjectRobotPath('https://github.com')
    service.ExecuteOperation()
    variable = service.ReturnObject()
