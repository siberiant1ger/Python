import random
options = ["rock", "paper", "scissors"]
print("welcome to the rock, paper, scissors game")

while True:
    user_choice = input(' enter "paper", "rock" or "scissors" to play: ').lower()
    user_choice in options
    break
else:
    print("invalid input, please try again")   
