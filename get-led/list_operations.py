# Операции со списками
numbers = [1, 2, 3, 4, 5]

# Квадраты чисел
squares = [x**2 for x in numbers]
print("Квадраты чисел:", squares)

# Фильтрация четных чисел
even_numbers = [x for x in numbers if x % 2 == 0]
print("Четные числа:", even_numbers)

# Сумма чисел
total = sum(numbers)
print("Сумма чисел:", total)
