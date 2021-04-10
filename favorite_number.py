import json

filename= 'favorite_num.json'
def create_num():
    try:
        with open(filename) as fobs:
            fav_num = json.load(fobs)
    except FileNotFoundError:
        fav_num = input('Please tell me your favorite number: ')
        with open(filename,'w') as fobs:
            json.dump(fav_num,fobs)
            print('I will remember next time ')
    else:
        print('I knew your favorite number is : '+fav_num)

create_num()