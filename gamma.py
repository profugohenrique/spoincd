from scipy.stats import gamma

# alpha = shape, beta = rate
alpha, beta = 2, 1
amostra = gamma(alpha, scale=1/beta).rvs(1000)
print(f"Gamma (α=2, β=1): {amostra[:5]}")
