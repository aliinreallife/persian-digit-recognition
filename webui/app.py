from flask import Flask, render_template, request
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image
import re
import base64
import numpy as np
from datetime import datetime
import os

app = Flask(__name__)
model = load_model("models/PDRM.keras")


def saveImage(imgData, predicted_digit):
    parent_dir = "images_log/"
    predicted_dir = parent_dir + str(predicted_digit)
    imgstr = re.search(b"base64,(.*)", imgData).group(1)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    if not os.path.exists(predicted_dir):
        os.makedirs(predicted_dir)
    # Generate a unique filename using the current date and time
    filename = datetime.now().strftime("%Y%m%d%H%M%S%f") + ".png"
    with open(os.path.join(predicted_dir, filename), "wb") as output:
        output.write(base64.b64decode(imgstr))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict/", methods=["GET", "POST"])
def predict():
    imgData = request.get_data()
    imgstr = re.search(b"base64,(.*)", imgData).group(1)
    with open("images_log/output.png", "wb") as output:
        output.write(base64.b64decode(imgstr))
    img = Image.open("images_log/output.png").convert("L")
    img = img.resize((32, 32))
    img = np.array(img)
    img = img.reshape(1, 32, 32, 1)
    img = img / 255.0
    img = 1 - img
    prediction = model.predict([img])[0]
    predicted_digit = np.argmax(prediction)
    saveImage(imgData, predicted_digit)
    return str(predicted_digit), 200


if __name__ == "__main__":
    app.run()
