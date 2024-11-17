import tensorflow as tf
import numpy as np
import os
from .preprocess import preprocess_image
from pathlib import Path

# Path to the trained model
MODEL_PATH = Path(__file__).resolve().parent / "trained_model/model.h5"


class AIModel:
    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}")
        self.model = tf.keras.models.load_model(MODEL_PATH)
        print("AI Model loaded successfully.")

    def predict_deforestation(self, image_path):
        """
        Predict deforestation using a pre-trained model.

        Args:
            image_path (str): Path to the satellite image.

        Returns:
            np.ndarray: Model predictions as a mask.
        """
        image = preprocess_image(image_path)
        prediction = self.model.predict(image[np.newaxis, ...])
        return prediction.squeeze()


# Example usage
if __name__ == "__main__":
    model = AIModel()
    mask = model.predict_deforestation("path/to/satellite_image.tif")
    print("Prediction completed.")
