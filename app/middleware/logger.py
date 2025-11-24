from flask import request

def request_logger(app):
    @app.before_request
    def log_request():
        body = request.get_json(silent=True)
        print(f"[REQUEST] {request.method} {request.path} - Body: {body}")
