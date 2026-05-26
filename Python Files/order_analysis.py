import pandas as pd
import matplotlib.pyplot as plt

# Dark Theme
plt.style.use("dark_background")

# Load Dataset
df = pd.read_csv("../Dataset/Zomato Dataset.csv")

# Count Orders by Type
order_data = df["Type_of_order"].value_counts()

# Create Figure
fig = plt.figure(figsize=(8,5))

# Background Color
fig.patch.set_facecolor("#0f172a")

# Plot Pie Chart
order_data.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=["skyblue","orange","mediumseagreen","plum"],
    textprops={'color':'white'}
)

# Remove Y Label
plt.ylabel("")

# Title
plt.title(
    "Distribution of Order Types",
    fontsize=14,
    fontweight="bold"
)

# Show Chart
plt.show()