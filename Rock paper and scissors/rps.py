import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]


# the loop under runs until the user decides to exit by pressing e
while True:
    user_input = input("enter rock/paper/scissors or press e to exit the game ").lower()
    if user_input == "e":
        break

    if user_input not in choices:
        continue
    
    # The computer here chooses a random number which either gives rock, paper or scissors
    random_number = random.randint(0, 2)
    
    computer_pick = choices[random_number]
    print("The Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1 # user win count

    else:
        print("You lost!")
        computer_wins += 1 # computer win count
        
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Have a nice day")