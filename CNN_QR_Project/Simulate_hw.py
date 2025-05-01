
# simulate_hw.py - Simulate RTL

import numpy as np
import time

def simulate_convolution(input_image, kernel):
    # Simulate a basic 3x3 convolution
    image_height, image_width = input_image.shape
    kernel_size = kernel.shape[0]  # Assuming square kernels
    
    output_image = np.zeros((image_height - kernel_size + 1, image_width - kernel_size + 1))

    # Perform convolution operation
    for i in range(output_image.shape[0]):
        for j in range(output_image.shape[1]):
            region = input_image[i:i + kernel_size, j:j + kernel_size]
            output_image[i, j] = np.sum(region * kernel)  # Element-wise multiplication

    return output_image

def simulate_hw_acceleration(input_image, kernel):
    # Simulate hardware-accelerated convolution operation
    start_time = time.time()
    result = simulate_convolution(input_image, kernel)
    end_time = time.time()
    
    # Report performance
    print(f"Hardware simulation completed in {end_time - start_time:.5f} seconds.")
    return result

# Example usage
if __name__ == "__main__":
    # Example input image and kernel (3x3)
    input_image = np.random.rand(128, 128)
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    
    result = simulate_hw_acceleration(input_image, kernel)
    print("Simulation complete.")
