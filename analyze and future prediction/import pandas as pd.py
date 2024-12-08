import pandas as pd
import numpy as np

# Simulate normal and faulty conditions
np.random.seed(42)

# Generate synthetic data
data = {
    "Voltage (V)": np.random.normal(230, 5, 1000).tolist() + np.random.choice([210, 250], 50).tolist(),
    "Current (A)": np.random.normal(15, 2, 1000).tolist() + np.random.choice([5, 25], 50).tolist(),
    "Temperature (°C)": np.random.normal(50, 10, 1000).tolist() + np.random.choice([90, 100], 50).tolist(),
    "Vibration (mm/s)": np.random.normal(2, 1, 1000).tolist() + np.random.choice([6, 7], 50).tolist(),
    "Label": ["Normal"] * 1000 + ["Fault"] * 50
}

# Create DataFrame
df = pd.DataFrame(data)
df.to_csv("line_fault_dataset.csv", index=False)

print("Dataset created!")
