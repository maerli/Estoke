import http.server
import socketserver


from http.server import BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
  def do_HEAD(self):
    return

  def do_GET(self):
    self.respond()

  def do_POST(self):
    return

  def handle_http(self, status, content_type):
    self.send_response(status)
    self.send_header("Content-type", content_type)
    self.end_headers()
    return bytes("Hello World", "UTF-8")

  def respond(self):
    content = self.handle_http(200, "text/html")
    self.wfile.write(content)


PORT = 80

with socketserver.TCPServer(("", PORT), Server) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
