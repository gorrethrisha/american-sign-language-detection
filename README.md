# American Sign Language (ASL) Detection

## Project Overview

This project develops a deep learning-based American Sign Language (ASL) Detection system to recognize hand sign images and predict the corresponding alphabet or gesture represented by the sign.

## Objective

The primary objective of this project is to develop a Convolutional Neural Network (CNN) model capable of accurately classifying American Sign Language hand gestures while learning meaningful visual patterns from image data.

## Dataset Information

* Total Images: **87,000**
* Total Classes: **29**

### Classes Used for Training

* `A - Z` → Alphabet Classes
* `SPACE`
* `DELETE`
* `NOTHING`

## Tech Stack

* Python
* NumPy
* Matplotlib
* TensorFlow
* Keras
* Kaggle Notebook

## Methodology

The following steps were followed during the development of the project:

1. Dataset Overview
2. Data Preprocessing
3. Image Visualization
4. CNN Model Building
5. Model Training
6. Model Evaluation
7. Training History Visualization
8. Prediction 

## Model Performance

| Metric | Value |
| ------- | ----- |
| Training Accuracy | 98.82% |
| Validation Accuracy | 82.30% |
| Training Loss | 0.0368 |
| Validation Loss | 1.1678 |

## Conclusion

An American Sign Language (ASL) Detection system was successfully developed using a Convolutional Neural Network (CNN) to classify hand sign images into 29 different classes, including alphabets (`A-Z`) and special gestures (`SPACE`, `DELETE`, and `NOTHING`).
The model achieved a training accuracy of 98.82% and a validation accuracy of 82.30%, demonstrating strong learning capability and effective feature extraction from image data. 
The developed system can assist in automated sign language recognition applications and serve as a foundation for real-time sign language translation systems.
