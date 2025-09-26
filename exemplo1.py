import numpy as np
import pandas as pd
from scipy import stats

# Conjunto 1 (Simétrico)
dados1 = [45, 48, 49, 50, 50, 51, 52, 55]
print("Conjunto 1:")
print(f"Média: {np.mean(dados1):.2f}")
print(f"Desvio Padrão: {np.std(dados1, ddof=1):.2f}")  # ddof=1 para amostra
print(f"Assimetria: {stats.skew(dados1):.2f}")

# Conjunto 2 (Dispersão Alta)
dados2 = [10, 30, 40, 50, 50, 60, 70, 90]
print("\nConjunto 2:")
print(f"Média: {np.mean(dados2):.2f}")
print(f"Desvio Padrão: {np.std(dados2, ddof=1):.2f}")
print(f"Assimetria: {stats.skew(dados2):.2f}")

import matplotlib.pyplot as plt
plt.boxplot([dados1, dados2], labels=["Conjunto 1", "Conjunto 2"])
plt.title("Comparação de Dispersão")
plt.show()
