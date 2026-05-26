import pandas as pd
import matplotlib.pyplot as plt

# Dark Theme
plt.style.use("dark_background")

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# Average Delivery Time by Traffic Level
traffic_data = df.groupby(
    "Road_traffic_density"
)["Time_taken (min)"].mean()

# Create Figure
fig = plt.figure(figsize=(8,5))

# Background Color
fig.patch.set_facecolor("#0f172a")

# Plot Bar Chart
traffic_data.plot(
    kind='bar',
    color=["salmon","khaki","mediumseagreen","deepskyblue"]
)

# Title and Labels
plt.title(
    "Average Delivery Time by Traffic Level",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Traffic Level", fontsize=12)
plt.ylabel("Average Delivery Time (mins)", fontsize=12)

# Rotate Labels
plt.xticks(rotation=15)

# Add Grid
plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.1
)

# Graph Background
plt.gca().set_facecolor("#111827")

# Show Graph
plt.show()