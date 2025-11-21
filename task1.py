print("Hello, World!")


def factorial(n):
    if n < 0:
        return None 
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result




import random

numbers = random.randint(100)

max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

print("Максимальный элемент:", max_value)
