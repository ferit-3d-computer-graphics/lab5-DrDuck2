import k3d
import numpy as np

grid_size = 50
x = np.linspace(-1, 1, grid_size)
y = np.linspace(-1, 1, grid_size)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

vertices = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T.astype(np.float32)

indices = []
for i in range(grid_size-1):
    for j in range(grid_size-1):
        idx = i * grid_size + j
        indices.append([idx, idx+1, idx+grid_size])
        indices.append([idx+1, idx+grid_size+1, idx+grid_size])
indices = np.array(indices, dtype=np.uint32)

z_min, z_max = Z.min(), Z.max()
z_norm = (Z.ravel() - z_min) / (z_max - z_min)
colors = (z_norm * 0xFFFF00 + (1 - z_norm) * 0x0000FF).astype(np.uint32)

mesh_gradient = k3d.mesh(
    vertices, indices,
    colors=colors,
    wireframe=False,
    flat_shading=False
)

mesh_flat = k3d.mesh(
    vertices, indices,
    color=0x00FF00, 
    wireframe=False,
    flat_shading=False
)
mesh_flat.transform.translation = [2.5, 0, 0]  

plot = k3d.plot()
plot += mesh_gradient
plot += mesh_flat
plot.display()