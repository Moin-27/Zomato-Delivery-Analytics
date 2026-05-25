import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# Count Orders by Type
order_data = df["Type_of_order"].value_counts()

# Create Figure
plt.figure(figsize=(8,5))

# Plot Pie Chart
order_data.plot(kind='pie', autopct='%1.1f%%')

# Remove Y Label
plt.ylabel("")

# Title
plt.title("Distribution of Order Types", fontsize=14)

# Show Chart
plt.show()