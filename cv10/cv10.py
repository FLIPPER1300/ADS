import re
import itertools
from collections import defaultdict,deque
import networkx as nx
import matplotlib.pyplot as plt

def parse_all_formulas(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    formulas = {}
    i = 0
    while i < len(lines):
        if re.match(r'^P\d+', lines[i]):
            name = lines[i]
            n_vars, n_clauses = map(int, lines[i + 1].split())
            clauses = []
            for j in range(i + 2, i + 2 + n_clauses):
                literals = list(map(int, lines[j].split()))
                clause = [lit for lit in literals if lit != 0]
                if clause:
                    clauses.append(clause)
            formulas[name] = (n_vars, clauses)
            i += 2 + n_clauses
        else:
            i += 1
    return formulas

def add_edge(graph, frm, to):
    graph[frm].append(to)

def create_implication_graph(n_vars, clauses):
    graph = defaultdict(list)
    for a, b in clauses:
        add_edge(graph, -a, b)
        add_edge(graph, -b, a)
    return graph

def kosaraju_scc(graph):
    visited = set()
    order = []

    def dfs(v):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs(u)
        order.append(v)

    for v in list(graph.keys()) + [k for k in range(-n_vars, n_vars+1) if k != 0]:
        if v not in visited:
            dfs(v)

    # Transpose the graph
    transposed = defaultdict(list)
    for v in graph:
        for u in graph[v]:
            transposed[u].append(v)

    # Second pass
    visited.clear()
    components = {}
    def reverse_dfs(v, label):
        visited.add(v)
        components[v] = label
        for u in transposed[v]:
            if u not in visited:
                reverse_dfs(u, label)

    label = 0
    for v in reversed(order):
        if v not in visited:
            reverse_dfs(v, label)
            label += 1

    return components

def solve_2SAT(n_vars, clauses):
    graph = create_implication_graph(n_vars, clauses)
    components = kosaraju_scc(graph)

    assignment = [None] * (n_vars + 1)
    for i in range(1, n_vars + 1):
        if components.get(i, -1) == components.get(-i, -2):
            return False, None  # x and ¬x in the same SCC → UNSAT
        assignment[i] = components.get(i, 0) > components.get(-i, 0)
    return True, assignment[1:]

def print_result(sat, assignment):
    print("  SPLNITEĽNÁ" if sat else "NESPLNITEĽNÁ")
    if sat:
        print("    model:", ["PRAVDA" if v else "NEPRAVDA" for v in assignment])


def draw_implication_graph(n_vars, clauses):
    # Vytvoríme prázdny graf
    G = nx.DiGraph()

    # Vytvoríme implikačný graf
    for a, b in clauses:
        # Každá klauzula (a ∨ b) sa stane dvoma implikáciami: (-a → b) a (-b → a)
        G.add_edge(-a, b)
        G.add_edge(-b, a)

    # Nastavíme pozície uzlov pomocou algoritmu spring layout
    pos = nx.spring_layout(G, seed=42)  # Nastavenie semienka pre reprodukovateľnosť

    # Nakreslíme graf
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold",
            arrows=True)

    # Zobrazíme graf
    plt.title(f"Implikačný graf pre {n_vars} premenných a {len(clauses)} klauzúl")
    plt.show()

if __name__ == "__main__":
    filename = "Vstupy_2SAT.txt"
    formulas = parse_all_formulas(filename)

    for name, (n_vars, clauses) in formulas.items():
        draw_implication_graph(n_vars, clauses)
        print(f"\nVýsledok pre formulu {name}:")

        sat, assignment = solve_2SAT(n_vars, clauses)
        print_result(sat, assignment)