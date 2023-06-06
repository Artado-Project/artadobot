from services.robotsScannerService import RobotsReaderService


def run_test():
    serivce = RobotsReaderService(None)
    serivce.InjectRobotPath("https://www.youtube.com/tr")
    serivce.ExecuteOperation()
