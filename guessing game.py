import random

print("Enter Rock, Paper or Scissor")
guess_list = ["Rock", "Paper", "Scissor"]
guess = random.randint(0, 2)
guess_letter = guess_list[guess]

while True:
    user = input("Guess: ")
    if user != guess_letter:
        print("Guess again")
    elif user == guess_letter:
        print("Guess correct")
        break
























