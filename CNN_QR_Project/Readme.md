# CNN-based QR Code Feature Extractor with Hardware Acceleration

This project implements a CNN-based QR Code feature extractor, where I accelerate the detection of QR code features (such as alignment 
and finder patterns) in hardware. The project is broken down into several Python modules for preprocessing, hardware simulation, 
postprocessing, and QR code decoding.

### Project Structure

Hardware Components
The design is divided into the following key components:

**`Convolution (Conv2D)`**: This module performs the 2D convolution operation to extract edge features from the input image.
    **`ReLU`**: A Rectified Linear Unit (ReLU) activation module that applies non-linear activation to the output of the convolution operation.
    **`Max Pooling`**: A max pooling operation to down-sample the feature map and retain the most significant features.
    **`Top Module`**: The top module integrates the Conv2D, ReLU, and Max Pooling modules to process the image input in a pipeline.

The project includes the following software modules:

- **`preprocess.py`**: Resizes and converts input images to grayscale for further processing.
- **`simulate_hw.py`**: Simulates hardware-accelerated modules like 2D convolution for edge detection.
- **`postprocess.py`**: Handles the visualization of output images and parsing of hardware results.
- **`decode_qr.py`**: Decodes QR codes from images using the `pyzbar` library.

**`Example QR Code`**
- python software/preprocess.py input/test_qr.png

### Requirements

To run this project, I have used the following Python libraries:

- OpenCV (`opencv-python`)
- NumPy (`numpy`)
- Pyzbar (`pyzbar`)
- Matplotlib (`matplotlib`)

I have installed these dependencies by running:

```bash
pip install opencv-python numpy pyzbar matplotlib
