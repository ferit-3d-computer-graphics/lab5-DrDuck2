import k3d
import numpy as np

# 1. Create procedural terrain mesh
grid_size = 40
x = np.linspace(-3, 3, grid_size)
y = np.linspace(-3, 3, grid_size)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# Create vertices and faces
vertices = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T.astype(np.float32)

indices = []
for i in range(grid_size-1):
    for j in range(grid_size-1):
        idx = i * grid_size + j
        indices.append([idx, idx+1, idx+grid_size])
        indices.append([idx+1, idx+grid_size+1, idx+grid_size])
indices = np.array(indices, dtype=np.uint32)

# 2. Color by elevation
z_min, z_max = Z.min(), Z.max()
z_norm = (Z.ravel() - z_min) / (z_max - z_min)
colors = (z_norm * 0xFFFFFF).astype(np.uint32)

# 3. Find peak and valley locations
peak_idx = np.argmax(Z.ravel())
valley_idx = np.argmin(Z.ravel())
peak_pos = vertices[peak_idx] + [0, 0, 0.2]  # Offset above surface
valley_pos = vertices[valley_idx] + [0, 0, 0.2]

# 4. Create plot with labels
plot = k3d.plot()

# Add terrain mesh
plot += k3d.mesh(vertices, indices, colors=colors, wireframe=False)

# Add text labels
plot += k3d.text("PEAK", position=peak_pos.tolist(), color=0xff0000, scale=0.3)
plot += k3d.text("VALLEY", position=valley_pos.tolist(), color=0x0000ff, scale=0.3)

# Add colorbar legend
plot += k3d.text2d(f"Elevation\n{z_min:.2f}", position=[0.05, 0.7], size=1.0, color=0x0000ff)
plot += k3d.text2d(f"Elevation\n{z_max:.2f}", position=[0.05, 0.8], size=1.0, color=0xff0000)

plot.display()
