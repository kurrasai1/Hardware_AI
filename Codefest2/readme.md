# Challenge 9 - AI Hardware Accelerator Exploration

## 🎯 Project Title
**CNN-Based Feature Extractor for Real-Time QR Code Processing**

## 📜 Description
This project explores hardware acceleration of CNN-based feature extraction used in QR code recognition. The system offloads convolution, activation, and dense layer computations to a custom-designed chiplet running on an FPGA. This reduces latency and enables real-time QR decoding on edge devices.

## 📁 Contents
- `cnn_qr_model.py`: Python-based CNN feature extractor
- `profile_report.txt`: Profiling logs from cProfile, memory_profiler
- `graphs/`: Includes call graph (Doxygen) and dataflow graph (NetworkX)
- `report.pdf`: Detailed summary of analysis and system design
- `architecture_diagram.png`: Block diagram showing software-hardware interaction

## 🔧 Tools Used
- TensorFlow/Keras for CNN model
- Python profiling tools: cProfile, py-spy, memory_profiler
- Doxygen + Graphviz for call graphs
- AST + NetworkX for custom dataflow analysis
- Vivado + Verilog + FPGA board for hardware acceleration prototype

## ✅ Key Insights
- CNN convolution layers account for majority of inference time.
- MAC operations and ReLU are highly parallelizable and ideal for custom hardware.
- FPGA-based accelerators can reduce inference latency and energy use compared to CPU/GPU.

## 🚀 Goals
- Train a CNN that extracts robust features from distorted or rotated QR codes.
- Develop a Verilog-based accelerator for CNN inference and run it on FPGA.
- Establish a communication link between Python software and FPGA hardware.
- Achieve a minimum 3× speedup over CPU inference time with similar accuracy.

## 🧠 Author
**Megha Sai Sumanth Kurra**  
MS ECE, Portland State University

## 📅 Course
ECE 410/510 Spring 2025 - Codefest (Prof. Christof Teuscher)
