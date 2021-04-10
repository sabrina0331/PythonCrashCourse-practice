from car import Car
from battery import Battery

class ElectricCar(Car):
    def __init__(self,brand,car_model,year):
        super().__init__(brand,car_model,year) 
        self.battery = Battery()

    
