import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split

# Load your QR code dataset (for example, QR code images and their labels)
# This part assumes you have a dataset of QR codes. If you don't have a dataset, 
# you can use OpenCV or any tool to generate QR codes programmaticaly.

def load_dataset(data_dir):
    images = []
    labels = []
    
    # For simplicity, assume images are stored in a folder named data_dir
    for filename in os.listdir(data_dir):
        if filename.endswith(".png"):  # Assuming QR code images are in .png format
            img_path = os.path.join(data_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (64, 64))  # Resize the image to a fixed size
            images.append(img)
            
            # For simplicity, assuming labels are encoded in the filename
            label = int(filename.split("_")[0])  # Example: "0_qrcode.png", "1_qrcode.png"
            labels.append(label)
    
    # Convert to numpy arrays and normalize pixel values
    images = np.array(images) / 255.0  # Normalize to [0, 1]
    labels = np.array(labels)
    return images, labels

# Load dataset (assuming you have a 'data' folder with images)
X, y = load_dataset("path_to_your_qr_code_dataset")

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Add channel dimension (for grayscale images)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# Build the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')  # Assuming 10 classes for QR code patterns
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save the trained model
model.save('models/keras_model.h5')

print("Model saved as 'models/keras_model.h5'")
