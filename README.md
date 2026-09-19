# ADS – Algorithms and Data Structures

Repository of exercises from the **Algorithms and Data Structures** course. Each folder contains the solution for a given exercise (Python script + input data).

## Exercise overview

### [cv2](cv2/cvicenie2.py)
Finding an optimal route between cities using dynamic programming – minimizing a penalty for deviating from an ideal distance between stops (similar to a billboard-placement problem).

### [cv3](cv3/cv3.py)
The Traveling Salesman Problem (TSP) solved exactly with the **Held-Karp algorithm** (dynamic programming over bitmasks) on city coordinates read from a file.

### [cv4](cv4/cv4.py) and [cv4_reloaded](cv4/cv4_reloaded.py)
A variant of the **knapsack problem** with two constraints at once – maximum weight and maximum volume. `cv4.py` only computes the maximum achievable value, while `cv4_reloaded.py` additionally backtracks to reconstruct which specific items were selected.

### [cv5_a](cv5/cv5_a/cv5_a.py)
Finding the path with the minimum total cost (damage) through a matrix, moving from each row to the next vertically or diagonally – a classic grid DP problem.

### [cv5_b](cv5/cv5_b/cv5_b.py)
Implementation of the **LZW** (Lempel–Ziv–Welch) compression algorithm, including building the dictionary and comparing original vs. compressed data size.

### [cv6](cv6/cv6_a.py) and [cv6_b](cv6/cv6_b.py)
A greedy algorithm for placing charging stations on a graph of cities (a set-cover / dominating-set type problem). `cv6_b.py` extends the solution with grid graph generation, computing the approximation ratio against the theoretical optimum, and visualizing the graph with `networkx`/`matplotlib`.

### [cv10](cv10/cv10.py)
Solving the **2-SAT** problem using an implication graph and strongly connected components (**Kosaraju's algorithm**), including visualization of the implication graph and printing satisfiability/variable assignments for multiple formulas from an input file.
