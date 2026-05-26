import pandas as pd
import matplotlib.pyplot as plt

# Dark Theme
plt.style.use("dark_background")

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# ================= Vehicle Type Analysis =================

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor("#0f172a")

vehicle_data = df["Type_of_vehicle"].value_counts()

vehicle_data.plot(
    kind="bar",
    color=["skyblue", "orange", "lightgreen", "salmon"],
    ax=ax
)

ax.set_title("Orders by Vehicle Type", fontsize=14, fontweight="bold")
ax.set_xlabel("Vehicle")
ax.set_ylabel("Orders")
ax.tick_params(axis='x', rotation=0)
ax.grid(axis='y', linestyle='--', alpha=0.1)
ax.set_facecolor("#111827")

plt.tight_layout()
plt.show()
