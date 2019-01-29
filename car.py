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
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def set_car_type(self, new_type):
        try:
            car_class = mapped_classes.get(new_type)
            return car_class(self.model, self.year,self.max_speed)
        except TypeError:
            print("TypeError")

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_max_speed(self):
        return self.max_speed


class GasCar(Car):
    types = 'Gas'

    def __init__(self, model, year, max_speed):
        super().__init__(model, year, max_speed)


class ElectroCar(Car):
    types = 'Electro'

    def __init__(self, model, year, max_speed):
        super().__init__(model, year, max_speed)


class PetrolCar(Car):
    types = 'Petrol'

    def __init__(self, model, year, max_speed):
        super().__init__(model, year, max_speed)


mapped_classes = {"petrol": PetrolCar, "gas": GasCar, "electro": ElectroCar}

car = Car('BMW', 2018, 300)
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.

atribute_error = car.set_car_type('peter') # TypeError

print(petrol_car.__class__)  # <class '__main__.PetrolCar'>
print(petrol_car.get_model())  # Returns `BMW`
print(petrol_car.get_year())  # Returns 2018
print(petrol_car.get_max_speed())  # Returns 300

gas_car = car.set_car_type('gas')  # It returns `GasCar` instance.
print(gas_car.__class__)  # <class '__main__.GasCar'>
print(isinstance(petrol_car, PetrolCar))  # True
print(isinstance(gas_car, GasCar))  # True
print(isinstance(gas_car, ElectroCar))  # False

electro = car.set_car_type('elect') # return "Wrong type!"
