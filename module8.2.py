def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            num = float(num)
            result += num

        except (TypeError, ValueError):
            incorrect_data += 1

    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        sum_of_numbers, count_of_incorrect = personal_sum(numbers)
        if count_of_incorrect == 0:
            if isinstance(sum_of_numbers, float) and len(numbers) > 0:
                return sum_of_numbers / len(numbers)
        else:
            return 0
    except (TypeError, ValueError) as e:
        print(f'В numbers записан некорректный тип данных')
        return None






print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
