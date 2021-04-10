filename = 'guest_book.txt'

active = True
all_info = ''
while active:
    
    guest_infos = input('Please enter your name: ')
    if guest_infos == 'quit':
        break
    print('Thank you for your cooperation!')
    all_info += '\n' +guest_infos
    store_information = all_info
    
with open(filename, 'w') as fobs:
    fobs.write(store_information)

