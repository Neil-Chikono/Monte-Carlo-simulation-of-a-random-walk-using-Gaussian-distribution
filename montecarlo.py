import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
particles = 10000
steps = 1000

# Generate random directions - Gaussian-distributed dx and dy
angles = np.random.normal(0, 2*np.pi, (particles, steps))

# Calculate movement
dx = np.cos(angles)
dy = np.sin(angles)

# Accumulate positions
x = np.cumsum(dx, axis=1)
y = np.cumsum(dy, axis=1)

# Visualise the trajectories
plt.figure(figsize=(8, 8))

for i in range(30):
    plt.plot(x[i], y[i], alpha=0.3)

# Visualise final positions
plt.scatter(x[:, -1], y[:, -1], s=5)

plt.scatter(0, 0, color="red", label="Origin")
plt.axis("equal")
plt.legend()
plt.title("Monte Carlo Random Walk")
plt.show()
