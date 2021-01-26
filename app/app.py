import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    url = "http://merde:8989/"
    x = requests.get(url)
    return "bravo ----==== " + str(x.text) + " ====----"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8787)