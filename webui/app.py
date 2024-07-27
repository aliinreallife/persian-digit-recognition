from flask import Flask, render_template, request
import re
import base64
from recognizer import recgonize
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict/", methods=["GET", "POST"])
def predict():
    imgData = request.get_data()
    imgstr = re.search(b"base64,(.*)", imgData).group(1)
    if not os.path.exists("drawn_digits"):
        os.makedirs("drawn_digits")
    with open("drawn_digits/input.png", "wb") as output:
        output.write(base64.b64decode(imgstr))
    predicted_digit = recgonize("drawn_digits/input.png")
    return str(predicted_digit), 200


if __name__ == "__main__":
    app.run()
