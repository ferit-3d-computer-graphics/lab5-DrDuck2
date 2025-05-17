import k3d
import numpy as np
import time

vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
], dtype=np.float32)

indices = np.array([
    [0,1,2], [0,2,3], [4,5,6], [4,6,7],
    [0,1,5], [0,5,4], [1,2,6], [1,6,5],
    [2,3,7], [2,7,6], [3,0,4], [3,4,7]
], dtype=np.uint32)

cube = k3d.mesh(vertices, indices, color=0x00ff00, wireframe=True)
plot = k3d.plot()
plot += cube

def create_overlay_text(angle=0, fps=0):
    return k3d.text2d(
        f"Rotation Angle: {angle:.1f}°\nFPS: {fps:.1f}",
        position=[0.05, 0.05], 
        size=1.0,
        color=0x000000,
        label_box=False
    )

text_overlay = create_overlay_text()
plot += text_overlay

plot.display()

angle = 0
last_time = time.time()

for _ in range(300): 
    angle += 2
    theta = np.radians(angle)
    rot_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)
    
    cube.model_matrix = rot_matrix
    
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time
    fps = 1 / delta_time if delta_time > 0 else 0
    
    plot -= text_overlay
    text_overlay = create_overlay_text(angle, fps)
    plot += text_overlay
    
    time.sleep(0.05)