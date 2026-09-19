import sqlite3
class repository:
    connection = None
    cursor = None

    def __init__(self):
        self.connection = sqlite3.connect('my_database.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           Login Text,
                           Password Text,
                           RepeatPassword Text,
                           ResultAutorization BOOLEAN,
                           TextError TEXT)''')
    def add(self,login,password,resultAutorization,textError) ->(bool,str):
        try:
            self.cursor.execute(
                "INSERT INTO users (login, password, RepeatPassword, resultAutorization, textError) "
                "VALUES (?, ?, ?, ?, ?)",
                (login, password, password, resultAutorization, textError),
            )
            self.connection.commit()
            return True,""
        except sqlite3.Error as error:
            return False,error
    def delete(self,login,password):
        try:
            self.cursor.execute('''DELETE FROM users WHERE login = ? AND Password = ?''',(login,password))
            self.connection.commit()
            return True,""
        except sqlite3.Error as error:
            return False,error
    def get(self,login,password):
        try:
            result = self.cursor.execute('''SELECT * FROM users WHERE login = ? AND Password = ?''',(login,password))
            self.connection.commit()
            return result,""
        except sqlite3.Error as error:
            return None,error
