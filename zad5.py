import k3d
import numpy as np

def create_cone(radius=0.1, height=0.3, segments=32):
    theta = np.linspace(0, 2*np.pi, segments)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.zeros_like(x)
    base_vertices = np.vstack([x, y, z]).T
    tip_vertex = np.array([[0, 0, height]])
    vertices = np.vstack([base_vertices, tip_vertex]).astype(np.float32)
    
    faces = []
    tip_index = len(vertices) - 1
    for i in range(segments):
        next_i = (i + 1) % segments
        faces.append([i, next_i, tip_index])
    
    return vertices, np.array(faces, dtype=np.uint32)

def rotation_x_matrix(degrees):
    theta = np.radians(degrees)
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)

def rotation_y_matrix(degrees):
    theta = np.radians(degrees)
    return np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)

def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ], dtype=np.float32)

plot = k3d.plot(background_color=0x000000)
axis_length = 1.5

plot += k3d.line([[0,0,0], [axis_length,0,0]], color=0xFF0000, width=0.05)
plot += k3d.line([[0,0,0], [0,axis_length,0]], color=0x00FF00, width=0.05)
plot += k3d.line([[0,0,0], [0,0,axis_length]], color=0x0000FF, width=0.05)

cone_vertices, cone_faces = create_cone()

x_transform = translation_matrix(axis_length, 0, 0) @ rotation_y_matrix(90)
plot += k3d.mesh(cone_vertices, cone_faces, color=0xFF0000, model_matrix=x_transform)

y_transform = translation_matrix(0, axis_length, 0) @ rotation_x_matrix(-90)
plot += k3d.mesh(cone_vertices, cone_faces, color=0x00FF00, model_matrix=y_transform)

z_transform = translation_matrix(0, 0, axis_length)
plot += k3d.mesh(cone_vertices, cone_faces, color=0x0000FF, model_matrix=z_transform)

label_offset = 0.2
plot += k3d.text("X", position=[axis_length+label_offset,0,0], color=0xFF0000, scale=0.3)
plot += k3d.text("Y", position=[0,axis_length+label_offset,0], color=0x00FF00, scale=0.3)
plot += k3d.text("Z", position=[0,0,axis_length+label_offset], color=0x0000FF, scale=0.3)

plot += k3d.points([[0, 0, 0]], point_size=0.1, color=0xFFFFFF)

plot.camera = [3, 3, 3, 0, 0, 0, 0, 0, 1]
plot.display()
