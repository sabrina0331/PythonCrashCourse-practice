from name_function import get_formatted_name
print('Enter q to quit')
while True:
    first = input('tell me your first name: ')
    if first == 'q':
        break
    last = input('tell me your last name: ')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print("Formatted name : "+formatted_name) 