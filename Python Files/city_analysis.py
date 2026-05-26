import pandas as pd
import matplotlib.pyplot as plt

# Dark Theme
plt.style.use("dark_background")

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# City Distribution Data
city_data = df["City"].value_counts()

# Create Figure
fig = plt.figure(figsize=(6,6))

# Background Color
fig.patch.set_facecolor("#0f172a")

# Pie Chart
city_data.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=["plum","skyblue","orange"],
    textprops={'color':'white'}
)

# Title
plt.title(
    "City Distribution",
    fontsize=16,
    fontweight="bold"
)

# Remove Y Label
plt.ylabel("")

# Show Chart
plt.show()