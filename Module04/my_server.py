from http.server import HTTPServer, BaseHTTPRequestHandler
import os

directory = "application"


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"{self.path=}")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open(os.path.join(directory, "index.html"), "rb") as main_file:
            self.wfile.write(main_file.read())


def run():
    http = HTTPServer(("localhost", 8000), CustomHTTPRequestHandler)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    run()
