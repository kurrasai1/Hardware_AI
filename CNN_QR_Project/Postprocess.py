# postprocess.py – Output Parsing and Visualization

import numpy as np
import matplotlib.pyplot as plt

def visualize_output(image, title="Image Output"):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.show()

def parse_output(output_data):
    # Simulate parsing a hardware result or final image output
    # Here, we assume it's a 2D numpy array (image)
    print(f"Parsed output with shape: {output_data.shape}")
    return output_data

# Example usage
if __name__ == "__main__":
    output_image = np.random.rand(128, 128)  # Example output image from hardware simulation
    parsed_image = parse_output(output_image)
    visualize_output(parsed_image, title="Processed Image Visualization")
