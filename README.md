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

- Python
- NumPy
- Matplotlib
- TensorFlow
- Keras
- Streamlit
- Kaggle Notebook

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
| Training Accuracy | 98.28% |
| Validation Accuracy | 83.85% |
| Training Loss | 0.0509 |
| Validation Loss | 0.9781 |

## Streamlit Web Application

A Streamlit-based web application was developed to provide an interactive interface for American Sign Language (ASL) Detection.

The application allows users to upload an image of an ASL hand sign and instantly predicts the corresponding alphabet or gesture using the trained Convolutional Neural Network (CNN) model.

## Project Files

- `ASL Detection.ipynb` - Complete notebook containing data preprocessing, CNN model development, training, and evaluation.
- `app.py` - Streamlit web application for ASL hand sign detection.
- `asl_model.keras` - Saved trained CNN model used for prediction.
- `requirements.txt` - Required Python packages for running the application and reproducing the project environment.
- `README.md` - Project documentation.

## Conclusion

An American Sign Language (ASL) Detection system was successfully developed using a Convolutional Neural Network (CNN) to classify hand sign images into 29 different classes, including alphabets (`A-Z`) and special gestures (`SPACE`, `DELETE`, and `NOTHING`).
The model achieved a training accuracy of 98.28% and a validation accuracy of 83.85%, demonstrating strong learning capability and effective feature extraction from image data. 
The developed system can assist in automated sign language recognition applications and serve as a foundation for real-time sign language translation systems.
