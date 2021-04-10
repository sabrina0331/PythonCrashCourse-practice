# import json

# def check_user_name():
#     filename = 'username.json'
#     try: 
#         with open(filename) as fobs:
#             user_name = json.load(fobs)
#     except:
#         return None
#     else:
#         return user_name
# def store_new_user():
#     user_name = input('What is your name: ')
#     filename = 'username.json'
#     with open(filename, 'w') as fobs:
#         json.dump(user_name,fobs)
#     return user_name
    

# def greet_user():
#     user_name = check_user_name()
#     if user_name:
#         print('Welcome back '+ user_name)
#     else:
#         user_name = store_new_user()
#         print('We will rememeber you when you come back, '+user_name+" !")
       

# greet_user()

#Read json user_name
import json

def check_user_name():
    filename = 'user_infos.json'
    try: 
        with open(filename) as all_infos:
           username = json.load(all_infos)
    except:
        return None
    else:
        return username
    
def create_new_user():
    filename ='user_infos.json'
    username = input('Please tell me your name: ')
    with open(filename,'w') as all_infos:
        # context = all_infos.write(username)        
       json.dump(username,all_infos)
    print('I will remember your name next time '+ username)
    return username

def greet_user():
    filename = 'user_infos.json'
    username = check_user_name()
    if username:
        logged_info = input('Is '+username+' your name?')
        if logged_info == 'yes':
            print('Welcome back '+ username)
        elif logged_info == 'no':
            username = create_new_user()
    else:
        username = create_new_user()
        print('I will remember your name next time '+ username)

greet_user()        