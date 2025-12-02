## roll the dice game on CLI
import random
from time import sleep

print("Welcome to Roll the Dice")

while True:
    user_input = input("Roll the Dice? (y/n): ").lower()
    if user_input == "y":
        print("Rolling dice...")
        sleep(4)
        x = random.randrange(1, 6)
        y = random.randrange(1, 6)
        print(f"The dice is {x, y}")

    elif user_input == "n":
        print("end")
        break
    else:
        print("Please enter y or n")
