from http.server import HTTPServer
from server import HOSTNAME, SERVER_PORT, Server

def main() -> None:
    server = HTTPServer((HOSTNAME, SERVER_PORT), Server)
    print(f'Сервер запущен на http://{HOSTNAME}:{SERVER_PORT}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print('Сервер отключён')

if __name__ == "__main__":
    main()