## MyVer

import random

choices = ("rock", 
          "paper", 
          "scissors")

answer =  random.choice(choices)

while True:

    user = input("Please enter your choice(rock,paper,or scissors): ").lower()

    if user not in choices:
        print("Invalid choice.")

    elif user == answer:
        print(f"Computer chose {answer}")
        print(f"You chose {user}")
        print()

        print("It is a TIE!")
        break
    
    elif user == "rock" and answer == "scissors" or user == "scissors" and answer == "paper" or user == "paper" and answer == "rock":
        print(f"Computer chose {answer}")
        print(f"You chose {user}")
        print()
        
        print("You WIN!")
        break

    else:
        print(f"Computer chose {answer}")
        print(f"You chose {user}")
        print()
        
        print("You LOSE!")
        break


## Tutor
# import random

# options = ("rock", "paper", "scissors")

# is_running = True

# while is_running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a TIE!")
#     elif player == "rock" and computer == "scissors":
#         print("You WIN!")
#     elif player == "paper" and computer == "rock":
#         print("You WIN!")
#     elif player == "scissors" and computer == "paper":
#         print("You WIN!")
#     else:
#         print("You LOSE!")

#     play_again = input("Play again? (y/n): ").lower()
#     if not play_again == "y":
#         is_running = False

# print("Thanks for playing!")