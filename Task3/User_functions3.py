#1. Квадрат або четвертий степінь чисел
def transform_numbers(a, b, c):
    def transform(x):
        return x**2 if x >= 0 else x**4

    return transform(a), transform(b), transform(c)

a, b, c = map(float, input("Введіть три дійсних числа: ").split())
print(transform_numbers(a, b, c))

#2. Визначення найближчої точки до початку координат
def closest_to_origin(x1, y1, x2, y2):
    distance_a = (x1**2 + y1**2)**0.5
    distance_b = (x2**2 + y2**2)**0.5
    return "A" if distance_a < distance_b else "B"

x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())
print(closest_to_origin(x1, y1, x2, y2))

#3. Перевірка існування та прямокутності трикутника
def triangle_angles(angle1, angle2):
    angle3 = 180 - angle1 - angle2
    if angle3 <= 0:
        return "Трикутник не існує"
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "Трикутник є прямокутним"
    else:
        return "Трикутник існує, але не є прямокутним"

angle1, angle2 = map(float, input("Введіть величини двох кутів трикутника: ").split())
print(triangle_angles(angle1, angle2))

#4. Замінити менше число на половину суми, а більше на подвоєний добуток
def replace_numbers(x, y):
    if x < y:
        return (x + y) / 2, x * y * 2
    else:
        return x * y * 2, (x + y) / 2

x, y = map(float, input("Введіть два числа: ").split())
print(replace_numbers(x, y))

#5. Розташування точки на площині
def point_location(x, y):
    if x == 0 and y == 0:
        return "Точка знаходиться в початку координат"
    elif x == 0:
        return "Точка знаходиться на осі Y"
    elif y == 0:
        return "Точка знаходиться на осі X"
    elif x > 0 and y > 0:
        return "Точка знаходиться в першому координатному куті"
    elif x < 0 and y > 0:
        return "Точка знаходиться в другому координатному куті"
    elif x < 0 and y < 0:
        return "Точка знаходиться в третьому координатному куті"
    else:
        return "Точка знаходиться в четвертому координатному куті"

x, y = map(float, input("Введіть координати точки A: ").split())
print(point_location(x, y))

#6. Замінити нерівні числа на більше, рівні на нуль
def replace_or_zero(a, b):
    if a != b:
        larger = max(a, b)
        return larger, larger
    else:
        return 0, 0

a, b = map(int, input("Введіть два цілі числа: ").split())
print(replace_or_zero(a, b))

#7. Підрахувати кількість негативних чисел
def count_negatives(a, b, c):
    return sum(1 for x in [a, b, c] if x < 0)

a, b, c = map(float, input("Введіть три числа: ").split())
print(count_negatives(a, b, c))

#8. Підрахувати кількість додатних чисел
def count_positives(a, b, c):
    return sum(1 for x in [a, b, c] if x > 0)

a, b, c = map(float, input("Введіть три числа: ").split())
print(count_positives(a, b, c))

#9. Підрахувати кількість цілих чисел
def count_integers(a, b, c):
    return sum(1 for x in [a, b, c] if x == int(x))

a, b, c = map(float, input("Введіть три числа: ").split())
print(count_integers(a, b, c))

#10. Визначити дільники числа k
def count_divisors(a, b, c, k):
    return sum(1 for x in [a, b, c] if x % k == 0)

a, b, c, k = map(int, input("Введіть три числа і число k: ").split())
print(count_divisors(a, b, c, k))
