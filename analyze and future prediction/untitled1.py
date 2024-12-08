import pandas as pd

# Load dataset
df = pd.read_csv("line_fault_dataset.csv")

# Define thresholds
thresholds = {
    "Voltage (V)": (220, 240),
    "Current (A)": (10, 20),
    "Temperature (°C)": (20, 80),
    "Vibration (mm/s)": (0, 5)
}

# Fault analysis function
def analyze_fault(row):
    faults = []
    if not thresholds["Voltage (V)"][0] <= row["Voltage (V)"] <= thresholds["Voltage (V)"][1]:
        faults.append("Voltage Fault")
    if not thresholds["Current (A)"][0] <= row["Current (A)"] <= thresholds["Current (A)"][1]:
        faults.append("Current Fault")
    if not thresholds["Temperature (°C)"][0] <= row["Temperature (°C)"] <= thresholds["Temperature (°C)"][1]:
        faults.append("Temperature Fault")
    if not thresholds["Vibration (mm/s)"][0] <= row["Vibration (mm/s)"] <= thresholds["Vibration (mm/s)"][1]:
        faults.append("Vibration Fault")
    return faults if faults else ["Normal"]

# Apply fault analysis
df["Fault Type"] = df.apply(analyze_fault, axis=1)

# Summarize results
fault_summary = df["Fault Type"].explode().value_counts()

print("Fault Summary:\n", fault_summary)

# Save analyzed dataset
df.to_csv("analyzed_line_faults.csv", index=False)


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("line_fault_dataset.csv")

# Plot line chart
df[["Voltage (V)", "Current (A)", "Temperature (°C)", "Vibration (mm/s)"]][:100].plot(figsize=(10, 6))
plt.title("Parameter Trends Over Time")
plt.xlabel("Sample Index")
plt.ylabel("Values")
plt.legend(loc="upper right")
plt.grid()
plt.show()


plt.figure(figsize=(8, 6))

# Scatter plot for Voltage vs Current
plt.scatter(df["Voltage (V)"], df["Current (A)"], c="blue", alpha=0.5, label="Voltage vs Current")
plt.title("Voltage vs Current Scatter Plot")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.legend()
plt.grid()
plt.show()

fault_counts = df["Fault Type"].explode().value_counts()

# Plot bar chart
fault_counts.plot(kind="bar", figsize=(8, 5), color="orange")
plt.title("Frequency of Fault Types")
plt.xlabel("Fault Type")
plt.ylabel("Count")
plt.grid(axis="y")
plt.show()
