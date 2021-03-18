list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3]

first_element = list_[0]
count = 0

for value in list_:  # перебираем числа, все кроме первого
    if value > first_element:
        count += 1

print(count)
