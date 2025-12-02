import random

print(f"!--)Welcome to Random Number Generator(--!")

# function to get number from user
# also check the value is integer most if he entered a char it's will ask again until we get integer

def get_num(message):
    while True:
        user_input = input(message)
        try:
            number = int(user_input)
            break
        except ValueError:
            print("Please enter a number")
    return number

#calling function for each value

attempts = get_num("Enter number of attempt: ")
number_min = get_num("Enter minimum number: ")
number_max = get_num("Enter maximum number: ")

# generating numbers depending on attempts
i = attempts # defining how many times
for i in range(attempts):
    x = random.randrange(number_min,number_max)
    print(f"Random Number is --> {x}")
    i -= 1
