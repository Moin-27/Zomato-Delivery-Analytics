import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# City Distribution
city_data = df["City"].value_counts()

# Create Figure
plt.figure(figsize=(6,6))

# Pie Chart
city_data.plot(
    kind='pie',
    autopct='%1.1f%%'
)

# Title
plt.title("City Distribution")

# Remove Y Label
plt.ylabel("")

# Show Chart
plt.show()