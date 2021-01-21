import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    url = "http://thefirstcontainer:8080/"
    x = requests.get(url)
    return "maya ----==== " + str(x.text) + " ====----"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8989)