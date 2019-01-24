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
        if new_type == 'petrol':
            return PetrolCar(self.model, self.year, self.max_speed)
        elif new_type == 'gas':
            return GasCar(self.model, self.year, self.max_speed)
        elif new_type == 'electron':
            return ElectronCar(self.model, self.year, self.max_speed)
            # subcl =  self.__class__.__subclasses__()
            # print(subcl)
            # for cl in subcl:
            #     print(cl)
            #     if cl.types == subcl:
            #         return cl(self.model, self.year, self.max_speed)

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


class ElectronCar(Car):
    types = 'Electron'

    def __init__(self, model, year, max_speed):
        super().__init__(model, year, max_speed)


class PetrolCar(Car):
    types = 'Petrol'

    def __init__(self, model, year, max_speed):
        super().__init__(model, year, max_speed)


car = Car('BMW', 2018, 300)
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.

print(petrol_car.get_model())  # Returns `BMW`
print(petrol_car.get_year())  # Returns 2018
print(petrol_car.get_max_speed())  # Returns 300

gas_car = car.set_car_type('gas')  # It returns `GasCar` instance.
print(gas_car.__class__)  # <class '__main__.GasCar'>
print(petrol_car.__class__)  # <class '__main__.PetrolCar'>
print(isinstance(petrol_car, PetrolCar))  # True
print(isinstance(gas_car, GasCar))  # True
print(isinstance(gas_car, ElectronCar))  # False
