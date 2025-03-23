class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.brand

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    
    # @staticmethod
    # def general_description():
    #     return "Cars are means of transport"
    
    # @property
    # def model(self):
    #     return self.model
    

#. inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) 
        # Calling parent constructor to set brand and model attributes 
        # no need to set them again in child constructor 
        self.battery_size = battery_size

    #. Polymorphism
    # Overriding fuel_type method of parent class
    def fuel_type():
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.full_name())
print(my_tesla.fuel_type())