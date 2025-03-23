class Car:
    total_car = 0
    # best way to call it outside - by using class name
    # Car.total_car

    def __init__(self, brand, model):
        #. encapsulation - making brand and model private
        self.__brand = brand
        self.__model = model
        # added double underscore (__) to make it private
        # now we will be able to access it using getter method
        # self.brand = brand
        # self.model = model
        Car.total_car += 1 
        # this will increase on every initialization of object

    #. encapsulation - getter method
    def get_brand(self):
        # return self.brand
        return self.__brand + " !"

    #. encapsulation - getter method without get name
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    #. static method - no need to pass self as argument 
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    # to access object.model - no need to call it as method
    # it will be called as attribute
    # my_car.model
    # instead of my_car.model()
    # getter method
    # this is read only property


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
print(my_tesla.__brand) # private variable can't be accessed directly
print(my_tesla.get_brand()) #. encapsulation - getter method
print(my_tesla.full_name())  #. encapsulation - getter method
print(my_tesla.battery_size)  
print(my_tesla.fuel_type()) #. Polymorphism
# polymorphism - same method name in parent and child class
# but different implementation
# see this - different type of input will decide which method to call


# . isinstance() - to check if object is instance of class
# print(isinstance(my_tesla, Car))  # True
# print(isinstance(my_tesla, ElectricCar))  # True

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")


# print(my_car.general_description())
# print(my_car.model)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

# Multiple inheritance
class ElectricCarTwo(Battery, Engine, Car):
    pass
    # pass is used to avoid writing any code in child class
    

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())