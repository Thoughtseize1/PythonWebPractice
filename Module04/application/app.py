import pathlib
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = pathlib.Path()
html_path = BASE_DIR / "index.html"


class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        file_path = BASE_DIR / "index.html"
        with open(file_path, "rb") as fd:
            self.wfile.write(fd.read())


def run(server=HTTPServer, handler=HTTPHandler):
    address = ("", 3000)
    http_server = server(address, handler)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == "__main__":
    run()
