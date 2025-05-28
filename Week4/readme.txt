# CUDA SAXPY Benchmarking (Challenge #13 - ECE 410/510)

This project benchmarks the performance of a CUDA SAXPY (Single-Precision A·X Plus Y) kernel for increasing input sizes. The objective is to measure how GPU execution time changes as the problem size increases and visualize the results.

## 🚀 Challenge Overview

**Goal**: Benchmark SAXPY for varying input sizes using CUDA and visualize the performance.

**Input sizes (N)**: From `2^15` to `2^25`

**Tasks**:
- Modify a CUDA SAXPY implementation
- Time both memory transfer and kernel execution separately
- Plot performance results

---

## 🧰 Requirements

- CUDA-capable GPU (or use [Google Colab](https://colab.research.google.com))
- CUDA Toolkit (10.0+)
- Python 3.x with Matplotlib (for plotting)
- C++ compiler with `nvcc` support

---

## 📁 File Structure

├── saxpy.cu # CUDA implementation of SAXPY with timing
├── results.txt # Output file containing execution times
├── plot_results.py # Python script to generate bar chart
└── README.md # Project documentation

Observations

Small N: Execution time is dominated by kernel launch and memory overhead.
Larger N: GPU acceleration benefits become more visible.
Trend: Execution time grows roughly linearly with input size beyond a threshold.
You may notice irregularities at very large sizes due to:

GPU memory constraints
Memory bandwidth bottlenecks
Increased kernel scheduling overhead
