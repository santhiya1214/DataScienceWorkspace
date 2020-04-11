# coding=utf-8
# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?Extras:DiscussionConcepts for this week:   
# 	• Modular arithmetic (the modulus operator)
# 	• Conditionals (if statements)
# 	• Checking equality
# 	• If the number is a multiple of 4, print out a different message.



num = int(input("Please enter the number"))
##div =int(input("please enter the number u want to divide by"))
if(num%4==0):
    print("the number u entered is a multiple of 4")

elif (num%2==0):
    print("The number u entered is even")
else:
    print("the number u entered is odd")