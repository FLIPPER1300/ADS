import numpy as np

def load_items(filename):
    items = []
    with open(filename, 'r') as file:
        for line in file:
            value, weight, volume = map(int, line.strip().split(','))
            items.append((value, weight, volume))
    return items


def knapsack_3d(items, max_weight, max_volume):
    dp = np.zeros((max_weight + 1, max_volume + 1), dtype=int)

    for value, weight, volume in items:
        for w in range(max_weight, weight - 1, -1):
            for v in range(max_volume, volume - 1, -1):
                dp[w][v] = max(dp[w][v], dp[w - weight][v - volume] + value)

    return dp[max_weight][max_volume]


def main():
    filename = "ADS_cvicenie4DAT.txt"
    items = load_items(filename)
    max_weight = 200
    max_volume = 80

    max_value = knapsack_3d(items, max_weight, max_volume)
    print("Maximálna hodnota starožitností v ruksaku:", max_value)

main()