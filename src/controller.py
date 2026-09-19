import sys
import logging
from src.repo import repository
from src.user_input import user_input
from src.validate import validate
from src.TwoFactorAuthorization import TwoFactor as TwoFactorAuthorization
from pathlib import Path
class controller:
    repo = repository()
    user_input = user_input()
    validate = validate()
    TwoFactor  = TwoFactorAuthorization()

    def setupLoging(self):
        LOG_DIR = Path(__file__).resolve().parent.parent / "logs"  # ONETPYTHON/logs
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        LOG_FILE = LOG_DIR / "file_txt.log"

        def setupLoging(self):
            logging.basicConfig(
                level=logging.DEBUG,
                format="%(asctime)s | [%(levelname)-7s] | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                handlers=[
                    logging.StreamHandler(sys.stdout),
                    logging.FileHandler(LOG_FILE, encoding="utf-8"),
                ],
            )

        logging.info("Логгер успешно сконфигурирован")
        logging.info("Приложение запущено")

    def add(self):
        login, password,password2 = self.__input__()
        valid, error = self.validate.validate(login,password,password2)

        if(valid is False):
            logging.warning(error)

        if self.TwoFactor.getAuthorization() != True:
            logging.info("вход через двух факторовку")
            pass

        isAdd ,textError = self.__add__(login,password,valid,error)

        if isAdd is False:
            logging.error(textError)


        return isAdd,textError

    def delete(self):
        login, password, password2 = self.__input__()
        valid, error = self.validate.validate(login, password, password2)

        if (valid is False):
            logging.error(error)

        is_delete,text_error = self.__delete__(login,password)
        if is_delete is False:
            logging.error(text_error)

        return is_delete,text_error

    def get(self):
        login, password,password2 = self.__input__()
        value,error = self.repo.get(login,password)
        if value is None:
            logging.warning(error)
        return value,error

    def __input__(self):
        logging.info("Юзер вводит данные")
        login, password,password2 = self.user_input.input()
        return login,password,password2

    def __validate__(self,login,password,passRepeat):
        logging.info("Проходит валидация")
        return self.validate.validate(login,password,passRepeat)

    def __add__(self,login,password,AuthorizationValue,TextError):
        logging.info("Добавление пользователя")
        isAdd,textValue =self.repo.add(login,password,AuthorizationValue,TextError)

        return isAdd,textValue

    def __get__(self,login,password):
        logging.info("Получение пользователя")
        value,error  = self.repo.get(login,password)

        if value is not None:
            logging.error(error)

        return value,error


    def __delete__(self,login,password):
        logging.info("Удаление пользователя")
        isDelete,textValue = self.repo.delete(login,password)

        if isDelete is False:
            logging.error(textValue)

        return isDelete,textValue