import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/Zomato Dataset.csv")

# Average Delivery Time by Traffic Level
traffic_data = df.groupby("Road_traffic_density")["Time_taken (min)"].mean()

# Create Figure
plt.figure(figsize=(8,5))

# Plot Chart
traffic_data.plot(kind='bar')

# Title and Labels
plt.title("Average Delivery Time by Traffic Level", fontsize=14)
plt.xlabel("Traffic Level", fontsize=12)
plt.ylabel("Average Delivery Time (mins)", fontsize=12)

# Rotate Labels
plt.xticks(rotation=15)

# Add Grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show Graph
plt.show()