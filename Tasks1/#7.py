#7
def print_even_numbers(n, m):
    # Починаємо із -n
    start = -n
    # Закінчуємо на n
    end = n

    # Проходимо від start до end з кроком m
    for num in range(start, end + 1, m):
        # Перевіряємо, чи є поточне число парним
        if num % 2 == 0:
            print(num)

# Порядковий номер студента у журналі
student_number = 7

# Викликаємо функцію з параметрами -n=10, n=10 та m=student_number
print("Парні числа від -10 до 10 з кроком 7:")
print_even_numbers(10, student_number)