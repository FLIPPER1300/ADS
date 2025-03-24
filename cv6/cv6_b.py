import networkx as nx
import matplotlib.pyplot as plt
import math


def load_graph(filename):
    G = nx.Graph()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            city1, city2 = line.strip().split()
            G.add_edge(city1, city2)
    return G


def generate_grid_graph(k, m):
    G = nx.grid_2d_graph(k, m)
    return G


def greedy_station_placement(G):
    covered = set()
    stations = set()

    while len(covered) < len(G.nodes):
        best_city = max(G.nodes - covered, key=lambda city: len(set(G.neighbors(city)) - covered), default=None)

        if best_city is None:
            break

        stations.add(best_city)
        covered.add(best_city)
        covered.update(G.neighbors(best_city))

    return stations


def optimal_station_count(k, m):
    if k == 4 and m >= 10:
        return m
    elif k == 6 and m >= 7:
        return math.ceil((10 * m + 4) / 7)
    elif 16 <= k <= m:
        return math.ceil(((k + 2) * (m + 2)) / 5) - 4
    else:
        return k * m // 5  # Približný odhad pre iné hodnoty


def compute_approximation_ratio(k, m):
    G = generate_grid_graph(k, m)
    stations = greedy_station_placement(G)
    opt_count = optimal_station_count(k, m)
    approx_ratio = len(stations) / opt_count if opt_count > 0 else float('inf')
    return G, stations, len(stations), opt_count, approx_ratio


def draw_graph(G, stations):
    pos = {node: (node[1], -node[0]) for node in G.nodes()}
    plt.figure(figsize=(8, 8))

    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=500)
    nx.draw_networkx_nodes(G, pos, nodelist=stations, node_color='red', node_size=600)

    plt.title("Nabíjacie stanice v grafe")
    plt.show()



filename = "Stanice6.txt"
G = load_graph(filename)
stations = greedy_station_placement(G)

print(f"Počet miest s nabíjacími stanicami: {len(stations)}")
print("Mestá s nabíjacími stanicami:", " ".join(map(str, stations)))

# Testovanie na mriežkovom grafe
k, m = 6,7   # Príklad rozmerov
grid_G, grid_stations, num_stations, opt_stations, approx_ratio = compute_approximation_ratio(k, m)
print(f"Pre mriežkový graf {k}x{m} je počet staníc: {num_stations}")
print(f"Optimálny počet staníc: {opt_stations}")
print(f"Aproximačný pomer: {approx_ratio:.2f}")

# Vykreslenie grafu
draw_graph(grid_G, grid_stations)
