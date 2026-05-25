import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/Zomato Dataset.csv")

# Average Delivery Time by City
avg_delivery = df.groupby("City")["Time_taken (min)"].mean()

# Create Figure
plt.figure(figsize=(8,5))

# Plot Bar Chart
avg_delivery.plot(kind='bar')

# Chart Title & Labels
plt.title("Average Delivery Time by City", fontsize=14)
plt.xlabel("City Type", fontsize=12)
plt.ylabel("Average Delivery Time (mins)", fontsize=12)

# Rotate X-axis Labels
plt.xticks(rotation=15)

# Add Grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show Graph
plt.show()
