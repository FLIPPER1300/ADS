import numpy as np

def find_optimal_route(cities, ideal_distance=440):
    K = len(cities)
    dp = np.full(K, float('inf'))  # Minimálne penalizácie
    prev = np.full(K, -1)  # Optimálne predchádzajúce zastávky
    
    dp[0] = 0  # Začiatok cesty nemá penalizáciu
    
    for i in range(1, K):  # Pre každé mesto
        for j in range(i):  # Skúmame všetky predchádzajúce možné zastávky
            distance = cities[i] - cities[j]
            penalty = (ideal_distance - distance) ** 2
            
            if dp[j] + penalty < dp[i]:
                dp[i] = dp[j] + penalty
                prev[i] = j
    
    # Rekonštrukcia optimálnej trasy
    route = []
    index = K - 1
    while index != -1:
        route.append(index + 1)  # Indexy premeníme na poradie (číslovanie od 1)
        index = prev[index]
    
    return dp[-1], list(reversed(route))

# Načítanie vstupného súboru
def load_data(filename):
    with open(filename, 'r') as file:
        cities = list(map(int, file.readlines()))
    return cities


filename = "Dat_21.txt"  # Zmeňte podľa potreby
cities = load_data(filename)
min_penalty, optimal_route = find_optimal_route(cities)

print(f"Minimálna penalizácia: {min_penalty}")
print("Optimálna trasa (indexy miest):", list(map(int, optimal_route)))
