"""
Improve previous task to make it possible to run code in this way:

car = Car('BMW', 2018, 300)
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
petrol_car.get_model()  # Returns `BMW`
petrol_car.get_year()  # Returns 2018
petrol_car.get_max_speed()  # Returns 300

gas_car = car.set_car_type('gas')  # It returns `GasCar` instance.

"""


class Car:
    def __init__(self, model, year, max_speed, ):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def get_car_type(self):
        return self.types.title()

    def change_type(self, new_types):
        self.types = new_types

    def set_car_type(self, types):
        self.types = types
        return self

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_max_speed(self):
        return self.max_speed


car = Car('BMW', 2018, 300)
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.

print(petrol_car.get_car_type())
print(petrol_car.get_model())  # Returns `BMW`
print(petrol_car.get_year())  # Returns 2018
print(petrol_car.get_max_speed())  # Returns 300

gas_car = car.set_car_type('gas')  # It returns `GasCar` instance.
print(gas_car.get_car_type())
