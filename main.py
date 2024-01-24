from collections import Counter
import re

def frequently_words(text, words_number=5):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text_lowercase = text.lower()
    words = text_lowercase.split()
    count = Counter(words)
    frequently_words = count.most_common(words_number)

    return frequently_words

example_text = """

"""

resultado = frequently_words(example_text)
print("Palavras mais frequentes:", resultado)

from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/common_words":
            self.common_words()
        elif self.path == "/rota2":
            self.common_bad_words()
        elif self.path == "/rota3":
            self.common_good_words()
        else:
            self.resposta_404()

    def common_words(self):
        self.send_responses(200, "Test text 1")

    def common_bad_words(self):
        self.send_responses(200, "Test text 2")

    def common_good_words(self):
        self.send_responses(200, "Test text 3")

    def resposta_404(self):
        self.send_responses(404, "Not found page")

    def send_responses(self, status_code, message):
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

def init_server(port=8080):
    server_address = ("", port)
    server = HTTPServer(server_address, SimpleHandler)
    print(f"Servidor iniciado em http://localhost:{port}")
    server.serve_forever()

if __name__ == "__main__":
    init_server()
