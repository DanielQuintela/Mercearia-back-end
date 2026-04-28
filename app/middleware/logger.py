from flask import request

def request_logger(app):
    @app.before_request
    def log_request():
        body = request.get_data(as_text=True) if request.is_json else None
        print(f"[REQUEST] {request.method} {request.path} - Body: {body}")
