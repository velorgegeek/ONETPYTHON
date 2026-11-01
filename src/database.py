import sqlite3
from doctest import FAIL_FAST


class DatabaseRepository:
    def __init__(self, database_path: str):
        self.connection = sqlite3.connect(database_path)
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                message TEXT NOT NULL
            )
        """)
        self.connection.commit()


    def get_by_id(self, comment_id: int)-> tuple[list,str]:
        try:
            cursor = self.connection.execute(
                """
                SELECT id, name, message
                FROM comments
                WHERE id = ?
                """,
                (comment_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None, "Комментарий не найден"

            return row, ""


        except sqlite3.Error as error:
            return None,str(error)


    def get_by_name(self, username: str) -> tuple[list,str]:
        try:
            cursor = self.connection.execute(
                """
                SELECT id, name, message
                FROM comments
                WHERE name = ?
                ORDER BY id
                """,
                (username,)
            )

            row = cursor.fetchone()

            if row is None:
                return None, "Комментарий не найден"

            return row, ""

        except sqlite3.Error as error:
            return None,str(error)

    def add(self, comment_id: int, username: str, message: str) -> tuple[bool, str]:
        try:
            self.connection.execute(
                """
                INSERT INTO comments (id, name, message)
                VALUES (?, ?, ?)
                """,
                (comment_id, username, message)
            )
            self.connection.commit()

        except sqlite3.Error as error:
            return False,str(error)
        return True,""


    def update(self, comment_id: int, new_message: str) -> tuple[bool, str]:

        try:
            cursor = self.connection.execute(
                """
                UPDATE comments
                SET message = ?
                WHERE id = ?
                """,
                (new_message, comment_id)
            )
            self.connection.commit()

            if cursor.rowcount == 0:
                return False, "Комментарий не найден"

            return True, ""

        except sqlite3.Error as error:
            return False,str(error)

    def delete(self, comment_id: int) -> tuple[bool, str]:
        try:
            cursor = self.connection.execute(
                """
                DELETE FROM comments
                WHERE id = ?
                """,
                (comment_id,)
            )
            self.connection.commit()

            if cursor.rowcount == 0:
                return False, "Комментарий не найден"

            return True, ""

        except sqlite3.Error as error:
            return False,str(error)

    def __del__(self):
        self.connection.close()
