# Challenge #4 - ECE 410/510 Spring 2025

This repository contains the solution to Challenge #4 of the Spring 2025 Codefest.

## 🧠 Project Title:
**LLM-Assisted Silicon Brain Design: Verilog Implementation of LIF Neuron Arrays**

## 📜 Summary:
This project replicates the methodology of the paper _"Designing Silicon Brains using LLM"_, leveraging ChatGPT to design HDL code for a Leaky Integrate-and-Fire (LIF) neuron array.

## 📁 Contents:
- `lif_array.v`: Verilog code for the LIF neuron array
- `tb.v`: Testbench for simulating the neuron array
- `lif_array.gds`: (optional) GDSII file from OpenLane flow
- `Challenge4_Report_ECE410_510.pdf`: Detailed report of the challenge
- `Challenge4_Report_ECE410_510.tex`: LaTeX source of the report

## 🔧 Tools Used:
- ChatGPT (for HDL generation)
- Icarus Verilog (for simulation)
- OpenLane (for GDS generation)
- GTKWave (for waveform visualization)

## 🧪 How to Run:
```bash
iverilog -o sim tb.v lif_array.v
vvp sim
```

## 📊 Improvements Explored:
- ReLU neuron design
- Hodgkin–Huxley neuron model
- Interface optimizations and ASIC flow

## 👨‍💻 Author:
**Megha Sai Sumanth Kurra**  
Master's Student, Portland State University

---

```
This project is part of ECE 410/510 Spring 2025 Codefest, guided by Prof. Christof Teuscher.
```
