
import src.controller as c
import src.database as db
if __name__ == '__main__':
    controller = c.controller(db.DatabaseRepository('my_db.db'))
    result = controller.parse_page('https://www.cyberforum.ru/cpp-networks/thread3217388.html')
    print(result)
