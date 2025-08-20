# ================================
# Full Assignment: Data Handling & Visualization
# ================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ======================================
# 1. Data Visualization with Matplotlib
# ======================================
print("\n--- 1. Matplotlib Visualization ---")

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Line plot
plt.plot(x, y, marker='o', color='blue')
plt.title("Line Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar chart
plt.bar(x, y, color='green')
plt.title("Bar Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# ======================================
# 2. NumPy Multidimensional Arrays
# ======================================
print("\n--- 2. NumPy Arrays ---")

# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((3, 3))
ones = np.ones((2, 3))

print("1D Array:", arr1)
print("3x3 Zeros:\n", zeros)
print("2x3 Ones:\n", ones)

# Reshape
reshaped = arr1.reshape((5, 1))
print("\nReshaped to column vector:\n", reshaped)

# Attributes
print("Shape:", reshaped.shape)
print("Data type:", reshaped.dtype)

# ======================================
# 3. Pandas Data Cleaning
# ======================================
print("\n--- 3. Pandas Data Cleaning ---")

# Create DataFrame with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, np.nan, 30, 22],
    "Score": [85, 90, np.nan, 70]
}
df = pd.DataFrame(data)

print("\nOriginal DataFrame:\n", df)

# Inspect
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe())

# Drop rows with missing values
df_dropped = df.dropna()
print("\nAfter dropna:\n", df_dropped)

# Fill missing values with mean
df_filled = df.copy()
df_filled["Score"].fillna(df["Score"].mean(), inplace=True)
df_filled["Age"].fillna(df["Age"].mean(), inplace=True)

print("\nAfter fillna with mean:\n", df_filled)

# Done
print("\n=== Assignment Completed ===")
