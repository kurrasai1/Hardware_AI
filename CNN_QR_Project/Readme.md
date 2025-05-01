# CNN-based QR Code Feature Extractor with Hardware Acceleration

This project implements a CNN-based QR Code feature extractor, where I accelerate the detection of QR code features (such as alignment 
and finder patterns) in hardware. The project is broken down into several Python modules for preprocessing, hardware simulation, 
postprocessing, and QR code decoding.

### Project Structure

The project includes the following modules:

- **`preprocess.py`**: Resizes and converts input images to grayscale for further processing.
- **`simulate_hw.py`**: Simulates hardware-accelerated modules like 2D convolution for edge detection.
- **`postprocess.py`**: Handles the visualization of output images and parsing of hardware results.
- **`decode_qr.py`**: Decodes QR codes from images using the `pyzbar` library.

### Requirements

To run this project, I have used the following Python libraries:

- OpenCV (`opencv-python`)
- NumPy (`numpy`)
- Pyzbar (`pyzbar`)
- Matplotlib (`matplotlib`)

I have installed these dependencies by running:

```bash
pip install opencv-python numpy pyzbar matplotlib
