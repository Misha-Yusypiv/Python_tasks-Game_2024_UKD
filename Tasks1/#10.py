class LibraryUser:
    def __init__(self, user_id, last_name, first_name, group, course):
        self.user_id = user_id
        self.last_name = last_name
        self.first_name = first_name
        self.group = group
        self.course = course
        self.borrowed_books = []
        self.returned_books = []

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)
        print(f"Книга '{book_title}' успішно додана до списку боргу.")

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            self.returned_books.append(book_title)
            print(f"Книга '{book_title}' успішно повернена.")
        else:
            print(f"Книга '{book_title}' не знайдена у списку боргу.")

    def print_user_info(self):
        print("Карта читача:")
        print(f"ID: {self.user_id}")
        print(f"Прізвище: {self.last_name}")
        print(f"Ім’я: {self.first_name}")
        print(f"Група: {self.group}")
        print(f"Курс: {self.course}")
        print("Список боргованих книг:", self.borrowed_books)
        print("Список повернутих книг:", self.returned_books)


# Створення об'єкта користувача
user_data = {
    "user_id": 1,
    "last_name": "Юсипів",
    "first_name": "Михайло",
    "group": "ІПЗс-21",
    "course": 3
}
user = LibraryUser(**user_data)

# Головний цикл програми
while True:
    print("\nМеню:")
    print("1. Вивести карту читача")
    print("2. Взяти книгу у борг")
    print("3. Повернути книгу")
    print("0. Вийти з програми")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        user.print_user_info()
    elif choice == "2":
        book_title = input("Введіть назву книги, яку бажаєте взяти у борг: ")
        user.borrow_book(book_title)
    elif choice == "3":
        if user.borrowed_books:
            print("Список книг у боргу:", user.borrowed_books)
            book_title = input("Введіть назву книги, яку бажаєте повернути: ")
            user.return_book(book_title)
        else:
            print("Ви не маєте жодної книги у боргу.")
    elif choice == "0":
        print("Дякую за користування програмою!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
