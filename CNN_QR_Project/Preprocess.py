# preprocess.py - Image Resize and Grayscale Conversion

import cv2
import numpy as np

def preprocess_image(image_path, target_size=(128, 128)):
    # Read image
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Image at path {image_path} cannot be read.")
    
    # Resize image to target size
    resized_image = cv2.resize(image, target_size)
    
    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    
    return grayscale_image

# Example usage
if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"
    processed_image = preprocess_image(image_path)
    cv2.imwrite("processed_image.jpg", processed_image)  # Save the processed image
    print("Image preprocessed and saved.")
