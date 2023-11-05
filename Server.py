# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:42:43 2023

@author: Kushal
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:56:58 2023

@author: Kushal
"""


from flask import Flask,request, jsonify
import os
from roboflow import Roboflow


app = Flask(__name__)

rf = Roboflow(api_key="7ZBY6Mq7nyCsWG8IdbZC")
project = rf.workspace().project("trash-detection-otdmj")


recycle_dict = {
    "Recycle": [
        "Aluminium blister pack",
        "Aluminium foil",
        "Bottle",
        "Bottle cap",
        "Carded blister pack",
        "Clear plastic bottle",
        "Corrugated carton",
        "Drink can",
        "Drink carton",
        "Egg carton",
        "Food Can",
        "Food Carton",
        "Glass bottle",
        "Glass jar",
        "Metal bottle cap",
        "Metal lid",
        "Other can",
        "Other carton",
        "Other container",
        "Other plastic",
        "Other plastic bottle",
        "Other plastic container",
        "Other plastic cup",
        "Other plastic wrapper",
        "Paper",
        "Paper bag",
        "Paper cup",
        "Paper straw",
        "Plastic bottle cap",
        "Pop tab",
        "Scrap metal",
        "Six pack rings",
        "Unlabeled litter",
        "Wrapping paper"
    ],
    "Compost": [
        "Food waste",
        "Meal carton",
        "Polypropylene bag",
        "Tissues",
        "Toilet tube"
    ],
    "Landfill": [
        "Aerosol",
        "Battery",
        "Broken glass",
        "Cigarette",
        "Crisp packet",
        "Cup",
        "Disposable food container",
        "Disposable plastic cup",
        "Foam cup",
        "Foam food container",
        "Garbage bag",
        "Glass cup",
        "Lid",
        "Magazine paper",
        "Normal paper",
        "Other Carton",
        "Other plastic wrapper",
        "Plastic film",
        "Plastic gloves",
        "Plastic lid",
        "Plastic straw",
        "Plastic utensils",
        "Pop tab",
        "Rope & strings",
        "Shoe",
        "Single-use carrier bag",
        "Spread tub",
        "Squeezable tube",
        "Straw",
        "Styrofoam piece",
        "Toilet tube",
        "Tupperware"
    ]
}

def classify_item(item, recycle_dict):
    for category, items in recycle_dict.items():
        if item in items:
            return category
    return "Unknown"


def x(path):
    model = project.version(35).model
    x = (model.predict(f'{path}.jpeg', confidence=40, overlap=30).json())
    print(x)
    a = x['predictions'][0]['class']
    print(a)
    classification = classify_item(a, recycle_dict)
    return classification


@app.route('/i')
def bruh():
    print('Summary Entry 1')
    ticker = request.args['img']
    return jsonify(x(ticker))


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

