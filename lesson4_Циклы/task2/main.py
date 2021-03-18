list_numbers = list(range(15, 25))

count_even = 0  # количество четных чисел

for value in list_numbers:  # перебираем все числа
    if value % 2 == 0:
        count_even += 1

print(count_even)
