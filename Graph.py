import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv("results.csv")

# График 1: Приближение площади
plt.figure(figsize=(10, 6))
plt.plot(data["N"], data["Approximation"], label="Approximation", color="blue")
plt.axhline(y=0.25 * 3.14159265359 + 1.25 * 0.927295218001 - 1, color="red", linestyle="--", label="Exact Area")
plt.xlabel("Number of Points (N)")
plt.ylabel("Area")
plt.title("Monte Carlo Approximation of Intersection Area")
plt.legend()
plt.grid()
plt.show()

# График 2: Относительное отклонение
plt.figure(figsize=(10, 6))
plt.plot(data["N"], data["Error"], label="Relative Error (%)", color="green")
plt.xlabel("Number of Points (N)")
plt.ylabel("Relative Error (%)")
plt.title("Relative Error of Approximation")
plt.legend()
plt.grid()
plt.show()
