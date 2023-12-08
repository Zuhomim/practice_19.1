from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostname = 'localhost'
server_port = 8088


class MyServer(SimpleHTTPRequestHandler):
    """Класс веб-приложения на локальном адресе, порт 8088"""

    def __get_html_content(self):
        """Возвращает html-content из файла index.html"""
        with open("index.html", 'rt') as f:
            page_content = f.read()

        return page_content

    def do_get(self):
        """Обработка GET-запросов (получаем html-content)"""

        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":

    web_server = HTTPServer((hostname, server_port), MyServer)

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
