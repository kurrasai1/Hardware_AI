# 🧊 GPU-Accelerated Q-Learning on FrozenLake (OpenAI Gym)

This project explores the performance benefits of using **GPU acceleration (via CuPy)** to speed up a Q-learning agent solving the FrozenLake environment.

---

## 📌 Challenge Description

This project is part of **Challenge #11** in a weekly AI/ML coding series:

> **Goal**: Optimize a Q-learning implementation of FrozenLake using GPU acceleration.  
> **Steps**:
> 1. Modify the original CPU-based Q-learning code to run on GPU using CuPy.
> 2. Benchmark and compare performance between CPU and GPU versions.
> 3. Report findings.

---

## 💡 What is Q-Learning?

Q-learning is a reinforcement learning algorithm used to learn an optimal policy by iteratively updating a Q-table using the Bellman equation:

\[
Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \left[r + \gamma \cdot \max_{a'} Q(s', a') - Q(s, a)\right]
\]

Where:
- \(s\): current state
- \(a\): action
- \(r\): reward
- \(s'\): next state
- \(\alpha\): learning rate
- \(\gamma\): discount factor

---

## 🚀 GPU Acceleration with CuPy

[**CuPy**] is a GPU-backed drop-in replacement for NumPy. By using CuPy, we can:
- Move the Q-table to GPU memory.
- Perform matrix operations (e.g., `argmax`, `max`, arithmetic) on GPU.
- Achieve **significant speedups** in training time for large numbers of episodes.

---

## 🧪 Benchmark Setup

| Parameter     | Value          |
|---------------|----------------|
| Environment   | `FrozenLake-v1` |
| Episodes      | 10,000         |
| Algorithm     | Q-learning     |
| Exploration   | ε = 0.1        |
| Learning Rate | α = 0.8        |
| Discount      | γ = 0.95       |

---

## ⏱️ Results

| Version       | Time (s) | Speedup |
|---------------|----------|---------|
| CPU (NumPy)   | 4.56     | —       |
| GPU (CuPy)    | 1.28     | 3.56×   |

> Note: Actual results may vary based on your hardware and GPU.

---

## 📦 Requirements

- Python 3.7+
- OpenAI Gym
- CuPy (for GPU version)
- NumPy
