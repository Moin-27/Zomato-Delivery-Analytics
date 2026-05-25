import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/Zomato Dataset.csv")

# Count Orders by Vehicle Type
vehicle_data = df["Type_of_vehicle"].value_counts()

# Create Figure
plt.figure(figsize=(8,5))

# Plot Bar Chart
vehicle_data.plot(kind='bar')

# Title and Labels
plt.title("Orders by Vehicle Type", fontsize=14)
plt.xlabel("Vehicle Type", fontsize=12)
plt.ylabel("Number of Orders", fontsize=12)

# Rotate Labels
plt.xticks(rotation=0)

# Add Grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show Graph
plt.show()