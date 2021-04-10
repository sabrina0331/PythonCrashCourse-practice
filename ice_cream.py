from class_practice import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,name, cuisine,flavor_list):
        super().__init__(name,cuisine)

        self.flavor_list = flavor_list
        

    def describe_ice_creams(self):
        ice_cream_list = []
        while self.flavor_list:
            each_flavor = self.flavor_list.pop()
            ice_cream_list.append(each_flavor)
        print('This restaurant also have ice cream with the following flavor: ')  
        for ice_cream in ice_cream_list:
            print('\t'+ice_cream)
       

restaurant2 = IceCreamStand('Icy City','American',['Chocolate','strawberry','Ube'])
restaurant2.describe_restaurant()
restaurant2.describe_ice_creams()
