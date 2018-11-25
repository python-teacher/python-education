class Car:
    def __init__(self, type, model, year, max_speed, ):
        self.type = type
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def get_car_type(self):
        # car = str(self.type)+' ' + str(self.model)+' '+ str(self.year) +' '+ str(self.max_speed)
        return self.type
    def change_type(self,types):
        self.type = types

car = Car('gas', 'BMW', 2018, 280)
print(car.get_car_type())  # prints `Gas`
car.change_type('petrol')
print(car.get_car_type())  # prints `Petrol`.
car.change_type('electrical')
print(car.get_car_type())  # prints `Electrical`.
