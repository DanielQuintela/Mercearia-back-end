from main import app

@app.route("/")
def homepage():
    return "Olá mundo"