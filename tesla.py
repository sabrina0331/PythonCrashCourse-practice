from car import Car
from battery import Battery
from electric_car import ElectricCar

teslaCar = ElectricCar('Tesla','Model X','2021')
teslaCar.battery.upgrade_battery(70)
teslaCar.battery.describe_range()