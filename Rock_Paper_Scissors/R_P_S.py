#Welcome to rock, paper, Scissors game
import random

print("Welcome to the Rock Paper Scissors Game")

def get_type(message):
   while True:
       user_input = input(message).lower()
       try:
           if user_input == "r":
               return "r"
           elif user_input == "p":
               return "p"
           elif user_input == "s":
               return "s"
           else:
               print("--)Please enter correct input(--")
       except:
           continue


type_1 = get_type("Please enter a rock, paper, or scissors (R/P/S): ")
tool_box = ["r", "p", "s"] # Rock =  r /\ Paper = p /\ Scissors = s

tool = random.choice(tool_box)

if tool == type_1:
    print("draw")
elif tool == "r" and type_1 == "s":
    print("computer choice : rock | player choice : paper")
    print("computer win")
elif tool == "p" and type_1 == "r":
    print("computer choice : paper | player choice : rock")
    print("computer win")
elif tool == "s" and type_1 == "p":
    print("computer choice : scissors | player choice : paper")
    print("computer win")
else:
    if tool == "r":
        print("computer choice : rock ")
    elif tool == "p":
        print("computer choice : paper ")
    elif tool == "s":
        print("computer choice : scissors ")
    print("player wins")
