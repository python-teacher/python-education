"""
Improve previous task to make it possible to run code in this way:

car = Car('BMW', 2018, 300)
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
petrol_car.get_model()  # Returns `BMW`
petrol_car.get_year()  # Returns 2018
petrol_car.get_max_speed()  # Returns 300

gas_car = car.set_car_type('gas')  # It returns `GasCar` instance.

"""