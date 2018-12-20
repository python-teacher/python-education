"""
Define a base class for auto.
Base class should contain:
Fields:

type (gas, electron, petrol)
model
year
max speed.
Method:
get car type
Define child classes for each type of car.
get_car_type method should return just an appropriate type of car.

Create a general class which should work in this way:

car = Car('gas', 'BMW', 2018, 280)
print(car.get_car_type()) # prints Gas
car.change_type('petrol')
print(car.get_car_type()) # prints Petrol.
"""


class Car:
    def __init__(self, types, model, year, max_speed, ):
        self.types = types
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def get_car_type(self):
        return self.types.title()

    def change_type(self, new_types):
        self.types = new_types


car = Car('gas', 'BMW', 2018, 280)
print(car.get_car_type())  # prints `Gas`
car.change_type('petrol')
print(car.get_car_type())  # prints `Petrol`.
