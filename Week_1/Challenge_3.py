import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants
R = 1e3   # Resistance in ohms (1 kΩ)
C = 1e-6  # Capacitance in farads (1 µF)
RC = R * C

# Time vector (0 to 0.05 sec)
t = np.linspace(0, 0.05, 1000)

# Input voltage function (step from 0V to 5V)
def V_in(t):
    return 5.0 if t > 0 else 0.0

# Differential equation: dVout/dt = (Vin - Vout) / RC
def rc_circuit(Vout, t):
    return (V_in(t) - Vout) / RC

# Initial condition: capacitor starts discharged
V0 = 0

# Solve ODE
Vout = odeint(rc_circuit, V0, t).flatten()

# Plot result
plt.plot(t, Vout, label='V_out(t)', color='b')
plt.axhline(5, color='r', linestyle='--', label='V_in (Step Input)')
plt.title('RC Circuit: Step Response (Analog ODE Solver)')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.show()

