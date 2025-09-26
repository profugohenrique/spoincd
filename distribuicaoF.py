from scipy.stats import f

# dfn, dfd = graus de liberdade
dfn, dfd = 5, 10
amostra = f(dfn, dfd).rvs(1000)
print(f"F (5,10): {amostra[:5]}")
