def knapsack(filename):
    # Načítame dáta zo súboru
    items = []
    with open(filename, 'r') as file:
        for line in file:
            value, weight, volume = map(int, line.strip().split(','))
            items.append((value, weight, volume))

    n = len(items)  # počet položiek
    max_weight = 200  # maximálna hmotnosť
    max_volume = 80  # maximálny objem

    # Inicializujeme 3D pole pre dynamické programovanie
    backpack = [[[0] * (max_volume + 1) for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # Dynamické programovanie
    for i in range(1, n + 1):
        value, weight, volume = items[i - 1]  # Získame hodnotu, hmotnosť a objem položky
        for w in range(max_weight + 1):  # Pre každú možnú hmotnosť
            for v in range(max_volume + 1):  # Pre každý možný objem
                if w >= weight and v >= volume:
                    # Ak sa zmestí do ruksaku, môžeme ju pridať
                    backpack[i][w][v] = max(backpack[i - 1][w][v],
                                            backpack[i - 1][w - weight][v - volume] + value)
                else:
                    # Inak nevieme túto položku pridať
                    backpack[i][w][v] = backpack[i - 1][w][v]

    # Zistenie položiek v ruksaku
    w = max_weight
    v = max_volume
    selected_items = []

    # Prechádzanie spätne cez pole a zisťovanie, ktoré položky boli pridané
    for i in range(n, 0, -1):
        if backpack[i][w][v] != backpack[i - 1][w][v]:
            # Ak sa hodnota zmenila, znamená to, že položka i bola pridaná
            selected_items.append(i - 1)  # Ukladáme index položky
            w -= items[i - 1][1]  # Znižujeme hmotnosť
            v -= items[i - 1][2]  # Znižujeme objem

    # Najväčšia možná cena
    return backpack[n][max_weight][max_volume], sorted(selected_items)


filename = 'ADS_cvicenie4DAT.txt'
result, selected_items = knapsack(filename)
print(f"Najväčšia cena, ktorú môžeme dosiahnuť: {result}")
print(f"Indexy vybraných predmetov: {selected_items}")
