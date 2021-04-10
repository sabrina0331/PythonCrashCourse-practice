filename = 'guest.txt'
user_name = input('Please enter your name: ')

with open(filename,'w') as information:
    information.write(user_name)