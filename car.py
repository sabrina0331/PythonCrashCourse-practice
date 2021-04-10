class Car():
    def __init__(self,brand,car_model,year):
        self.brand = brand
        self.car_model = car_model
        self.year = year
    def print_cars(self):
        print("This "+ self.brand+ " car's model is "+ self.car_model+ " from "+ self.year)


