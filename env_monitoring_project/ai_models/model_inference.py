import tensorflow as tf
import numpy as np

# Load the model
MODEL_PATH = "/Users/rishinpandit/Desktop/InternetApplied/Project/EcoGuard-Backend/env_monitoring_project/ai_models/U6_E_1201-F1_0.7134-IOU_0.6555.h5"
# model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_input(input_data):
    """
    Preprocess input data to match the model's expected input format.
    """
    input_array = np.array(input_data).reshape(1, -1)  # Adjust dimensions based on the model's input requirements
    return input_array

def make_prediction(input_data):
    """
    Make a prediction using the AI model.
    """
    preprocessed_data = preprocess_input(input_data)
    prediction = model.predict(preprocessed_data)
    return prediction.tolist()

import os

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
else:
    print(f"Model found at {MODEL_PATH}")

print("Model loaded successfully!")