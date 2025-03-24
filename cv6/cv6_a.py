import networkx as nx


def load_graph(filename):
    G = nx.Graph()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            city1, city2 = line.strip().split()
            G.add_edge(city1, city2)
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


filename = "Stanice6.txt"
G = load_graph(filename)
stations = greedy_station_placement(G)

print(f"Počet miest s nabíjacími stanicami: {len(stations)}")
print("Mestá s nabíjacími stanicami:", " ".join(stations))
