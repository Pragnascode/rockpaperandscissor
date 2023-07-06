import random
exit=False
user_pts=0
comp_pts=0

while exit == False:
    options = ["rock","paper","scissors"]
    user_input = input("choose rock,paper,scissors or exit")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("game ended")
        print("you won total score of "+ str(user_pts) + "" + "computer won total score of " + str(comp_pts))
        if user_pts > comp_pts:
            print("you won the game!")
        elif user_input == comp_pts :
            print("its a tie game, we both won !!")
        else :
            print("computer won the game!")
        exit= True
    if user_input == "rock":
        if computer_input == "rock":
            print("your input is rock")
            print("my input is rock")
            print("its a tie")
        elif computer_input == "paper":
            print("your input is rock")
            print("my input is paper")
            print("i win")
            comp_pts += 1
        elif computer_input == "scissor":
            print("your input is rock")
            print("my input is scissor")
            print("you win")
            user_pts += 1

    if user_input == "paper" :
        if computer_input == "rock":
            print("your input is paper")
            print("my input is rock")
            print("you win!")
            user_pts += 1
        elif computer_input == "paper":
            print("your input is paper")
            print("my input is paper")
            print("its a tie")
        elif computer_input == "scissor":
            print("your input is paper")
            print("my input is scissor")
            print("i win!")
            comp_pts += 1
    if user_input == "scissor":
        if computer_input == "rock":
            print("your input is scissor")
            print("my input is rock")
            print("i win !")
            comp_pts += 1
        elif computer_input == "paper":
            print("your input is scissor")
            print("my input is paper")
            print("you win")
            user_pts += 1
        elif computer_input == "scissor":
            print("your input is scissor")
            print("my input is scissor")
            print("its tie")














