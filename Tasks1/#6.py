#6
def check_sequence(string):
    length = len(string)
    i = 0
    
    while i < length:
        # Якщо поточний символ - '0'
        if string[i] == '0':
            # Перевіряємо, чи наступні символи у рядку - '1'
            for j in range(i+1, length):
                # Якщо знайдено послідовність '1' такої ж довжини
                if string[j] == '1' and j - i == i + 1:
                    break
            else:
                # Якщо послідовність '1' не знайдено
                return False
        # Якщо поточний символ - '1'
        else:
            # Перевіряємо, чи наступні символи у рядку - '0'
            for j in range(i+1, length):
                # Якщо знайдено послідовність '0' такої ж довжини
                if string[j] == '0' and j - i == i + 1:
                    break
            else:
                # Якщо послідовність '0' не знайдено
                return False
        
        # Переходимо до наступної пари послідовностей
        i += i + 1
    
    # Якщо умова виконується для кожної пари, повертаємо True
    return True

# Послідовності для перевірки
sequences = ["01010101", "00011100011"]

# Перевірка кожної послідовності
for sequence in sequences:
    result = check_sequence(sequence)
    print(f"Послідовність: {sequence}, Результат: {result}")
