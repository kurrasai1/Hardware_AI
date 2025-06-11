import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
dt = 1e-4      # time step
t_max = 2      # total time in seconds
t = np.arange(0, t_max, dt)

# Memristor parameters (Biolek-like model)
Ron = 100       # ON resistance in ohms
Roff = 16000    # OFF resistance in ohms
D = 10e-9       # width of the device
mu_v = 1e-14    # mobility
V = 1.0 * np.sin(2 * np.pi * 1 * t)  # input voltage waveform

# Initialization
w = np.zeros(len(t))
w[0] = D / 2  # start at midpoint
i = np.zeros(len(t))
R = np.zeros(len(t))

# Simulate memristor dynamics
for k in range(1, len(t)):
    R[k] = Ron * (w[k-1]/D) + Roff * (1 - w[k-1]/D)
    i[k] = V[k] / R[k]
    
    # Update state
    dw = mu_v * Ron * i[k] * dt
    w[k] = w[k-1] + dw
    
    # Bound w
    if w[k] > D:
        w[k] = D
    elif w[k] < 0:
        w[k] = 0

# Plot I-V characteristic
plt.figure(figsize=(8, 6))
plt.plot(V, i, color='blue')
plt.title("Memristor I-V Curve (Pinched Hysteresis Loop)")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.grid(True)
plt.savefig("iv_curve.png", dpi=300)
plt.show()
