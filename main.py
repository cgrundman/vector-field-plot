import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl

# Grid
x = np.linspace(2, 14, 13)
y = np.linspace(2, 14, 13)
X, Y = np.meshgrid(x, y)

# Wave parameters
kx = 2 * np.pi / (x.max() - x.min())
ky = 2 * np.pi / (y.max() - y.min())

for idx, phase in enumerate(np.linspace(0, 2*np.pi, 90)):

    # Define scalar wave
    wave = np.sin(kx*X + ky*Y + phase) + 2

    # Define vector field: gradient of wave (direction of propagation)
    U = kx * wave
    V = ky * wave

    cmap = mpl.colormaps['magma']
    colors = cmap(np.linspace(0, 0.7, 4))

    # Example: split into 3 subsets
    mask1 = ((X.astype(int) % 4 == 0) & (Y.astype(int) % 4 == 0)) # Sensor Position
    mask2 = ((X.astype(int) < 4) | (Y.astype(int) < 4)) | ((X.astype(int) > 12) | (Y.astype(int) > 12))  # Extrapolaion
    mask3 = ((X.astype(int) == 11) & (Y.astype(int) == 10)) # Measurement Location
    mask4 = ~mask1 & ~mask2 & ~mask3      # Interpolation

    plt.figure(figsize=(6,6))

    # Subset 1
    plt.quiver(
        X[mask1], Y[mask1], U[mask1], V[mask1], 
        color=colors[0], label="Sensorposition"
    )

    # Subset 2
    plt.quiver(
        X[mask2], Y[mask2], U[mask2], V[mask2], 
        color=colors[3], label="Extrapolation"
    )

    # Subset 3
    plt.quiver(
        X[mask4], Y[mask4], U[mask4], V[mask4], 
        color=colors[2], label="Interpolation"
    )

    # Subset 3
    plt.plot(
        X[mask3], Y[mask3], linewidth=0, marker='.', 
        markersize=30, color="red", label="Messpunkt"
    )

    ax = plt.gca()

    ax.set_facecolor("#e3e3e3")
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.grid(True)
    plt.xticks(np.arange(1, 16, 1))
    plt.yticks(np.arange(1, 16, 1))
    plt.ylabel("Bullshit", visible=False)
    plt.legend(loc="lower right", fontsize=16)
    plt.title("Vektorfeld zur Windmessung", fontsize=20)
    plt.axis("equal")
    plt.tight_layout()
    #plt.show()
    plt.savefig(f"figures/wind_field_{idx}.png")
    plt.close()