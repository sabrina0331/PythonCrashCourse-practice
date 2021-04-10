# filename = 'pi_digits.txt' 
with open('pi_digits.txt') as fob:
    info_string = ''
    for information in fob:
        info_string += information
    # print(info_string)
    string = info_string.replace('Python','C')
    print(string)