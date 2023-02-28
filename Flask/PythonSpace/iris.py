"""
Create on 2023-02-06
author : LucheSia
Descripytion: Flutter 와 Python의 AI 의 예측값 보내기 
"""

from flask import Flask, jsonify, request, render_template
import joblib

app = Flask(__name__)

@app.route("/iris")
def iris():
    sepalLength = float(request.args.get("sepalLength"))
    sepalWidth = float(request.args.get("sepalWidth"))
    petalLength = float(request.args.get("petalLength"))
    petalWidth = float(request.args.get("petalWidth"))

    clf = joblib.load("./rf_iris.h5")
    pred = clf.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])

    return jsonify({
        'result' : pred[0][5:]
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)