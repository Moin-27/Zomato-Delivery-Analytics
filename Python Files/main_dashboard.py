import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset/Zomato Dataset.csv")

# Create Dashboard Figure
plt.figure(figsize=(18,12))

# ================= GRAPH 1 =================
plt.subplot(3,2,1)

city_data = df.groupby("City")["Time_taken (min)"].mean()

city_data.plot(kind='bar')

plt.title("Average Delivery Time by City")
plt.xlabel("City")
plt.ylabel("Time (mins)")

plt.xticks(rotation=15, fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.5)


# ================= GRAPH 2 =================
plt.subplot(3,2,2)

traffic_data = df.groupby("Road_traffic_density")["Time_taken (min)"].mean()

traffic_data.plot(kind='bar')

plt.title("Traffic Impact Analysis")
plt.xlabel("Traffic Level")
plt.ylabel("Time (mins)")

plt.xticks(rotation=15, fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.5)


# ================= GRAPH 3 =================
# PIE CHART IN CENTER

plt.axes([0.37, 0.34, 0.26, 0.26])

order_data = df["Type_of_order"].value_counts()

order_data.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Distribution of Order Types")
plt.ylabel("")


# ================= GRAPH 4 =================
plt.subplot(3,2,5)

weather_data = df.groupby("Weather_conditions")["Time_taken (min)"].mean()

weather_data.plot(kind='bar')

plt.title("Weather Impact Analysis")
plt.xlabel("Weather")
plt.ylabel("Time (mins)")

plt.xticks(rotation=15, fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.5)


# ================= GRAPH 5 =================
plt.subplot(3,2,6)

vehicle_data = df["Type_of_vehicle"].value_counts()

vehicle_data.plot(kind='bar')

plt.title("Orders by Vehicle Type")
plt.xlabel("Vehicle")
plt.ylabel("Orders")

plt.xticks(rotation=0, fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.5)


# Layout Spacing
plt.tight_layout(pad=4.0)

# Show Dashboard
plt.show()