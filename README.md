![download](https://github.com/aliinreallife/persian-digit-recognition/assets/91134550/e3bdd009-1b20-43a9-8ae9-5cca97581496)

## Description

This project is a Persian digit recognition model. It uses Convolutional Neural Network (CNN) to recognize handwritten Persian digits. The model is trained on the Hoda dataset, which is a dataset of handwritten Persian digits.

## Live Demo

You can access a live demo of the model at [this link](https://welcome-unlikely-minnow.ngrok-free.app/).

## Usage

To train the model, run the train.ipynb Jupyter notebook. This will train the CNN on the Hoda dataset and save the trained model to disk.

After training the model, you can use it to recognize Persian digits. The model takes a `32x32` grayscale image of a handwritten digit as input and outputs the recognized digit.

### Required Libraries
- TensorFlow: For creating and training the Model.
- Hoda Dataset Reader: For reading the Hoda dataset.
- Matplotlib: For plotting training progress.
- NumPy: For numerical operations.
- OpenCV: For image processing.
- PIL: For image processing.

## Module Origin

The module `hoda_dataset_reader` is sourced from [HodaDatasetReader](https://github.com/amir-saniyan/HodaDatasetReader).

## License
This project is MIT Licensed.
