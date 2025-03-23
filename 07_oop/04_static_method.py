
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @staticmethod
    def multiply(a, b):
        return a * b

calc = Calculator(10, 5)

# Instance method - uses self
print(calc.add())            # Output: 15

# Static method - no self required
print(Calculator.multiply(3, 4))  # Output: 12

print(calc.multiply(6, 7))  #! Still works, but not preferred


# ---------------------------------

class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

    @staticmethod
    def show_welcome_message():
        print("Welcome to Car Showroom!")  
        # No need for instance or class data

    @staticmethod
    def add_numbers(a, b):
        return a + b


# Usage
Car.show_welcome_message()  # Recommended way
c1 = Car("Toyota", "Camry")
c2 = Car("Honda", "Civic")

c1.display_info()
print(Car.add_numbers(10, 20))  # 30

