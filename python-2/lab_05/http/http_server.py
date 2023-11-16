import os
import http.server

class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path

        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open(os.path.join(os.path.dirname(__file__), "index.html"), "rb") as f:
                self.wfile.write(f.read())
        else:
            try:
                with open(path, "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-type", f.info.get("Content-Type"))
                    self.end_headers()
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Not found :0</h1>")


server = http.server.HTTPServer(("localhost", 8000), MyRequestHandler)
print("Server started on http://localhost:8000")
server.serve_forever()
