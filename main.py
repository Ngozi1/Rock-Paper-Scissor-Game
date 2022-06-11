import random

CPU_wins = 0
player_wins = 0

def choose_option():
    user_choice = input("choose Rock, Paper or Scissor: ")
    if user_choice in ["rock", "R"]:
        user_choice = "R"
    elif user_choice in ["paper", "P"]:
        user_choice = "P"
    elif user_choice in ["scissor", "S"]:
        user_choice = "S"
    else:
        print("Invalid, try again.")
        choose_option()
    return user_choice

def CPU_option():
    CPU_choice = random.randint(1,3)
    if CPU_choice == 1:
        CPU_choice = "R"
    elif CPU_choice == 2:
        CPU_choice = "P"
    else:
        CPU_choice = "S"
    return CPU_choice

while True:
    print("")
    user_choice = choose_option()
    CPU_choice = CPU_option()
    print("")

    if user_choice == "R":
        if CPU_choice == "R":
            print("you choose rock. the computer choose rock. You tied.")
        elif CPU_choice == "P":
            print("you choose rock. the computer choose paper. You lose.")
            CPU_wins += 1

        elif CPU_choice == "S":
            print("you choose rock. the computer choose scissoor. You win.")
            player_wins += 1

    elif user_choice == "P":
        if CPU_choice == "R":
            print("you choose paper. the computer choose rock. You win.")
            player_wins += 1   

        elif CPU_choice == "P":
            print("you choose paper. the computer choose paper. You tied.")

        elif CPU_choice == "P":
            print("you choose paper. the computer choose scissoor. You lose.")
            player_wins += 1   
    
    elif user_choice == "S":
        if CPU_choice == "R":
            print("you choose scissor. the computer choose rock. You lose.")
            CPU_wins += 1   

        elif CPU_choice == "P":
            print("you choose scissor. the computer choose paper. You win.")
            player_wins += 1

        elif CPU_choice == "S":
            print("you choose scissor. the computer choose scissoor.S You tied.")


    print("") 
    print("player wins:" + str(player_wins))  
    print("CPU wins: " + str(CPU_wins))  
    print("")   

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y","y","YES", "yes"]:
        pass
    elif user_choice in ["N","n","NO", "no"]:
       break
    else:
       break

        
        