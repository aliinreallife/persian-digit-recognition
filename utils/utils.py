import matplotlib.pyplot as plt
from PIL import Image
import re
import base64
from datetime import datetime
import os
import cv2
import numpy as np


def cropped_digit(img: np.ndarray) -> np.ndarray:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the image to get a binary image
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the bounding box for each contour
    bounding_boxes = [cv2.boundingRect(contour) for contour in contours]

    # Find the bounding box with the largest area
    x, y, w, h = max(bounding_boxes, key=lambda item: item[2] * item[3])

    # Crop the digit from the image along with 4 pixels around it
    cropped = img[
        max(0, y - 4) : min(img.shape[0], y + h + 4),
        max(0, x - 4) : min(img.shape[1], x + w + 4),
    ]
    return cropped


def make_square(img: np.ndarray) -> np.ndarray:
    # Determine the number of pixels to add on each side to make the image square
    top = bottom = (max(img.shape[0], img.shape[1]) - img.shape[0]) // 2
    left = right = (max(img.shape[0], img.shape[1]) - img.shape[1]) // 2

    # Add white pixels on each side to make the image square
    squared_image = cv2.copyMakeBorder(
        img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255]
    )
    return squared_image


def dump_image(imgData: bytes, predicted_digit: np.int64) -> str:
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
    return "Image saved successfully!"
