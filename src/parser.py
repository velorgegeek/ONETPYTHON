import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin

class ForumParser:
    def get_html(self,url) ->requests.Response:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 YaBrowser/26.8.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
        }
        response = requests.get(url, headers=headers, timeout=10)
        return response

    def parse_html(self,response : str) -> list:
        bs = BeautifulSoup(response, 'html.parser')

        posts = bs.select('table[id^="post"]')

        results = []
        for p in posts:
            name = p.find('a', class_='bigusername')
            message = p.find('div', id=re.compile(r'^post_message_\d+$'))
            post_id = message['id'].replace('post_message_', '')

            text = message.get_text(strip=True)
            result = [post_id, name.get_text(), text]

            results.append(result)

        return results



    def parse_page(self, page):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 YaBrowser/26.8.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
        }

        results = []
        this_page = page
        set_result = set()
        while True:
            print(this_page)
            response = requests.get(this_page, headers=headers, timeout=20)

            bs = BeautifulSoup(response.text, 'html.parser')

            posts = bs.select('table[id^="post"]')
            if not posts:
                break



            for p in posts:
                name = p.find('a', class_='bigusername')
                message = p.find('div', id=re.compile(r'^post_message_\d+$'))

                for quote in message.select('div.bbcode_container'):
                    quote.decompose()

                post_id = message['id'].replace('post_message_', '')
                if post_id in set_result:
                    continue
                set_result.add(post_id)
                text = message.get_text(separator=' ',strip=True)
                result = [post_id, name.get_text(), text]

                results.append(result)

            next_link = bs.find('a', rel='next')
            if not next_link or not next_link.get('href'):
                break

            this_page = urljoin(this_page, next_link['href'])


            time.sleep(1)
        return results