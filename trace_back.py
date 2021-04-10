# print('Tell me two number, I will divide them for you')
# print('type p to quit')
# while True:
#     first_num = input('Please tell me your first number: ')
#     if first_num == 'q':
#         break
#     second_num = input("Please tell me your second number: ")
#     if second_num == 'q':
#         break
#     try:
#         answer = int(first_num)/int(second_num)
#     except:
#         print('You cannot divide 0')
#     else:
#         print(answer)
def count_words(filename):
    try: 
        with open(filename) as fobs:
            contents = fobs.read()
    except FileNotFoundError:
        # print('Sorry '+ filename+' does not exisit please pick another one')
        pass
        # with open(filename,'w') as fobs:
        #     fobs.write()
        
    else:
        words = contents.split()
        # print(contents.split())
        number_of_words = len(words)
        print('The file '+filename+' has about '+ str(number_of_words)+' words.')
filenames = ['gmat.txt','alice.txt','dog.txt']
for filename in filenames:
    count_words(filename)