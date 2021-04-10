# def display_message():
#     print("Chapter 8: function")


# display_message()
# def favorite_book(title):
#     print('One of my favorite books is '+ title)

# favorite_book('Gmat Official guide')

# def describe_pet(animal_name,animal_type="cat"):
#     print('I have a '+ animal_type+" its name is "+ animal_name)

# describe_pet(animal_name='Mimi')
# describe_pet(animal_name='Harry', animal_type='Hamister')
# def describe_pet(animal_type="cat",animal_name):
#     print('I have a '+ animal_type+" its name is "+ animal_name)

# describe_pet(animal_name='Mimi')
# def make_shirt(size='L',printed='I love Python'):
#     print('Size is :' +size +' , color printed is '+printed)

# make_shirt()
# make_shirt(size='M')
# make_shirt('S','Sunflower')
# def describe_city(city,country):
#     print(city+', '+ country)

# describe_city('Shanghai','China')
# describe_city('Beijing','China')
# describe_city('Tokyo','Japan')
# # def build_name(fn,ln,age=''):
#     person = {
#         'fn': fn,
#         'ln': ln
#     }
#     if age:
#         person['age'] = age
#     print(person)
#     return person

# build_name('Chrals','Dickens','55')
# def make_album(singer,album_name):
#     infos = {}
#     infos['singer_name'] = singer_name
#     infos['album'] = album
#     return infos

    
# while True:
#     print('Who is your favorite singer: ')
#     print('Press q to quit this game..')
#     singer_name = input('Singer name: ')
#     if singer_name == "q":
#         break
#     album = input('Album name: ')
#     if album == 'q':
#         break
#     new_data = make_album(singer_name,album)
#     print(new_data)
# def greeting(names):
#     for name in names:
#         print('Hello '+ name)
    
# username = ['Ginna','Jenny','Col']
# greeting(username)    
# unprinted_designs = ['Iphone','One Plus','Surface']
# printed_designs = []
# while unprinted_designs:
#     confirmed = unprinted_designs.pop()
#     printed_designs.append(confirmed)
#     print("Printing: "+ confirmed)
# print('No more unprinted')
# for printed_models in printed_designs:
#     print(printed_models)

# def confirm_printed(unprinted_designs, printed_designs):
#     while unprinted_designs:
#         confirmed = unprinted_designs.pop()
#         printed_designs.append(confirmed)
#         print("Printing: "+ confirmed)

# def repeat_printing(confirmed):
#     for printed_models in confirmed:
#         print(printed_models)
    
# unprinted_designs = ['Iphone','One Plus','Surface']
# printed_designs = []
# confirm_printed(unprinted_designs[:],printed_designs)
# repeat_printing(printed_designs)
# print(unprinted_designs)

# def make_great(magicians):
#     while magicians:
#         confirmed = magicians.pop()
#         new_array.append('The Great '+ confirmed)   
#     return new_array

# def show_magicians(new_array):
#     for name in new_array:
#         print(name)


# magicians = ['David','Carl','Rick','Gel']
# new_array = []
# make_great(magicians[:])
# show_magicians(new_array)
# print(magicians)

# def user_info(fn,ln,**other_info):
#     profile =  {}
#     profile['fn']= fn
#     profile['ln'] = ln
#     for info,val in other_info.items():
#         profile[info] = val
#     print(profile)

# user_info(fn='Abraham', ln='Linkin', location='US', occupation='President')
# user_info(fn='Taylor', ln='Swift',occupation='Singer')
# def build_sandwich(*toppings):
#     for top in toppings:
#         print('Added '+ top +" in your sandwich")

# build_sandwich('tomatoes','Chocolate')
def build_car_info(car_brand,car_type,**other_infos):
    all_user_info = {}
    all_user_info['car_brand']= car_brand
    all_user_info['car_type'] = car_type
    for other_info,details in other_infos.items():
        all_user_info[other_info] = details
    return(all_user_info)

# car = build_car_info(car_brand='Subaru',car_type='outback',color='silver',tow_package=True)
# print(car)
# car1 = build_car_info(car_brand='Fiat',car_type='sedan',color='red',tow_package=False)
# print(car1)

