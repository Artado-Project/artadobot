from abc import ABC, abstractmethod

from helpers.LoggerHelper import LoggerHelper


class IService(ABC):
    @abstractmethod
    def __init__(self, logger: LoggerHelper) -> None:
        self._logger = logger
        super().__init__()

    pass
