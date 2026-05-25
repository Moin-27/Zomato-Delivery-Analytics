import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# Average Delivery Time by Delivery Person Rating
rating_data = df.groupby("Delivery_person_Ratings")["Time_taken (min)"].mean()

# Create Figure
plt.figure(figsize=(10,5))

# Plot Line Chart
rating_data.plot(marker='o')

# Title and Labels
plt.title("Delivery Time by Delivery Partner Ratings", fontsize=14)
plt.xlabel("Delivery Partner Ratings", fontsize=12)
plt.ylabel("Average Delivery Time (mins)", fontsize=12)

# Add Grid
plt.grid(linestyle='--', alpha=0.5)

# Show Graph
plt.show()