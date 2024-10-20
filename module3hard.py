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
        elif isinstance(item, (list, tuple, set)):
            total += calculate_structure_sum(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, (int, float)):
                    total += value
                elif isinstance(value, str):
                    total += len(value)
                elif isinstance(value, (list, tuple, set)):
                    total += calculate_structure_sum(value)
    return total

    


result = calculate_structure_sum(data_structure)
print(result) # => 99
