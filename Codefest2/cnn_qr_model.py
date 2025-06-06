import tensorflow as tf
from tensorflow.keras import layers, models

def build_qr_feature_extractor(input_shape=(128, 128, 1), num_features=64):
    model = models.Sequential()

    # Convolutional layers for feature extraction
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.GlobalAveragePooling2D())

    # Dense layer to extract feature vector
    model.add(layers.Dense(num_features, activation='relu'))

    return model

if __name__ == "__main__":
    model = build_qr_feature_extractor()
    model.summary()
