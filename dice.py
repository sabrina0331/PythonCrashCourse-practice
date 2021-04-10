from random import randint 

class Die():
    def __init__(self,sides=6):
        self.sides = sides
    def change_roll_die(self,sides=6):
        self.sides = sides

    def roll_die(self,num):
        self.num = num 
        roll_number = 0
        while roll_number < self.num:
            random_number = randint(1,self.sides)
            print(random_number)
            roll_number += 1 

first_draw = Die()
first_draw.roll_die(10)
# second_draw = Die()
# second_draw.change_roll_die(10)
# second_draw.roll_die(10)