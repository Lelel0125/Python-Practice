# Python number guessing game

## MyVer
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guess_time = 0

print("Python Number Guessing Game")
print("Select a number between 1 and 100")

while True:
    guess = (input("Enter your guess: "))

    if not guess.isdigit():
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")

    else:
        guess = int(guess)

        if guess > highest_num or guess < lowest_num:
            print("The number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess == answer:
            guess_time += 1
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of guesses: {guess_time}")
            break
        elif guess < answer:
            print("Too low! Try again!")
            guess_time += 1
        else:
            print("Too high! Try again!")
            guess_time += 1


## Tutor

# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:
#     guess = input("Enter your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again!")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False

#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")