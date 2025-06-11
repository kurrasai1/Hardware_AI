# 🧠 Memristor Simulation using Biolek Model

This project simulates a memristor device and visualizes the I-V characteristic known as the **pinched hysteresis loop** using a simplified Biolek memristor model. This is in response to Challenge #28 from the *ECE 410/510 - Spring 2025* weekly challenge series.

---

## 🚀 Challenge Description

> **Challenge #28**: Model and simulate a memristor.  
> Memristors are important circuit elements for neuromorphic computing as they can emulate a synapse. Their resistive value represents the synaptic weight, which can be updated using mechanisms like Spike Timing-Dependent Plasticity (STDP).  
>  
> **Tasks**:
> 1. Download or implement a memristor model (e.g., Biolek model).
> 2. Visualize the characteristic pinched hysteresis loop in the I-V curve.
> 3. Document the results.

---

## 🧪 Simulation Details

- **Language**: Python 3
- **Model**: Biolek Memristor (simplified)
- **Input**: Sinusoidal voltage
- **Output**: I-V curve

### 🔧 Model Parameters

| Parameter | Description                  | Value         |
|-----------|------------------------------|---------------|
| `Ron`     | ON resistance                | 100 Ω         |
| `Roff`    | OFF resistance               | 16,000 Ω      |
| `D`       | Width of memristor           | 10 nm         |
| `μv`      | Ion mobility                 | 1e-14 m²/V·s  |
| `dt`      | Time step                    | 0.0001 s      |
| `T`       | Simulation duration          | 2 seconds     |

---

## 📈 Output

The simulation generates the following I-V curve demonstrating the **pinched hysteresis loop**, which is the signature behavior of a memristor:

in this file (iv_curve.png)

---

## 📂 Files Included

- `memristor_simulation.py` – Python code to simulate the memristor and generate the I-V curve.
- `iv_curve.png` – Output image showing the pinched hysteresis loop.
- `README.md` – Documentation for this project.

---

## ▶️ How did I Run

1. Cloned this repository.
2. Making sure I have Python 3 and the following packages installed:

```bash
pip install numpy matplotlib
