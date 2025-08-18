import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl

# Grid
x = np.linspace(1, 14, 14)
y = np.linspace(1, 14, 14)
X, Y = np.meshgrid(x, y)

# Wave parameters
kx = 2 * np.pi / (x.max() - x.min())
ky = 2 * np.pi / (y.max() - y.min())
omega = 3*np.pi/5   # frequency (for animation, if wanted)

for idx, phase in enumerate(np.linspace(0, 2*np.pi, 90)):

    # Define scalar wave
    wave = np.sin(kx*X + ky*Y + phase) + 2

    # Define vector field: gradient of wave (direction of propagation)
    U = kx * wave
    V = ky * wave

    cmap = mpl.colormaps['magma']
    colors = cmap(np.linspace(0, 0.7, 4))

    # Example: split into 3 subsets
    mask1 = ((X.astype(int) % 3 == 0) & (Y.astype(int) % 3 == 0)) # Sensor Position
    mask2 = ((X.astype(int) < 3) | (Y.astype(int) < 3)) | ((X.astype(int) > 12) | (Y.astype(int) > 12))  # Extrapolaion
    mask3 = ((X.astype(int) == 11) & (Y.astype(int) == 10)) # Measurement Location
    mask4 = ~mask1 & ~mask2 & ~mask3      # Interpolation

    plt.figure(figsize=(6,6))

    # Subset 1
    plt.quiver(X[mask1], Y[mask1], U[mask1], V[mask1], color=colors[0], label="Sensor Position")

    # Subset 2
    plt.quiver(X[mask2], Y[mask2], U[mask2], V[mask2], color=colors[3], label="Extrapolation")

    # Subset 3
    plt.quiver(X[mask4], Y[mask4], U[mask4], V[mask4], color=colors[2], label="Interpolation")

    # Subset 3
    plt.quiver(X[mask3], Y[mask3], U[mask3], V[mask3], color="red", label="Measurement Location")

    plt.gca().set_facecolor("#e3e3e3")
    plt.grid(True)
    plt.xticks(np.arange(1, 15, 1))
    plt.yticks(np.arange(1, 15, 1))
    plt.legend()
    plt.title("Vector Field for Wind Measurement")
    plt.axis("equal")
    #plt.show()
    plt.savefig(f"plots/wind_field_{idx}.png")
    plt.close()