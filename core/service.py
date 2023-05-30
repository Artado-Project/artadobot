from abc import ABC, abstractmethod
class IService(ABC):
    @abstractmethod
    def __init__(self, logger) -> None:
        self._logger = logger
        super().__init__()
    pass