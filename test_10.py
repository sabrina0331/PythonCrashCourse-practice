# print('Tell me two numbers i will divide it for you')
# print("Input 'q' to quit")

# try:
#     while True:
#         first_number = input('Your first number: ')
#         if first_number == 'q':
#             break
#         second_number = input('Your second number: ')
#         if second_number == 'q':
#             break
#         answer = int(first_number)/int(second_number)
#         print(answer)   
#         break
# except ValueError: 
#         print('Please input valid numbers')
# def read_info(filename):
#     try:
#         with open(filename) as fobs:
#             context = fobs.read()
#             each_details = context.split()
#             print('\n'+filename+' : ')
#             for each_detail in each_details:
#                 print(each_detail)
#     except FileNotFoundError:
#         # print('\n'+filename+' is not avaliable,please change to another one')
#         pass
#     # for each_context in context:
#     #     print(each_context)

# filenames = ['dogs.txt','cats.txt','fish.txt']
# for filename in filenames:
#     read_info(filename)

with open('gutenberg.txt') as fobs:
    # count_this = 0
    context = fobs.read()
    count_the = context.lower().count('the')
    print(count_the)