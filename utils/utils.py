import matplotlib.pyplot as plt
from datetime import datetime
import os
import cv2
import numpy as np



def cropped_digit(image: np.ndarray) -> np.ndarray:
    # Find contours in the binary image
    contours, _ = cv2.findContours(
        cv2.bitwise_not(image), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Get the bounding box for each contour
    bounding_boxes = [cv2.boundingRect(contour) for contour in contours]

    # Find the bounding box with the largest area
    x, y, w, h = max(bounding_boxes, key=lambda item: item[2] * item[3])

    # Crop the digit from the image along with padding (4 pixels) around it
    padding = 4
    cropped = image[
        max(0, y - padding) : min(image.shape[0], y + h + padding),
        max(0, x - padding) : min(image.shape[1], x + w + padding),
    ]
    return cropped


def make_square(image: np.ndarray) -> np.ndarray:
    # Determine the number of pixels to add on each side to make the image square
    top = bottom = (max(image.shape[0], image.shape[1]) - image.shape[0]) // 2
    left = right = (max(image.shape[0], image.shape[1]) - image.shape[1]) // 2

    # Add white pixels on each side to make the image square
    squared_image = cv2.copyMakeBorder(
        image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255]
    )
    return squared_image


def dump_image(
    image: np.ndarray,
    predicted_digit: int,
    resize_flag: bool = True,
    reversed_flag: bool = True,
) -> str:
    parent_dir = "drawn_digits/"
    predicted_dir = parent_dir + str(predicted_digit)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    if not os.path.exists(predicted_dir):
        os.makedirs(predicted_dir)
    # Generate a unique filename using the current date and time
    filename = datetime.now().strftime("%Y%m%d%H%M%S%f") + ".jpg"
    full_path = os.path.join(predicted_dir, filename)
    if resize_flag:
        image = cv2.resize(image, (32, 32))
    if reversed_flag:
        image = cv2.bitwise_not(image)
    cv2.imwrite(full_path, image)
    return full_path


def resize_image(image: np.ndarray, width: int = 32, hight: int = 32) -> np.ndarray:
    return cv2.resize(image, (width, hight))


def plot_image(image: np.ndarray, title: str = "image") -> None:
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.axis("off")
    plt.show()
