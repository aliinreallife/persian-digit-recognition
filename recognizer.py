import cv2
from utils.utils import cropped_digit, dump_image, make_square
from tensorflow.keras.models import load_model  # type: ignore
from PIL import Image
import numpy as np

model = load_model("models/PDRM.keras")

def recgonize(image_path: str) -> int:
    """
    This function uses a pre-trained model ("PDRM.keras") to recgonize the digit present in the image.
    The input image is preprocessed and then passed to the model for recgonition.
    The input should be an image with a white background and a black digit.

    Args:
        image_path (str): The path to the image file that needs to be recognized.

    Returns:
        int: The digit recgonized by the model.
    """
    image = Image.open(image_path).convert("L")
    image = np.array(image)
    cropped_image = cropped_digit(image)
    squared_image = make_square(cropped_image)
    image = squared_image
    image = cv2.resize(image, (32, 32))
    image = image.reshape(1, 32, 32, 1)
    image = cv2.bitwise_not(image)
    image = image / 255.0
    prediction = model.predict([image])[0]
    predicted_digit = int(np.argmax(prediction))
    dump_image(squared_image, predicted_digit)
    return predicted_digit
