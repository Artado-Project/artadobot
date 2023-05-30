from core.service import IService 
class RobotsReaderService(IService):
    
    def __init__(self, logger) -> None:
        super().__init__(logger)
    
    def InjectRobotPath(self, url: str):
        self.__injectedRobotsPath = url
        self.__robotsObject = {}
        self.__text = ""
    def __ReadPath(self):
        pass
    def __ConvertTextToObject(self, text: str):
        pass# convert opeartion
    def ExecuteOperation(self):
        pass