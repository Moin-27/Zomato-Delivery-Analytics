import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/Zomato Dataset.csv")

# Average Delivery Time by Weather
weather_data = df.groupby("Weather_conditions")["Time_taken (min)"].mean()

# Create Figure
plt.figure(figsize=(10,5))

# Plot Bar Chart
weather_data.plot(kind='bar')

# Title and Labels
plt.title("Average Delivery Time by Weather Conditions", fontsize=14)
plt.xlabel("Weather Conditions", fontsize=12)
plt.ylabel("Average Delivery Time (mins)", fontsize=12)

# Rotate Labels
plt.xticks(rotation=20)

# Add Grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show Graph
plt.show()