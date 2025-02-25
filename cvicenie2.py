import numpy as np

def find_optimal_route(cities, ideal_distance=440):
    K = len(cities)
    penalization = np.full(K, float('inf'))
    prev = np.full(K, -1)
    
    penalization[0] = 0

    for i in range(1, K):
        for j in range(i):
            distance = cities[i] - cities[j]
            penalty = (ideal_distance - distance) ** 2
            print("mesto",i,"spatne do",j,"penalizacia",penalty)

            if penalization[j] + penalty < penalization[i]:
                penalization[i] = penalization[j] + penalty
                prev[i] = j
    route = []
    index = K - 1
    while index != -1:
        route.append(index + 1)
        index = prev[index]
    
    return penalization[-1], list(reversed(route))

def load_data(filename):
    with open(filename, 'r') as file:
        cities = list(map(int, file.readlines()))
    return cities


filename = "Dat_21.txt"
cities = load_data(filename)
min_penalty, optimal_route = find_optimal_route(cities)

print(f"Minimálna penalizácia: {min_penalty}")
print("Optimálna trasa (indexy miest):", list(map(int, optimal_route)))
