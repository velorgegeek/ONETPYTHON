from abc import ABC, abstractmethod
import time

class TwoFactorAuthorization(ABC):

    @abstractmethod
    def getAuthorization(self)->bool:
        ...
class TwoFactor(TwoFactorAuthorization):
    def getAuthorization(self)->bool:
        time.sleep(1)
        return True