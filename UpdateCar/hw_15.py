class Car:
    instance = None
    def __init__(self,  model, year, max_speed, ):
        self.model = model
        self.year = year
        self.max_speed = max_speed
    def get_car_type(self):
        return self.type

    def change_type(self, types):
        self.type = types

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_max_speed(self):
        return self.max_speed

    def set_car_type(self,t):
        self.instance = t
        return self.instance
car = Car( 'BMW', 2018, 280)

petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
# print(petrol_car.get_model())# Returns `BMW`
# print(petrol_car.get_year()  )# Returns 2018
# print(petrol_car.get_max_speed()) # Returns 300

