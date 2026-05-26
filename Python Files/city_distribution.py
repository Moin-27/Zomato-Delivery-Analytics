import pandas as pd
import matplotlib.pyplot as plt

# Dark Theme
plt.style.use("dark_background")

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# Count City Types
city_data = df["City"].value_counts()

# Create Figure
fig = plt.figure(figsize=(6,6))

# Background Color
fig.patch.set_facecolor("#0b132b")

# Plot Pie Chart
city_data.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=["#c084d2", "#5dade2", "#f5b041"],
    textprops={'color':'white'}
)

# Title
plt.title(
    "City Distribution",
    fontsize=16,
    fontweight='bold',
    color='white'
)

# Remove Y Label
plt.ylabel("")

# Show Graph
plt.show()