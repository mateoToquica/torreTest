import json
from flask import Flask, request
import requests
import sys

sys.path.insert(0, '/controllers/validator_handler/validator_handler.py')
from controllers.validator_handler.validator_handler import validator_quantity
from flask_cors import CORS




app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/candidate", methods=["POST"])
def app_handler():
    name = request.json['name']
    years = request.json['work_experience']
    titles = request.json['titles']
    req = f"https://torre.bio/api/bios/{name}".format(name = name)
    r = requests.get(req)
    json_value = r.json()
    tmp = validator_quantity(json_value, years, titles)
    return tmp

if __name__ == "__main__":
    app.run()