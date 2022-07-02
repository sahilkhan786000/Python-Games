import random


computer_score =0
user_score=0
global user


while True:
    option=['stone' , 'paper', 'scissor']
    a = random.choice(option)
    user_input = input(''' Enter your Option 
    1) stone 
    2) paper
    3) scissor
    
    press q to exit
    Enter Your Value : ''')


    if user_input.isdigit()==True:
        user = int(user_input)

        if option[user-1]==a :
            computer_score, user_score = computer_score, user_score

    elif option[user-1] ==  'stone':
        if a =='paper':
            computer_score=computer_score+1
            print("computer wins")
            print("computer score", computer_score, "user score : ", user_score)
            print(" ")
        elif a=='scissor':
            user_score=user_score+1
            print("computer wins")
            print("computer score", computer_score, "user score : ", user_score)
            print(" ")

    elif option[user - 1] == 'paper':
        if a == 'stone':
                computer_score = computer_score + 1
                print("computer wins")
                print("computer score", computer_score, "user score : ", user_score)
                print(" ")
        elif a == 'scissor':
                user_score = user_score + 1
                print("computer wins")
                print("computer score", computer_score, "user score : ", user_score)
                print(" ")


    elif option[user- 1] == 'scissor':
        if a == 'paper':
            computer_score = computer_score + 1
            print("computer wins")
            print("computer score", computer_score, "user score : ", user_score)
            print(" ")
        elif a == 'stone':
            user_score = user_score + 1
            print("computer wins")
            print("computer score", computer_score, "user score : ", user_score)
            print(" ")

    elif user_input.isdigit() ==False:
        if str(user)=='q':
            print("final score")
            print("")
            print("computer score", computer_score, "user score", user_score)
        else :

             print("invalid input")



