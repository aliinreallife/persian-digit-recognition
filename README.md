![download](https://github.com/aliinreallife/persian-digit-recognition/assets/91134550/e3bdd009-1b20-43a9-8ae9-5cca97581496)

This project is a Persian digit recognition model. It uses Convolutional Neural Network (`CNN`) to recognize handwritten Persian digits. The model is trained on the Hoda dataset, which is a dataset of handwritten Persian digits.

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

### Dataset

The data used in this project comes from the `Hoda Dataset`, the dataset is pre-categorized into training, testing, and evaluation sets.
The dataset includes a total of `102,352 samples`, each of which consists of a 32x32 pixel grayscale image of a handwritten digit and a label indicating the digit's value (0-9).
For more information about the dataset, please visit the [Hoda Dataset website](https://farsiocr.ir/%D9%85%D8%AC%D9%85%D9%88%D8%B9%D9%87-%D8%AF%D8%A7%D8%AF%D9%87/%D9%85%D8%AC%D9%85%D9%88%D8%B9%D9%87-%D8%A7%D8%B1%D9%82%D8%A7%D9%85-%D8%AF%D8%B3%D8%AA%D9%86%D9%88%DB%8C%D8%B3-%D9%87%D8%AF%DB%8C/).


## Evaluation

After training the model, we evaluated its performance on a separate test set that the model had not seen during training. This gives us a sense of how well the model generalizes to new data.

## Confusion Matrix

We first looked at the confusion matrix, which shows the number of correct and incorrect predictions made by the model for each class. The rows of the matrix represent the actual classes, and the columns represent the predicted classes.

Here's the confusion matrix for our model:

![Confusion Matrix](https://github.com/aliinreallife/persian-digit-recognition/assets/91134550/f8aee533-e6ef-43a9-b7ab-55bbf55cff4c)

From the confusion matrix, we can see that the model performs well on most classes, with a high number of correct predictions along the diagonal of the matrix. However, there are some classes where the model makes more mistakes, as indicated by the off-diagonal elements.

## Precision, Recall, and F1 Score

We also computed the precision, recall, and F1 score for each class. These metrics give us more information about the model's performance.

- `Precision` is the proportion of true positive predictions (i.e., the number of correctly predicted instances of a class) out of all positive predictions made by the model.
- `Recall` is the proportion of true positive predictions out of all actual instances of a class.
- `F1 score` is the harmonic mean of precision and recall, and it gives us a single metric that balances the two.

Here are the precision, recall, and F1 score for our model:

|           |     0 |     1 |     2 |     3 |     4 |     5 |     6 |     7 |     8 |     9 |   accuracy |   macro avg |   weighted avg |
|:----------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|-----------:|------------:|---------------:|
| precision | 0.998 | 0.996 | 0.994 | 0.988 | 0.994 | 0.993 | 0.995 | 1     | 0.998 | 0.997 |      0.995 |       0.995 |          0.995 |
| recall    | 0.996 | 0.998 | 0.99  | 0.992 | 0.996 | 0.998 | 0.996 | 0.996 | 1     | 0.993 |      0.995 |       0.995 |          0.995 |
| f1-score  | 0.997 | 0.997 | 0.992 | 0.99  | 0.995 | 0.995 | 0.995 | 0.998 | 0.999 | 0.995 |      0.995 |       0.995 |          0.995 |

From these metrics, we can see that the model performs well on most classes, with high precision, recall, and F1 scores. However, there are some classes where the model's performance is lower, indicating areas where the model could be improved.

## Conclusion

Overall, our model performs well on the task of recognizing Persian digits. However, there are some areas where the model could be improved, as indicated by the evaluation metrics. Future work could focus on improving the model's performance on these more challenging classes.

## Module Origin

The module `hoda_dataset_reader` is sourced from [HodaDatasetReader](https://github.com/amir-saniyan/HodaDatasetReader).

## License
This project is `MIT` Licensed.
