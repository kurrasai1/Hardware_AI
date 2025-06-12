# 📦 CNN-based QR Code Feature Extractor with Hardware Acceleration

This project implements a **CNN-based QR Code feature extractor**, where I accelerate QR code feature detection (such as alignment and finder patterns) using a hardware pipeline. It combines Python-based preprocessing, simulation, and QR decoding with Verilog-based acceleration for core CNN components.

---

## 📁 Project Structure

```
project_root/
├── software/
│   ├── preprocess.py       # Resize + grayscale conversion
│   ├── simulate_hw.py      # Simulate Conv2D operation
│   ├── postprocess.py      # Display and visualize output
│   └── decode_qr.py        # Decode QR from image using pyzbar
├── hardware/
│   ├── conv2d.v            # 3x3 convolution (Sobel kernel)
│   ├── relu_sync.v         # ReLU with synchronous control
│   ├── maxpool.v           # 2x2 max pooling
│   └── top_module.v        # Integrates all three modules
├── sim/
│   ├── test_top_module.py  # Cocotb testbench
│   └── Makefile            # Makefile to run simulation
├── assets/
│   └── qr_test.png         # Sample QR image
└── README.md
```

---

## ⚙️ Hardware Accelerator Pipeline

The hardware pipeline consists of:

1. **Convolution (Conv2D)**  
   - 3x3 kernel (Sobel X) used to extract edge features  
   - Signed multiplier and adder tree logic

2. **ReLU (relu_sync.v)**  
   - Applies non-linearity, suppresses negative outputs

3. **MaxPooling (maxpool.v)**  
   - Down-samples the feature map to retain high activations

4. **Top Module (top_module.v)**  
   - Combines conv2d, relu_sync, and maxpool in a streaming design  
   - Designed to synthesize on FPGA or simulate via Cocotb

---

## 🧪 Simulation & Debugging

All modules are simulated using **Cocotb** with realistic outputs and terminal-style logs:

- Convolution result: `80`
- ReLU result: `80`
- Maxpool result: `8`

Waveform and synthesis reports mirror Vivado and terminal environments (MobaXterm screenshots included for documentation).

---

## 🧰 Software Tools

### 🧾 preprocess.py  
- Takes an input image and resizes to fixed dimension  
- Converts to grayscale for uniform hardware input

### 🧾 simulate_hw.py  
- Simulates 3x3 convolution on input using NumPy  
- Used to benchmark hardware accuracy and latency

### 🧾 postprocess.py  
- Plots final feature map  
- Visualizes output from hardware and verifies against reference

### 🧾 decode_qr.py  
- Uses `pyzbar` to decode QR image before or after processing

---

## 🖼️ Example Run

```bash
# Preprocess QR code
python software/preprocess.py input/test_qr.png

# Simulate Conv2D on CPU
python software/simulate_hw.py

# Postprocess and visualize
python software/postprocess.py

# Decode QR code
python software/decode_qr.py
```

---

## 📦 Requirements

To install all dependencies:

```bash
pip install opencv-python numpy pyzbar matplotlib
```

---

## 🧪 Simulation & Synthesis Tools Used

- [x] Cocotb + Icarus Verilog
- [x] Vivado-style synthesis report
- [x] Post-route timing estimation
- [x] Terminal-style logs (MobaXterm format)
- [x] Waveform simulation (.vcd)
- [x] Visual output of input QR → feature map

---

## 🧾 Sample Output

- `conv_out = 80` (after Sobel X convolution)
- `relu_out = 80`
- `maxpool_out = 8`
- Final feature vector visualized and logged

---

## 👤 Author

**Megha Sai Sumanth Kurra**  
Email: kurrasai@linux.pdx.edu
