class Restaurant():
    def __init__(self,name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
        
    def describe_restaurant(self):
        print("Restaurant name: "+ self.name+" ,cuisine_type: "+self.cuisine)

    def open_restaurant(self):
        print('This restaurant is oening..')

    def update_visits(self,num_people):
        self.number_served = num_people

    def increment_number_served(self,num):
        self.number_served += num

    def num_visited(self):
        print('There are '+ str(self.number_served) +" people have visited")

# class User():
#     def __init__(self,first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attemps = 0

#     def describe_user(self):
#         print('Full name: '+ self.first_name +" "+ self.last_name)
#         print('User has logged '+ str(self.login_attemps) +" attemps.")
    
#     def update_attemps(self,attemps):
#         self.login_attemps = attemps

#     def increment_login_attemps(self):
#         self.login_attemps += 1
#     def reset_login_attemps(self):
#         self.login_attemps = 0

# class Privileges():
#     def __init__(self,privileges_list=['can delete members','can add memebers']):
#         self.privileges_list = privileges_list
    
#     def show_privileges(self):
#         for privilege in self.privileges_list:
#             print(privilege)

# class Admin(User):
#     def __init__(self,first_name, last_name):
#         super().__init__(first_name,last_name)
#         self.privileges_list = Privileges()
#         print("Admin: "+self.first_name+ self.last_name+ " ")
    
    

# user1 = Admin('XY','Z')
# user1.privileges_list.show_privileges()
# class Car():
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     def get_car_info(self):
#         full_info = self.brand+" "+ self.model + " " + self.year
#         return full_info.title()

# class Battery():
#     def __init__(self,battery_consumed=75):
#         self.battery_consumed = battery_consumed

#     def describe_battery(self):
#         print('This car consumed '+ str(self.battery_consumed)+' battery..')
#     def get_range(self):
#         if self.battery_consumed >= 70:
#             range = 240
#         if self.battery_consumed  == 85:
#             range = 270
#         print('This car can go approximately '+ str(range))
#     def upgrade_battery(self):
#         if self.battery_consumed != 85:
#             self.battery_consumed = 85
#         print('Your battery consumed 85')

# class ElectricCar(Car):
#     def __init__(self,brand, model, year):
#         super().__init__(brand,model,year)
#         self.battery = Battery()
    
#     def update_battery(self,times):
#         self.battery = times

# # car1 = Car('Fiat','500L','2001')
# # print(car1.get_car_info())
# car2 = ElectricCar('Tesla','Model X','2009')
# print(car2.get_car_info())
# car2.battery.describe_battery()
# car2.battery.get_range()
# car2.battery.upgrade_battery()
# # car2.update_battery(50)
# # car2.describe_battery()

