import json
import matplotlib.pyplot as plt

# Define object IDs as variables
OBJECT_ID_1 = 289
OBJECT_ID_2 = 290

# Load data from file
with open("sensor_data_2025-02-20_11-36-45.json", "r") as file:  # Replace with your filename
    data = json.load(file)

# Extract values
steps = list(range(len(data)))  # X-axis as step index
distance_1, distance_2 = [], []
lateral_margin_1, lateral_margin_2 = [], []
longitudinal_margin_1, longitudinal_margin_2 = [], []
is_dangerous_1, is_dangerous_2 = [], []

for frame in data:
    for obj in frame:
        if obj["objectId"] == OBJECT_ID_1:
            distance_1.append(obj["distance"])
            lateral_margin_1.append(obj["lateral_margin"])
            longitudinal_margin_1.append(obj["longitudinal_margin"])
            is_dangerous_1.append(1 if obj["is_dangerous"] else 0)
        elif obj["objectId"] == OBJECT_ID_2:
            distance_2.append(obj["distance"])
            lateral_margin_2.append(obj["lateral_margin"])
            longitudinal_margin_2.append(obj["longitudinal_margin"])
            is_dangerous_2.append(1 if obj["is_dangerous"] else 0)

# Create subplots: 1 row, 4 columns
fig, axes = plt.subplots(1, 4, figsize=(24, 5))

# Plot Distance Graph
axes[0].plot(steps, distance_1, label=f"Object {OBJECT_ID_1} Distance", color="blue")
axes[0].plot(steps, distance_2, label=f"Object {OBJECT_ID_2} Distance", color="red")
axes[0].set_xlabel("Steps")
axes[0].set_ylabel("Distance")
axes[0].set_title("Distance over Time")
axes[0].legend()
axes[0].grid()

# Plot Lateral Margin Graph
axes[1].plot(steps, lateral_margin_1, label=f"Object {OBJECT_ID_1} Lateral Margin", color="blue")
axes[1].plot(steps, lateral_margin_2, label=f"Object {OBJECT_ID_2} Lateral Margin", color="red")
axes[1].set_xlabel("Steps")
axes[1].set_ylabel("Lateral Margin")
axes[1].set_title("Lateral Margin over Time")
axes[1].legend()
axes[1].grid()

# Plot Is Dangerous Graph
axes[2].plot(steps, is_dangerous_1, label=f"Object {OBJECT_ID_1} Is Dangerous", color="blue")
axes[2].plot(steps, is_dangerous_2, label=f"Object {OBJECT_ID_2} Is Dangerous", color="red")
axes[2].set_xlabel("Steps")
axes[2].set_ylabel("Is Dangerous (0 or 1)")
axes[2].set_title("Is Dangerous over Time")
axes[2].legend()
axes[2].grid()

# Plot Longitudinal Margin Graph
axes[3].plot(steps, longitudinal_margin_1, label=f"Object {OBJECT_ID_1} Longitudinal Margin", color="blue")
axes[3].plot(steps, longitudinal_margin_2, label=f"Object {OBJECT_ID_2} Longitudinal Margin", color="red")
axes[3].set_xlabel("Steps")
axes[3].set_ylabel("Longitudinal Margin")
axes[3].set_title("Longitudinal Margin over Time")
axes[3].legend()
axes[3].grid()

# Adjust layout and show plots
plt.tight_layout()
plt.show()
