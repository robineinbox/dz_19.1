import requests
import base64
from http.server import BaseHTTPRequestHandler

HOSTNAME = 'localhost'
SERVER_PORT = 8000


class Server(BaseHTTPRequestHandler):
    '''
    Класс сервера магазина
    '''

    def __get_html_from_git(self) -> str:
        '''
        Получает данные HTML-файла с удаленного репозитория
        :return: html-код
        '''
        headers = {
            'Authorization': 'token ' + 'YOUR_TOKEN'
        }
        data = requests.get(
            url='https://api.github.com/repos/robineinbox/web-homework/contents/homework_1/html/index.html'
        )
        html_data = data.text
        return html_data

    def do_GET(self):
        '''
        Обрабатывает GET-запросы, отправленные на сервер
        '''
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(self.__get_html_from_git(), 'utf-8'))