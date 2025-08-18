import numpy as np
import matplotlib.pyplot as plt

# Grid
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Vector field (rotation around origin)
U = -Y
V = X

# Example: split into 3 subsets
mask1 = X < -0.5        # left side
mask2 = (X >= -0.5) & (X <= 0.5)   # middle
mask3 = X > 0.5         # right side

plt.figure(figsize=(6,6))

# Subset 1
plt.quiver(X[mask1], Y[mask1], U[mask1], V[mask1], color="red", label="Left")

# Subset 2
plt.quiver(X[mask2], Y[mask2], U[mask2], V[mask2], color="green", label="Middle")

# Subset 3
plt.quiver(X[mask3], Y[mask3], U[mask3], V[mask3], color="blue", label="Right")

plt.legend()
plt.title("Vector Field with 3 Subsets")
plt.axis("equal")
#plt.show()
plt.savefig("test.png")