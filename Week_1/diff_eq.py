import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation
def model(y, t):
    return -2 * y

# Initial condition
y0 = 1

# Time points
t = np.linspace(0, 5, 100)

# Solve ODE
y = odeint(model, y0, t)

# Plot
plt.plot(t, y)
plt.title("Solution of dy/dt = -2y")
plt.xlabel("Time")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
