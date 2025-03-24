import networkx as nx


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
        # Vyberieme mesto s najviac nepokrytými susedmi
        best_city = max(G.nodes - covered, key=lambda city: len(set(G.neighbors(city)) - covered), default=None)

        if best_city is None:
            break

        # Umiestnime stanicu
        stations.add(best_city)
        covered.add(best_city)
        covered.update(G.neighbors(best_city))

    return stations


def compute_approximation_ratio(k, m):
    G = generate_grid_graph(k, m)
    stations = greedy_station_placement(G)
    approx_ratio = len(stations) / (k * m / 5)
    return len(stations), approx_ratio


filename = "Stanice6.txt"
G = load_graph(filename)
stations = greedy_station_placement(G)

print(f"Počet miest s nabíjacími stanicami: {len(stations)}")
print("Mestá s nabíjacími stanicami:", " ".join(map(str, stations)))

# Testovanie na mriežkovom grafe
k, m = 5, 5  # Príklad rozmerov
num_stations, approx_ratio = compute_approximation_ratio(k, m)
print(f"Pre mriežkový graf {k}x{m} je počet staníc: {num_stations}")
print(f"Aproximačný pomer: {approx_ratio:.2f}")
