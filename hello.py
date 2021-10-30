from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    r = requests.get('https://torre.bio/api/bios/mateotoquica')
 
    return r.json()