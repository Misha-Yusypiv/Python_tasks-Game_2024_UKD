#9
# Виведення ряду Фібоначчі
a, b = 0, 1
count = 0
while count < 20:
    if count >= 5:
        print(a)
    a, b = b, a + b
    count += 1

# Виведення парних чисел від 0 до 20
i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# Виведення кожного третього числа від -1 до -21
i = -1
count = 0
while i >= -21:
    if count % 3 == 0:
        print(i)
    i -= 1
    count += 1

#10
# Таблиця квадратів перших п'яти цілих додатних непарних чисел
for i in range(1, 10, 2):
    print(f"{i}^2 = {i**2}")
