import random

# print(help(random))

low = 1
high = 100
options = ("Rock", "Paper", "Scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)    1 ~ 100
# number = random.random()    0 ~ 1
# option = random.choice(options)
random.shuffle(cards)

print(cards)