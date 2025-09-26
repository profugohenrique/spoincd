from scipy.stats import beta
import matplotlib.pyplot as plt
# alpha, beta > 0
alpha, betas = 2, 5
amostra = beta(alpha, betas).rvs(1000)
print(f"Beta (α=2, β=5): {amostra[:5]}")
plt.hist(amostra)
plt.show()
