#4
def calculate_value(n):
    nn = n * 10 + n
    nnn = n * 100 + nn
    return n + nn + nnn

# Задане значення n
n = 5

# Обчислення та вивід результату
result = calculate_value(n)
print("Результат обчислення:", result)