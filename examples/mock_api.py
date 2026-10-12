"""Local learning API. No third-party dependencies; data lives in memory."""
import argparse
import json
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

TOKEN = 'demo-token'

class UsersServer(ThreadingHTTPServer):
    daemon_threads = True
    def __init__(self, address):
        super().__init__(address, UsersHandler)
        self.users = {}
        self.next_id = 1
        self.lock = threading.RLock()

class UsersHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Do not log request bodies or authorization headers.

    def reply(self, status, payload=None):
        content = b'' if payload is None else json.dumps(payload).encode('utf-8')
        self.send_response(status)
        if payload is not None:
            self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        if content:
            self.wfile.write(content)

    def error(self, status, error):
        self.reply(status, {'error': error})

    def body(self):
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 100_000:
                self.error(400, 'invalid_json')
                return None
            value = json.loads(self.rfile.read(length))
            if not isinstance(value, dict):
                self.error(422, 'validation_error')
                return None
            return value
        except (ValueError, UnicodeError):
            self.error(400, 'invalid_json')
            return None

    def route(self):
        parsed = urlparse(self.path)
        if parsed.path == '/health' and self.command == 'GET':
            self.reply(200, {'status': 'ok'})
            return
        if self.headers.get('Authorization') != f'Bearer {TOKEN}':
            self.error(401, 'unauthorized')
            return
        match = re.fullmatch(r'/users(?:/(\d+))?/?', parsed.path)
        if not match:
            self.error(404, 'not_found')
            return
        user_id = int(match.group(1)) if match.group(1) else None
        if self.command == 'GET':
            with self.server.lock:
                if user_id is not None:
                    user = self.server.users.get(user_id)
                    self.reply(200, dict(user)) if user is not None else self.error(404, 'not_found')
                    return
                query = parse_qs(parsed.query)
                try:
                    limit = int(query.get('limit', ['100'])[0])
                    if not 1 <= limit <= 100:
                        raise ValueError()
                except ValueError:
                    self.error(422, 'validation_error')
                    return
                items = [dict(user) for user in self.server.users.values()]
                self.reply(200, {'items': items[:limit], 'total': len(items)})
            return
        if self.command == 'DELETE' and user_id is not None:
            with self.server.lock:
                if user_id not in self.server.users:
                    self.error(404, 'not_found')
                else:
                    del self.server.users[user_id]
                    self.reply(204)
            return
        if self.command == 'POST' and user_id is None or self.command == 'PATCH' and user_id is not None:
            payload = self.body()
            if payload is None:
                return
            with self.server.lock:
                if self.command == 'PATCH' and user_id not in self.server.users:
                    self.error(404, 'not_found')
                    return
                if set(payload) - {'name', 'email'}:
                    self.error(422, 'validation_error')
                    return
                candidate = dict(self.server.users[user_id]) if self.command == 'PATCH' else {}
                candidate.update(payload)
                name, email = candidate.get('name'), candidate.get('email')
                if not isinstance(name, str) or not 1 <= len(name.strip()) <= 100:
                    self.error(422, 'validation_error')
                    return
                if not isinstance(email, str) or not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', email):
                    self.error(422, 'validation_error')
                    return
                email = email.lower()
                if any(user['email'] == email and identity != user_id for identity,user in self.server.users.items()):
                    self.error(409, 'duplicate_email')
                    return
                created = self.command == 'POST'
                if created:
                    user_id = self.server.next_id
                    self.server.next_id += 1
                user = {'id': user_id, 'name': name.strip(), 'email': email}
                self.server.users[user_id] = user
                self.reply(201 if created else 200, user)
            return
        self.error(405, 'method_not_allowed')

    do_GET = do_POST = do_PATCH = do_DELETE = route

def main():
    parser = argparse.ArgumentParser(description='Way2Python local practice API')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    with UsersServer(('127.0.0.1', args.port)) as server:
        print(f'Practice API: http://127.0.0.1:{server.server_port} · token: demo-token', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
