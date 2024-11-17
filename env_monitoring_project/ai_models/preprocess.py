import numpy as np
import rasterio
from rasterio.enums import Resampling


def preprocess_image(image_path, target_size=(256, 256)):
    """
    Preprocess the satellite image for the AI model.

    Args:
        image_path (str): Path to the satellite image (GeoTIFF).
        target_size (tuple): Target size for resizing (width, height).

    Returns:
        np.ndarray: Preprocessed image.
    """
    with rasterio.open(image_path) as src:
        # Read the image and resample to target size
        data = src.read(
            out_shape=(
                src.count,
                target_size[1],
                target_size[0]
            ),
            resampling=Resampling.bilinear
        )
        # Normalize the image
        data = data.astype(np.float32) / 255.0
        return np.transpose(data, (1, 2, 0))  # Channels last


# Example usage
if __name__ == "__main__":
    image = preprocess_image("/Users/rishinpandit/Desktop/InternetApplied/Project/EcoGuard-Backend"
                             "/env_monitoring_project/ai_models/downloaded_image.tif")
    print(f"Preprocessed image shape: {image.shape}")
