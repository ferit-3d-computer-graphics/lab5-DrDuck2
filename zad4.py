import k3d
import numpy as np

np.random.seed(42)
group1_points = np.random.randn(100, 3) * 0.5 + [1, 1, 1]
group2_points = np.random.randn(80, 3) * 0.8 + [-1, -1, -1]
all_points = np.vstack([group1_points, group2_points])

group1_colors = np.full(len(group1_points), 0xFF0000)  
group2_colors = np.full(len(group2_points), 0x00FF00)  
all_colors = np.hstack([group1_colors, group2_colors])

label_indices = [
    *np.random.choice(len(group1_points), 5, replace=False),
    *len(group1_points) + np.random.choice(len(group2_points), 5)
]

plot = k3d.plot()
point_cloud = k3d.points(
    positions=all_points.astype(np.float32),
    colors=all_colors,
    point_size=0.2,
    shader='flat'
)
plot += point_cloud

for idx in label_indices:
    point = all_points[idx]
    label_text = f"Point {idx}\n({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})"
    
    group_color = 0xFF0000 if idx < len(group1_points) else 0x00FF00
    
    label_pos = point + [0, 0, 0.3]
    
    plot += k3d.text(
        label_text,
        position=label_pos.tolist(),
        color=group_color,
        scale=0.3,
        label_box=True
    )

plot += k3d.text2d(
    "Group Legend:\n🔴 Group 1 (Red)\n🟢 Group 2 (Green)",
    position=[0.05, 0.8],
    size=1.2,
    color=0xFFFFFF,
    label_box=True
)

plot.display()
