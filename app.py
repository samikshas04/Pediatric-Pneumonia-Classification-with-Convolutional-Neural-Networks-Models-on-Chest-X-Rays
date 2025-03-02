import streamlit as st
#import os
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import cv2
from PIL import Image

import tensorflow as tf
from tensorflow import keras

# Load the saved model
loaded_model = keras.models.load_model(r'D:\sem 8\Pneumonia-Detection-using-CNN-main\Pneumonia-Detection-using-CNN-main\model\Pneumonia_model.h5')

# Streamlit UI
st.title("Pneumonia Detection App")# Streamlit UI




# Sidebar for file upload
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Model prediction button
    if st.button("Predict"):
        # Ensure the shape matches the expected input shape of your model
        input_image_resized = cv2.resize(np.array(image), (128, 128))

        # Normalize the pixel values
        input_image_normalized = input_image_resized / 255

        if len(input_image_normalized.shape) == 2:
            input_image_normalized = np.stack((input_image_normalized,) * 3, axis=-1)

        # Reshape for model prediction
        input_image_reshaped = np.reshape(input_image_normalized, [1, 128, 128, 3])

        # Make predictions
        input_prediction = loaded_model.predict(input_image_reshaped)

        # Get the predicted label
        input_pred_label = np.argmax(input_prediction)

        # Display the predicted label
        if input_pred_label == 1:
            st.error('Pneumonia detected!')
        else:
            st.success('No Pneumonia detected.')
