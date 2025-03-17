import numpy as np

# Načítanie matice D zo súboru
with open("cvicenie5a-1.txt", "r") as f:
    D = np.array([list(map(int, line.split())) for line in f])

m, n = D.shape  # 1000 x 50
dp = np.zeros((m, n), dtype=int)

# Inicializácia DP matice
dp[0, :] = D[0, :]

# Vypočítanie minimálneho poškodenia
for i in range(1, m):
    for j in range(n):
        min_prev = dp[i-1, j]  # Priamo nad
        if j > 0:
            min_prev = min(min_prev, dp[i-1, j-1])  # Ľavý horný
        if j < n-1:
            min_prev = min(min_prev, dp[i-1, j+1])  # Pravý horný
        dp[i, j] = D[i, j] + min_prev

# Nájdeme minimálne poškodenie
min_damage = np.min(dp[-1])
print("Minimálne možné poškodenie:", min_damage)
