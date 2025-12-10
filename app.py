from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "The vercel is working"

@app.route("/api")
def api():
    return "This is vercel api that you can see"

@app.route("/project 1")
def project():
    return "This is project one"

if __name__ == "__main__":
    app.run()