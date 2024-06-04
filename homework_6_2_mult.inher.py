class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self):
        return 150

class Nissan(Vehicle, Car):
    vehicle_type = "car"
    price = 1200000

    def horse_powers(self):
        return 200

# Создание экземпляра класса Nissan
nissan1 = Nissan()

# Вывод свойств экземпляра
print(f"Vehicle Type: {nissan1.vehicle_type}")
print(f"Price: {nissan1.price}")
print(f"Horse Powers: {nissan1.horse_powers()}")