import pandas as pd
import matplotlib.pyplot as plt

# Dark Theme
plt.style.use("dark_background")

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# Create Figure
fig = plt.figure(figsize=(18,12))

# Background Color
fig.patch.set_facecolor("#0f172a")


# ================= GRAPH 1 =================

ax1 = plt.subplot(3,2,1)

city_data = df.groupby("City")["Time_taken (min)"].mean()

city_data.plot(
    kind="bar",
    color=["skyblue","orange","lightgreen"]
)

plt.title("Average Delivery Time by City")
plt.xlabel("City")
plt.ylabel("Time (mins)")

ax1.tick_params(axis='x', rotation=15)

plt.grid(axis='y', linestyle='--', alpha=0.1)

ax1.set_facecolor("#111827")


# ================= GRAPH 2 =================

ax2 = plt.subplot(3,2,2)

traffic_data = df.groupby(
    "Road_traffic_density"
)["Time_taken (min)"].mean()

traffic_data.plot(
    kind="bar",
    color=["salmon","khaki","mediumseagreen","deepskyblue"]
)

plt.title("Traffic Impact Analysis")
plt.xlabel("Traffic Level")
plt.ylabel("Time (mins)")

ax2.tick_params(axis='x', rotation=15)

plt.grid(axis='y', linestyle='--', alpha=0.1)

ax2.set_facecolor("#111827")


# ================= GRAPH 3 =================

ax3 = plt.axes([0.22, 0.34, 0.24, 0.24])

order_data = df["Type_of_order"].value_counts()

order_data.plot(
    kind="pie",
    autopct="%1.1f%%",
    colors=["skyblue","orange","mediumseagreen","plum"],
    textprops={'color':'white'}
)

plt.title("Order Types")
plt.ylabel("")

ax3.set_facecolor("#0f172a")


# ================= GRAPH 4 =================

ax4 = plt.axes([0.54, 0.34, 0.24, 0.24])

city_pie = df["City"].value_counts()

city_pie.plot(
    kind="pie",
    autopct="%1.1f%%",
    colors=["plum","skyblue","orange"],
    textprops={'color':'white'}
)

plt.title("City Distribution")
plt.ylabel("")

ax4.set_facecolor("#0f172a")


# ================= GRAPH 5 =================

ax5 = plt.subplot(3,2,5)

weather_data = df.groupby(
    "Weather_conditions"
)["Time_taken (min)"].mean()

weather_data.plot(
    kind="bar",
    color="mediumseagreen"
)

plt.title("Weather Impact Analysis")
plt.xlabel("Weather")
plt.ylabel("Time (mins)")

ax5.tick_params(axis='x', rotation=15)

plt.grid(axis='y', linestyle='--', alpha=0.1)

ax5.set_facecolor("#111827")


# ================= GRAPH 6 =================

ax6 = plt.subplot(3,2,6)

vehicle_data = df["Type_of_vehicle"].value_counts()

vehicle_data.plot(
    kind="bar",
    color=["skyblue","orange","lightgreen","salmon"]
)

plt.title("Orders by Vehicle Type")
plt.xlabel("Vehicle")
plt.ylabel("Orders")

ax6.tick_params(axis='x', rotation=0)

plt.grid(axis='y', linestyle='--', alpha=0.1)

ax6.set_facecolor("#111827")


# ================= DASHBOARD TITLE =================

fig.suptitle(
    "Zomato Delivery Analytics Dashboard",
    fontsize=22,
    fontweight="bold"
)

# Layout
plt.tight_layout(pad=4)

# Show Dashboard
plt.show()