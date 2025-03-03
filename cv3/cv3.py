import math
import itertools

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

def tsp_dynamic_programming(distances):
    num_cities = len(distances)
    all_sets = 1 << num_cities
    dp = [[float('inf')] * num_cities for _ in range(all_sets)]
    dp[1][0] = 0

    for subset_size in range(2, num_cities + 1):
        for subset in itertools.combinations(range(1, num_cities), subset_size - 1):
            bits = 1
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev_bits = bits & ~(1 << k)
                for m in subset:
                    if m == k:
                        continue
                    dp[bits][k] = min(dp[bits][k], dp[prev_bits][m] + distances[m][k])

    bits = (1 << num_cities) - 1
    min_cost = float('inf')
    for k in range(1, num_cities):
        min_cost = min(min_cost, dp[bits][k] + distances[k][0])

    return min_cost

coordinates = read_coordinates('Test_13.txt')
print(coordinates)
distances = calculate_distances(coordinates)
print(distances)
min_cost = tsp_dynamic_programming(distances)
print(f"Minimum cost: {min_cost}")