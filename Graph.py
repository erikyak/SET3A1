import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("results3d.csv")

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

scales = data["Scale"]
n_points = data["N"]
approximations = data["Approximation"]

# Построение 3D-графика приближенной площади
sc = ax.scatter(n_points, scales, approximations, c=approximations, cmap='viridis', label="Approximated Area")
ax.set_xlabel("Number of Points (N)")
ax.set_ylabel("Scale")
ax.set_zlabel("Approximated Area")
ax.set_title("Monte Carlo Approximation of Intersection Area (3D)")

fig.colorbar(sc, ax=ax, label="Approximated Area")
plt.show()

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

errors = data["Error"]

# Построение 3D-графика относительного отклонения
sc = ax.scatter(n_points, scales, errors, c=errors, cmap='plasma', label="Relative Error (%)")
ax.set_xlabel("Number of Points (N)")
ax.set_ylabel("Scale")
ax.set_zlabel("Relative Error (%)")
ax.set_title("Relative Error of Approximation (3D)")

fig.colorbar(sc, ax=ax, label="Relative Error (%)")
plt.show()
