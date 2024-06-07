#1
# Присвоїти двом змінним будь-які числові значення
a = 5
b = 10

#2
# Чотири складних логічних вирази з оператором and
expr1 = (a > 0 and b > 0)          # True
expr2 = (a < 0 and b < 0)          # False
expr3 = (a < 10 and b == 10)       # True
expr4 = (a > 10 and b > 10)        # False
print(expr1, expr2, expr3, expr4)

#3
# Чотири складних логічних вирази з оператором or
expr5 = (a > 0 or b > 0)           # True
expr6 = (a < 0 or b < 0)           # False
expr7 = (a < 10 or b == 10)        # True
expr8 = (a > 10 or b > 10)         # False
print(expr5, expr6, expr7, expr8)

#4
# Логічні вирази зі змінними рядкового типу
str1 = "Hello"
str2 = "World"

expr9 = (len(str1) > 3 and len(str2) > 3)   # True
expr10 = (str1 == "Hello" and str2 == "Python")  # False
expr11 = (len(str1) < 10 or len(str2) < 10)      # True
expr12 = (str1 == "Python" or str2 == "Java")    # False
print(expr9, expr10, expr11, expr12)

#5
# Програма, яка виводить спеціальне повідомлення
x = 5  # Можна змінювати значення для перевірки

if x > 0:
    print("Значення більше 0")
else:
    print("Значення менше або дорівнює 0")

#6
# Програма з використанням else
x = -3  # Можна змінювати значення для перевірки

if x > 0:
    print(1)
else:
    print(-1)

#7
# Програма за описом
a = 15
b = 10
if a > b:
    c = a - b
elif a < b:
    c = a + b
else:
    c = a
print(c)



