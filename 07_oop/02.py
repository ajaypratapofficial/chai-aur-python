class Car:
    total_car = 0  # Class variable (shared by all instances)

    def __init__(self, brand, model, color):
        # Instance variables (unique to each object)
        self.__brand = brand
        self.__model = model
        self.color = color
        Car.total_car += 1  # Accessing class variable using class name

    # Instance method to access private variable __brand
    def get_brand(self):
        return self.__brand

    # Instance method to access private variable __model
    def get_model(self):
        return self.__model

    # Instance method that returns full car details
    def get_details(self):
        # Accessing instance variables and instance methods using 'self'
        return f"Brand: {self.get_brand()}, Model: {self.get_model()}, Color: {self.color}"

    # Instance method to update color
    def update_color(self, new_color):
        self.color = new_color

    # Static method (doesn't need 'self')
    @staticmethod
    def show_total_cars():
        return f"Total cars created: {Car.total_car}"

# ---------------------------------
# Creating Objects (Instances)
car1 = Car("Toyota", "Camry", "Red")
car2 = Car("Honda", "Civic", "Blue")

# Accessing data using instance methods
print(car1.get_details())  # Output: Brand: Toyota, Model: Camry, Color: Red
print(car2.get_details())  # Output: Brand: Honda, Model: Civic, Color: Blue

# Updating color using instance method
car1.update_color("Black")
print(car1.get_details())  # Updated color

# Accessing class variable (preferred way)
print(Car.show_total_cars())  # Output: Total cars created: 2
# 2 because we have created 2 objects of Car class
