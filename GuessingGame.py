import random
random.seed(1)
input = input("enter a number")
for x in range(10):
    value = int(random.randint(0,10))
    if input == value:
        print("Generated random number matches the input",value)
    else:
        print("entered number doesnt match the user input")
