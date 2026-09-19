import re
class validate:
    validate_num_regex = r"^\+?[1-9][0-9]{7,14}$"
    validate_email_regex = r"^\S+@\S+\.\S+$"

    specialSimbol = r"!@#$%^&*()_+=;:,./?\|"
    blockedName = {"admin",
                   "test",
                   "adminboss42",
                   "redsusik228"}

    def __init__(self): pass
    def validate(self,login,password,password2)-> (bool,str):
        value,response = self.__validLogin__(login)
        if(value == False):
            return value,response

        passValue,passResponse =self.__validPassword__(password,password2)
        if(passValue == False):
            return value,response

        return True,""
    def __validPassword__(self,Password, Password2) -> tuple[bool, str]:
        if len(Password) < 7:
            return False, "Слишком маленький пароль"
        if not re.search(r'[А-Я]', Password):
            return False, "Нет заглавных букв кириллицей"
        if not re.search(r'[а-я]', Password):
            return False, "Нет строчных букв кириллицей"
        if not re.search(r'\d', Password):
            return False, "Нет чисел в пароле"
        if not set(Password) & set(self.specialSimbol):
            return False, "Нет спец символов в пароле"
        if (Password != Password2):
            return False, "Пароли отличаются"
        return True, ""

    def __validLogin__(self,Login: str) -> tuple[bool, str]:
        if (re.match(self.validate_email_regex, Login)):
            return True, ""
        if (re.match(self.validate_num_regex, Login.replace(" ", ""))):
            return True, ""

        if len(Login) < 5:
            return False, "Логин слишком маленький"
        if (not re.fullmatch(r'^[A-Za-z0-9_]+$', Login)):
            return False, "Есть недопустимые символы"
        if not re.search(r'[_]', Login):
            return False, "Нет спецсимволов в логине"
        if Login in self.blockedName:
            return False, "Логин заблокирован"

        return True, ""
