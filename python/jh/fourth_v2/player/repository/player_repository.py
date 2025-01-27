from abc import ABC, abstractmethod


class PlayerRepository(ABC):

    @abstractmethod
    def createNumAndName(self):
        pass
