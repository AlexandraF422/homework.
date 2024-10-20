data_structure = [
 [1, 2, 3],
 {'a': 4, 'b': 5},
 (6, {'cube': 7, 'drum': 8}),
 "Hello",
 ((), [{(2, 'Urban', ('Urban2', 35))}]),
]

def calculate_structure_sum(data_structure):
    total = 0
    for item in data_structure:
        if isinstance(item, (int, float)):
            total += item
        elif isinstance(item, str):
            total += len(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, (int, float)):
                    total += value
                elif isinstance(value, str):
                    total += len(value)
                elif isinstance(item, tuple):
                    for subitem in item:
                        if isinstance(subitem, (int, float)):
                            total += subitem
                        elif isinstance(subitem, str):
                            total += len(subitem)
                        elif isinstance(item, list):
                            for sublist in item:
                                if isinstance(sublist, (int, float)):
                                    total += sublist
                                elif isinstance(sublist, str):
                                    total += len(sublist)
                                elif isinstance(item, set):
                                    for value in item:
                                        if isinstance(value, (int, float)):
                                            total += value
                                        elif isinstance(value, str):
                                            total += len(value)

    return total


result = calculate_structure_sum(data_structure)
print(result) # => 99