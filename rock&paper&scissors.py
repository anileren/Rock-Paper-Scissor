import random

rps = ["rock", "paper", "scissors"]
pc_choice = random.choice(rps)
user_choice = ""

def game():
    user_choice = input("Rock/paper/scissors ?")
    if user_choice.lower() == "rock" and pc_choice == "rock":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("even")
    elif user_choice.lower() == "rock" and pc_choice == "paper":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("lose")
    elif user_choice.lower() == "rock" and pc_choice == "scissors":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("win")
    elif user_choice.lower() == "paper" and pc_choice == "rock":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("win")
    elif user_choice.lower() == "paper" and pc_choice == "paper":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("even")
    elif user_choice.lower() == "paper" and pc_choice == "scissors":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("lose")
    elif user_choice.lower() == "scissors" and pc_choice == "rock":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("lose")
    elif user_choice.lower() == "scissors" and pc_choice == "paper":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("win")
    elif user_choice.lower() == "scissors" and pc_choice == "scissors":
        print("artificial intelligence's choice was: " + str(pc_choice))
        print("even")

game()
