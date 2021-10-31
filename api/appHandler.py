import json
from flask import Flask
import requests
import sys
sys.path.insert(0, '/controllers/validator_handler/validator_handler.py')
from controllers.validator_handler.validator_handler import validator_quantity



app = Flask(__name__)

@app.route("/candidate", methods=["POST"])
def app_handler(event):
    name = event.get('name')
    years = event.get('years')
    titles = event.get('titles')
    req = f"https://torre.bio/api/bios/{name}".format(name = name)
    r = requests.get(req)
    json_value = r.json()
    tmp = validator_quantity(json_value, years, titles)
    return tmp