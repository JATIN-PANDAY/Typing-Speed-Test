from time import *
import random as r

def error_find(para_text,user_input):
    error = 0
    for i in range(len(para_text)):
        try:
            if para_text[i] !=user_input[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed(time_s,time_e,user_input):
    time_delay = time_2 - time_1
    time = round(time_delay,2)
    speed = len(user_input)/time
    return round(speed)
    

while True:
    a = input('Are  your Ready for test : Yes/No :')
    if a =='yes':
        paragraph = ['Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit doloribus et consectetur.' , 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eius quisquam dolor exercitationem adipisci earum beatae architecto et fuga aliquam quidem quia dolores, velit enim ex odit est voluptas aliquid sint!' , 'What is your name .']
        random_para = r.choice(paragraph)
        print(random_para)
        print()
        time_1 = time()
        print('--- Start Typing --- ')
        print()

        user_input=input("Type here :")

        time_2 = time()

        print('Speed :',speed(time_2,time_1,user_input) , 'Words/sec')
        print(" Errors : ",error_find(random_para,user_input))
    elif a =='no':
        print('Thank you')
    else:
        print('Wrong input')


