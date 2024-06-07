class Transport:
    def get_type(self):
        raise NotImplementedError("This method should be overridden in derived classes")

class Land(Transport):
    def get_type(self):
        return "Land Transport"

class Water(Transport):
    def get_type(self):
        return "Water Transport"

class Auto(Land):
    pass

class Boat(Water):
    pass

class Gibrid(Land, Water):
    pass

# Створення об'єктів
land = Land()
water = Water()
auto = Auto()
boat = Boat()
gibrid = Gibrid()

# Виклик обробників для класів Boat і Gibrid
print("Boat:", boat.get_type())  # Виведе "Water Transport"
print("Gibrid:", gibrid.get_type())  # Виведе "Land Transport"
