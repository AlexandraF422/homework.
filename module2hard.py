result = []
n = int(input("Число "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if n % (i +j) == 0 and j > i:
            result.append((i))
            result.append(j)
result1 = ''
for p in result:
    result1 += str(p)
print('Шифр: ', result1)