import math
import itertools
import numpy as np

def read_coordinates(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        start_index = lines.index('NODE_COORD_SECTION\n') + 1
        for line in lines[start_index:]:
            if line.strip() == 'EOF':
                break
            parts = line.split()
            coordinates.append((float(parts[1]), float(parts[2])))
    return coordinates

def calculate_distances(coordinates):
    num_cities = len(coordinates)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)
    return distances

# Definujeme veľké číslo pre nekonečno
INF = float('inf')

# Held-Karpov algoritmus
def tsp_dp(distances):
    n = len(distances)
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Začíname v meste A (index 0)

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if not (mask & (1 << v)) and distances[u][v] > 0:
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + distances[u][v])

    # Nájdeme najkratšiu cestu späť do mesta A
    # Každý stav dp[mask][u] uchováva najkratšiu cestu pre danú kombináciu miest
    min_cost = INF
    for u in range(1, n):
        if distances[u][0] > 0:
            min_cost = min(min_cost, dp[(1 << n) - 1][u] + distances[u][0])

    return min_cost


coordinates = read_coordinates('Test_23.txt')
print(coordinates)
distances = calculate_distances(coordinates)
print(distances)
min_cost = tsp_dp(distances)
print(f"Minimum cost: {min_cost}")