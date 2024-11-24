def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}
        for i, string in enumerate(strings):
            file.write(string + '\n')
            start_byte = file.tell()
            strings_positions[i, start_byte] = string
        return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
     ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)