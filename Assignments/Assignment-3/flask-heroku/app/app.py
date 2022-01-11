# import modules
from app.acreCalculation import calculateAcre
from flask import Flask, json, jsonify, request

# instantiate flask object
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_input():
    """
    A flask app to take input and invoke acre calcuation module to process input parameter in square fee and return the area in acre
    """
    packet = request.get_json(force=True)
    length = packet['length']
    width = packet['width']

    areaInAcre = calculateAcre(length, width)

    return jsonify({"area-in-acre": areaInAcre, "input": packet})
