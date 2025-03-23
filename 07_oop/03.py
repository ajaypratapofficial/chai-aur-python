class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # self is accessing instance variable of parent

    def show_brand(self):
        return f"Brand: {self.brand}"

car = Vehicle("Toyota")
print(car.show_brand())  # Output: Brand: Toyota

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calling parent constructor
        self.model = model       # self refers to child instance now

    def show_details(self):
        # self can access both parent and child attributes
        return f"{self.show_brand()}, Model: {self.model}"


# Create instance of Car (child class)
my_car = Car("Toyota", "Corolla")

# Accessing methods
print(my_car.show_details())  # Output: Brand: Toyota, Model: Corolla
