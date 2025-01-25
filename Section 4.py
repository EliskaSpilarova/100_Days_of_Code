# Heads or Tails
import random
heads_or_tails = random.randint(1,2)
if heads_or_tails == 1:
    print("Heads!")
else:
    print("Tails!")

# Banker Roulette
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
picked_friend = random.choice(friends)
print(picked_friend)

# Rock Paper Scissors
from random import randrange

while True:
    number = randrange(3)
    if number == 0:
        computer_move = "rock"
    elif number == 1:
        computer_move = "scissors"
    elif number == 2:
        computer_move = "paper"

    human_move = input("Tell me your move (rock, paper, scissors, or end): ")

    if human_move == "end":
        print("Mischief managed.")
        break

    
    if human_move == computer_move:
        print("Draw.")
    elif (human_move == "paper" and computer_move == "rock") or \
         (human_move == "rock" and computer_move == "scissors") or \
         (human_move == "scissors" and computer_move == "paper"):
        print("You won!")
    else:
        print("The computer won.")