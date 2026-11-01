import requests
from bs4 import BeautifulSoup
import re


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
        response = requests.get(page, headers=headers, timeout=10)
        bs = BeautifulSoup(response.text, 'html.parser')

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