import json
import csv

# Define object IDs as variables
OBJECT_ID_1 = 577
OBJECT_ID_2 = 578

def fix_value(x):
    """Replace a value of 1000000000.0 with 0."""
    if isinstance(x, (int, float)) and x == 1000000000.0:
        return 0
    return x

def calculate_risk(d_current, d_safe):
    """Compute the absolute risk value based on the formula."""
    if d_current >= d_safe:
        return 0
    elif d_safe > 0:  # Avoid division by zero
        return 1 - (d_current / d_safe)
    return 1  # Maximum risk if safe distance is zero

# Load JSON data (adjust filename as needed)
with open("data2/sensor_data_2025-02-09_17-50-14.json", "r") as f:
    data = json.load(f)

# Prepare CSV headers
graph1_rows = [["step", f"obj{OBJECT_ID_1}_distance", f"obj{OBJECT_ID_2}_distance"]]
graph2_rows = [["step", f"obj{OBJECT_ID_1}_lateral_margin", f"obj{OBJECT_ID_2}_lateral_margin"]]
graph3_rows = [["step", f"obj{OBJECT_ID_1}_is_dangerous", f"obj{OBJECT_ID_2}_is_dangerous"]]
graph4_rows = [["step", f"obj{OBJECT_ID_1}_longitudinal_margin", f"obj{OBJECT_ID_2}_longitudinal_margin"]]

# Safe vs. Current Distances
graph5_rows = [["step", "longitudinal_safe_distance", "current_longitudinal_distance"]]  # Object 1
graph6_rows = [["step", "lateral_right_safe_distance", "current_lateral_right_distance"]]  # Object 1
graph7_rows = [["step", "lateral_left_safe_distance", "current_lateral_left_distance"]]  # Object 1
graph8_rows = [["step", "longitudinal_safe_distance", "current_longitudinal_distance"]]  # Object 2
graph9_rows = [["step", "lateral_right_safe_distance", "current_lateral_right_distance"]]  # Object 2
graph10_rows = [["step", "lateral_left_safe_distance", "current_lateral_left_distance"]]  # Object 2

# Risk Values
graph11_rows = [["step", "longitudinal_risk"]]  # Object 1
graph12_rows = [["step", "lateral_right_risk"]]  # Object 1
graph13_rows = [["step", "lateral_left_risk"]]  # Object 1
graph14_rows = [["step", "longitudinal_risk"]]  # Object 2
graph15_rows = [["step", "lateral_right_risk"]]  # Object 2
graph16_rows = [["step", "lateral_left_risk"]]  # Object 2

# Process each step
for step, frame in enumerate(data):
    obj1, obj2 = None, None

    for obj in frame:
        if obj.get("objectId") == OBJECT_ID_1:
            obj1 = obj
        elif obj.get("objectId") == OBJECT_ID_2:
            obj2 = obj

    # Extract values for Object 1
    if obj1:
        obj1_distance = fix_value(obj1.get("distance", 0))
        obj1_lateral_margin = fix_value(obj1.get("lateral_margin", 0))
        obj1_is_dangerous = 1 if obj1.get("is_dangerous") else 0
        obj1_longitudinal_margin = fix_value(obj1.get("longitudinal_margin", 0))
        obj1_long_safe = fix_value(obj1.get("longitudinal_safe_distance", 0))
        obj1_curr_long = fix_value(obj1.get("current_longitudinal_distance", 0))
        obj1_lat_right_safe = fix_value(obj1.get("lateral_right_safe_distance", 0))
        obj1_curr_lat_right = fix_value(obj1.get("current_lateral_right_distance", 0))
        obj1_lat_left_safe = fix_value(obj1.get("lateral_left_safe_distance", 0))
        obj1_curr_lat_left = fix_value(obj1.get("current_lateral_left_distance", 0))
    else:
        obj1_distance = obj1_lateral_margin = obj1_is_dangerous = obj1_longitudinal_margin = 0
        obj1_long_safe = obj1_curr_long = obj1_lat_right_safe = obj1_curr_lat_right = 0
        obj1_lat_left_safe = obj1_curr_lat_left = 0

    # Extract values for Object 2
    if obj2:
        obj2_distance = fix_value(obj2.get("distance", 0))
        obj2_lateral_margin = fix_value(obj2.get("lateral_margin", 0))
        obj2_is_dangerous = 1 if obj2.get("is_dangerous") else 0
        obj2_longitudinal_margin = fix_value(obj2.get("longitudinal_margin", 0))
        obj2_long_safe = fix_value(obj2.get("longitudinal_safe_distance", 0))
        obj2_curr_long = fix_value(obj2.get("current_longitudinal_distance", 0))
        obj2_lat_right_safe = fix_value(obj2.get("lateral_right_safe_distance", 0))
        obj2_curr_lat_right = fix_value(obj2.get("current_lateral_right_distance", 0))
        obj2_lat_left_safe = fix_value(obj2.get("lateral_left_safe_distance", 0))
        obj2_curr_lat_left = fix_value(obj2.get("current_lateral_left_distance", 0))
    else:
        obj2_distance = obj2_lateral_margin = obj2_is_dangerous = obj2_longitudinal_margin = 0
        obj2_long_safe = obj2_curr_long = obj2_lat_right_safe = obj2_curr_lat_right = 0
        obj2_lat_left_safe = obj2_curr_lat_left = 0

    # Compute risk values
    risk_long_1 = calculate_risk(obj1_curr_long, obj1_long_safe)
    risk_lat_right_1 = calculate_risk(obj1_curr_lat_right, obj1_lat_right_safe)
    risk_lat_left_1 = calculate_risk(obj1_curr_lat_left, obj1_lat_left_safe)

    risk_long_2 = calculate_risk(obj2_curr_long, obj2_long_safe)
    risk_lat_right_2 = calculate_risk(obj2_curr_lat_right, obj2_lat_right_safe)
    risk_lat_left_2 = calculate_risk(obj2_curr_lat_left, obj2_lat_left_safe)

    # Append data to CSV rows
    graph1_rows.append([step, obj1_distance, obj2_distance])
    graph2_rows.append([step, obj1_lateral_margin, obj2_lateral_margin])
    graph3_rows.append([step, obj1_is_dangerous, obj2_is_dangerous])
    graph4_rows.append([step, obj1_longitudinal_margin, obj2_longitudinal_margin])

    graph5_rows.append([step, obj1_long_safe, obj1_curr_long])
    graph6_rows.append([step, obj1_lat_right_safe, obj1_curr_lat_right])
    graph7_rows.append([step, obj1_lat_left_safe, obj1_curr_lat_left])
    graph8_rows.append([step, obj2_long_safe, obj2_curr_long])
    graph9_rows.append([step, obj2_lat_right_safe, obj2_curr_lat_right])
    graph10_rows.append([step, obj2_lat_left_safe, obj2_curr_lat_left])

    graph11_rows.append([step, risk_long_1])
    graph12_rows.append([step, risk_lat_right_1])
    graph13_rows.append([step, risk_lat_left_1])
    graph14_rows.append([step, risk_long_2])
    graph15_rows.append([step, risk_lat_right_2])
    graph16_rows.append([step, risk_lat_left_2])

# Save CSV files
for i, rows in enumerate([graph1_rows, graph2_rows, graph3_rows, graph4_rows, graph5_rows, graph6_rows, 
                          graph7_rows, graph8_rows, graph9_rows, graph10_rows, graph11_rows, graph12_rows, 
                          graph13_rows, graph14_rows, graph15_rows, graph16_rows], start=1):
    with open(f"graph{i}.csv", "w", newline="") as f:
        csv.writer(f).writerows(rows)

print("16 CSV files generated successfully!")
