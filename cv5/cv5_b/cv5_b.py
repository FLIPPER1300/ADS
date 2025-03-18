def lzw_compress(input_file):
    with open(input_file, 'r', encoding='ascii') as f:
        data = f.read().replace("\n", "")

    original_size = len(data)  # Počet bajtov v pôvodnom súbore

    # Inicializácia slovníka
    dictionary = {chr(i): i for i in range(128)}  # Prvých 128 ASCII znakov
    dict_size = 128
    max_dict_size = 256

    compressed_data = []
    prefix = ""

    for char in data:
        new_prefix = prefix + char
        if new_prefix in dictionary:
            prefix = new_prefix
        else:
            compressed_data.append(dictionary[prefix])
            if dict_size < max_dict_size:
                dictionary[new_prefix] = dict_size
                dict_size += 1
            prefix = char

    if prefix:
        compressed_data.append(dictionary[prefix])

    compressed_size = len(compressed_data)

    # Výpis výsledkov
    print(f"Pôvodná veľkosť: {original_size} bajtov")
    print(f"Kompresovaná veľkosť: {compressed_size} bajtov")
    print("Kódovacia tabuľka:")
    for key, value in dictionary.items():
        print(f"{repr(key)} -> {value}")

    return compressed_data


# Testovanie na súbore udaje5_2a.txt
compressed_output = lzw_compress("udaje5_2a.txt")
