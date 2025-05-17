import k3d
import numpy as np

red_sphere = k3d.points([[1, 0, 0]], color=0xFF0000, point_size=0.3)
blue_points = k3d.points([[0, 0, 1], [0, 1, 0]], color=0x0000FF, point_size=0.3)

legend_items = [
    ("Scene Legend", 0x000000, 1.2, [0.7, 0.60]),  # Title
    ("■ Red: Critical Errors", 0xFF0000, 1.2, [0.7, 0.70]),
    ("■ Blue: Neutral Areas", 0x0000FF, 1.2, [0.7, 0.80])
]

plot = k3d.plot()
plot += red_sphere
plot += blue_points

for text, color, size, pos in legend_items:
    plot += k3d.text2d(
        text,
        position=pos,
        color=color,
        size=size,
        label_box=True,
        reference_point='lt'         
    )

plot += k3d.line([[0,0,0], [2,0,0]], color=0xAAAAAA, width=0.02)
plot += k3d.line([[0,0,0], [0,2,0]], color=0xAAAAAA, width=0.02)
plot += k3d.line([[0,0,0], [0,0,2]], color=0xAAAAAA, width=0.02)

plot.display()
