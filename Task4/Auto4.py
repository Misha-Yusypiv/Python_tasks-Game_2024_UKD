class Transport:
    def get_type(self):
        raise NotImplementedError("This method should be overridden in derived classes")
        # Оголошуємо метод, який повинні перевизначити у похідних класах.

class Land(Transport):
    def get_type(self):
        return "Land Transport"
        # Перевизначення методу get_type для класу Land, який повертає "Land Transport".

class Water(Transport):
    def get_type(self):
        return "Water Transport"
        # Перевизначення методу get_type для класу Water, який повертає "Water Transport".

class Auto(Land):
    pass
    # Клас Auto успадковується від Land, але не має власних методів.

class Boat(Water):
    pass
    # Клас Boat успадковується від Water, але не має власних методів.

class Gibrid(Land, Water):
    pass
    # Клас Gibrid успадковується від Land і Water, але не має власних методів.

# Створення об'єктів
land = Land()  # Створюємо об'єкт класу Land.
water = Water()  # Створюємо об'єкт класу Water.
auto = Auto()  # Створюємо об'єкт класу Auto.
boat = Boat()  # Створюємо об'єкт класу Boat.
gibrid = Gibrid()  # Створюємо об'єкт класу Gibrid.

# Виклик обробників для класів Boat і Gibrid
print("Boat:", boat.get_type())  # Виведе "Water Transport" (унаслідований від класу Water).
print("Gibrid:", gibrid.get_type())  # Виведе "Land Transport" (унаслідований від класу Land).
