from abc import ABC, abstractmethod
import time

class Notificator(ABC):

    @abstractmethod
    def send(self,message:str) -> bool:
        ...

    @abstractmethod
    def notificate(self,result)->bool:
        ...
class TelegramNotificator(Notificator):
    chat_id = None
    def send(self,message:str)->[bool,str]:
        time.sleep(1)
        return True,"message was send"

    def set_chat_id(self,chat_id):
        self.chat_id = chat_id
    def notificate(self,result:str)->[bool,str]:

        message= f"New user logged {result}"
        value, message=  self.send(message)
        return value,message