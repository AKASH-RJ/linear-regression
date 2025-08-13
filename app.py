
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        speed = float(request.form["speed"])
        engine = float(request.form["engine"])
        weight = float(request.form["weight"])
        input_data = np.array([[speed, engine, weight]])
        prediction = model.predict(input_data)[0]
        prediction = round(prediction, 2)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
