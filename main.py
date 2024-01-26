from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
from typing import List
from urllib.parse import urlparse, parse_qs
from helpers.info import info


class SimpleHandler(SimpleHTTPRequestHandler):
    def _send_response(self, message, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, 'utf8'))

    def do_GET(self):
        print(self.path)
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        path = parsed_url.path

        if path == '/':
            with open("assets/pages/index.html", "r", encoding="utf-8") as file:
                html_content = file.read()
            self._send_response(html_content)

        if path == '/info':
            self._send_response(json.dumps(info))

        if path == '/image/:image':
            self._send_response("NOn-implemented")

        if path == '/urlParse':
            url_string: str = query_params["url"][0]
            parsed_url = urlparse(url_string)
            url_info = f"<p>It has {parsed_url.scheme} protocol;</p>\n" + \
                f"<p>domain is {parsed_url.netloc};</p>\n"
            path_steps = [step for step in parsed_url.path.split('/')[1:]]
            url_info += f"<p>it has {len(path_steps)} path steps: {' and '.join(path_steps)};</p>\n"
            if parsed_url.query != "":
                query_params = parse_qs(parsed_url.query)
                url_info += f"<p>and {len(query_params)} query parameters: {query_params}.</p>\n"
            else:
                url_info += "<p>and no query parameters.</p>\n"
            self._send_response(url_info)

    def do_POST(self):
        print(self.path)

        if self.path == '/fileParse':
            content_length = int(self.headers['Content-length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            post_data_dict = json.loads(post_data)

            text = post_data_dict['file']
            string = post_data_dict['string']

            if not text or not string:
                error_response = {'error': 'Both "file" and "string" parameters are required.'}
                self._send_response(json.dumps(error_response), status=400)
                return

            metadata = {
                'length_of_text': len(text),
                'alphanumeric_symbols': sum(char.isalnum() for char in text),
                'string_count': text.lower().count(string.lower())
            }

            self._send_response(json.dumps(metadata))


def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f'Starting server on "http://127.0.0.1:{port}"')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()


