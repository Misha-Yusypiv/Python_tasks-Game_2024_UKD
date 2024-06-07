#8
import math

def combinations_count(m):
    if m > 25:
        return "Помилка: кількість комірок перевищує кількість доступних символів."
    else:
        return math.prod(range(25, 25 - m, -1))

student_number = 8  # Порядковий номер студента у журналі
m = student_number
result = combinations_count(m)
print(f"Кількість можливих комбінацій для студента з номером {student_number}: {result}")