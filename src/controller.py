from bs4 import BeautifulSoup
from src.database import DatabaseRepository
from src.parser import ForumParser

class controller:

    db = None
    parser = ForumParser()
    def __init__(self,db : DatabaseRepository):
        self.db = db

    def parse_html(self,html):
        result = self.parser.parse_html(html)
        if result is []:
            return False, "Parser was empty"

        if not result:
            return False, "Parser was empty"

        for item in result:
            value, err = self.db.add(comment_id=item[0], username=item[1], message=item[2])
            if value != True:
                return False, err
        return True, ""
    def parse_page(self,url :str) ->(bool,str)   :
        result = self.parser.parse_page(url)
        if result is None:
            return False, "Parser was empty"

        if not result:
            return False, "Parser was empty"


        for item in result:
            value,err = self.db.add(comment_id=item[0],username = item[1], message=item[2])
            if value != True:
                return False,err
        return True,""