from scipy.stats import chi2

# df = graus de liberdade
df = 4
amostra = chi2(df).rvs(1000)
print(f"Qui-Quadrado (df=4): {amostra[:5]}")
