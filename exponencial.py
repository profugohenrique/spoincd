from scipy.stats import expon

# lambda = taxa
lambda_ = 1.5
amostra = expon(scale=1/lambda_).rvs(1000)
print(f"Exponencial (λ=1.5): {amostra[:5]}")
