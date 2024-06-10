class LibraryUser:
    # Конструктор класу LibraryUser, який ініціалізує об'єкт користувача бібліотеки з основними атрибутами
    def __init__(self, user_id, last_name, first_name, group, course):
        self.user_id = user_id  # Ідентифікаційний номер користувача
        self.last_name = last_name  # Прізвище користувача
        self.first_name = first_name  # Ім'я користувача
        self.group = group  # Група, до якої належить користувач
        self.course = course  # Курс користувача
        self.borrowed_books = []  # Список книг, які взяв користувач
        self.returned_books = []  # Список книг, які повернув користувач

    # Метод для додавання книги до списку боргованих книг
    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)  # Додаємо книгу до списку боргованих книг
        print(f"Книга '{book_title}' успішно додана до списку боргу.")  # Виводимо повідомлення про успішне додавання

    # Метод для повернення книги зі списку боргованих книг
    def return_book(self, book_title):
        if book_title in self.borrowed_books:  # Перевіряємо, чи книга є в списку боргованих книг
            self.borrowed_books.remove(book_title)  # Видаляємо книгу зі списку боргованих книг
            self.returned_books.append(book_title)  # Додаємо книгу до списку повернутих книг
            print(f"Книга '{book_title}' успішно повернена.")  # Виводимо повідомлення про успішне повернення
        else:
            print(f"Книга '{book_title}' не знайдена у списку боргу.")  # Виводимо повідомлення, якщо книга не знайдена

    # Метод для виведення інформації про користувача
    def print_user_info(self):
        print("Карта читача:")  # Заголовок карти читача
        print(f"ID: {self.user_id}")  # Виводимо ідентифікаційний номер користувача
        print(f"Прізвище: {self.last_name}")  # Виводимо прізвище користувача
        print(f"Ім’я: {self.first_name}")  # Виводимо ім'я користувача
        print(f"Група: {self.group}")  # Виводимо групу користувача
        print(f"Курс: {self.course}")  # Виводимо курс користувача
        print("Список боргованих книг:", self.borrowed_books)  # Виводимо список боргованих книг
        print("Список повернутих книг:", self.returned_books)  # Виводимо список повернутих книг

# Створення об'єкта користувача
user_data = {
    "user_id": 1,  # Ідентифікаційний номер користувача
    "last_name": "Юсипів",  # Прізвище користувача
    "first_name": "Михайло",  # Ім'я користувача
    "group": "ІПЗс-21",  # Група користувача
    "course": 3  # Курс користувача
}
user = LibraryUser(**user_data)  # Створюємо об'єкт користувача з використанням розпакування словника

# Виведення інформації про користувача при запуску програми
user.print_user_info()  # Викликаємо метод для виведення інформації про користувача

# Головний цикл програми
while True:
    print("\nМеню:")  # Виводимо меню програми
    print("1. Вивести карту читача")  # Опція для виведення карти читача
    print("2. Взяти книгу у борг")  # Опція для взяття книги у борг
    print("3. Повернути книгу")  # Опція для повернення книги
    print("0. Вийти з програми")  # Опція для виходу з програми

    choice = input("Виберіть опцію: ")  # Запитуємо у користувача вибір опції

    if choice == "1":
        user.print_user_info()  # Викликаємо метод для виведення інформації про користувача
    elif choice == "2":
        book_title = input("Введіть назву книги, яку бажаєте взяти у борг: ")  # Запитуємо назву книги у користувача
        user.borrow_book(book_title)  # Викликаємо метод для додавання книги до списку боргованих
    elif choice == "3":
        if user.borrowed_books:  # Перевіряємо, чи є книги у боргу
            print("Список книг у боргу:", user.borrowed_books)  # Виводимо список боргованих книг
            book_title = input("Введіть назву книги, яку бажаєте повернути: ")  # Запитуємо назву книги у користувача
            user.return_book(book_title)  # Викликаємо метод для повернення книги
        else:
            print("Ви не маєте жодної книги у боргу.")  # Виводимо повідомлення, якщо немає боргованих книг
    elif choice == "0":
        print("Дякую за користування програмою!")  # Виводимо повідомлення про завершення роботи
        break  # Виходимо з циклу, завершуючи програму
    else:
        print("Невірний вибір. Спробуйте ще раз.")  # Виводимо повідомлення про невірний вибір опції
