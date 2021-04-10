
class Battery():
    def __init__(self, battery_size = 80):
        self.battery_size = battery_size

    def upgrade_battery(self,battery_size):
        self.battery_size = battery_size
        
    def describe_range(self):
        if self.battery_size <=70:
            batter_range = 240
        else:
            batter_range = 270
        message = "This car has a "+ str(self.battery_size)+" -kWh battery."
        message += 'It can go approximately ' + str(batter_range)+' miles on a full charge.'
        print(message)