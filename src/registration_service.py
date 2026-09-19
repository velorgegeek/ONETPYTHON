import logging
import sys
import re


validate_num_regex = r"^\+?[1-9][0-9]{7,14}$"
validate_email_regex = r"^\S+@\S+\.\S+$"

specialSimbol = r"!@#$%^&*()_+=;:,./?\|"

blockedName= {"admin",
              "test",
              "adminboss42",
              "redsusik228"}

def main():
    setupLoging()

def setupLoging():

    log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(sys.stdout),  # Настройка логирования в консоль
            logging.FileHandler("logs/file_txt.log", encoding="utf-8")  # Настройка логирования в файл
        ]
    )

    logging.info("Логгер успешно сконфигурирован")
    logging.info("Приложение запущено")

def validPassword(Password,Password2)->tuple[bool,str]:
    logging.info(f"Валидация пароля {Password}")
    if len(Password) < 7:
        return False,"Слишком маленький пароль"
    if not re.search(r'[А-Я]', Password):
        return False,"Нет заглавных букв кириллицей"
    if not re.search(r'[а-я]',Password):
        return False,"Нет строчных букв кириллицей"
    if not re.search(r'\d',Password):
        return False, "Нет чисел в пароле"
    if not set(Password) & set(specialSimbol):
        return False, "Нет спец символов в пароле"
    if(Password != Password2):
        return False, "Пароли отличаются"
    return True,""

def validLogin(Login :str) -> tuple[bool,str]:
    logging.info(f"Валидация Логина {Login}")
    if(re.match(validate_email_regex, Login)):
        return True,""
    if(re.match(validate_num_regex, Login.replace(" ", ""))):
         return True,""


    if len(Login) < 5 :
        return False,"Логин слишком маленький"
    if(not re.fullmatch(r'^[A-Za-z0-9_]+$', Login)):
        return False,  "Есть недопустимые символы"
    if not re.search(r'[_]', Login):
        return False, "Нет спецсимволов в логине"
    if Login in blockedName:
        return False, "Логин заблокирован"

    return True,""

def register(Login, Password,Password2) -> tuple(bool,str):
    logging.info(f"Пользователь пытается зарегистрироваться: Логин {Login},Password {Password},Password2 {Password2}")
    try:

        isValid,message = validLogin(Login)
        if(not isValid):
            logging.error(f"Ошибка валидации Логина: {Login}  message: {message}")
            return False,message

        logging.debug("Валидация логина успешна.")

        passIsValid,message = validPassword(Password,Password2)
        if(not passIsValid):
            logging.error(f"Ошибка валидации Пароля: {Password} message: {message} ")
            return False,message
        logging.debug("Валидация пароля успешна.")

        logging.info("Регистрация успешна.")

        return True,""
    except Exception as e:
        logging.exception("Критическая ошибка при валидации:")
        return False,f"Внутренняя ошибка: {str(e)}"



if __name__ == "__main__":
    main()
    valid,msg = register("AZAZAZAZAZ_8","абвгдежН7_","абвгдежН7_")
    print(msg)

