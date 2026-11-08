
import src.controller as c
import src.database as db
import src.parser as p
if __name__ == '__main__':
    controller = c.controller(db.DatabaseRepository('my_db.db'))
    pars = p.ForumParser()
    result = controller.parse_page('https://www.cyberforum.ru/cpp-beginners/thread3225750.html')
    print(result)
