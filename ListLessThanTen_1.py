# coding=utf-8
'''
# Take a list, say for example this one: 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]and
# write a program that prints out all the elements
# of the list that are less than 5.
# Extras:DiscussionThis week’s topics: 
# More conditionals (if statements)
# Instead of printing the elements one by one, make a new list that has
# all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only
# elements from the original list a that are smaller than that number given by the user.'''


num = input("please enter the number to compare")
print(type(num))
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list1 = []
## one line to check the for loop3
## list1=[value for value in list if value <num]
for value in list:
    if (value < num):
        list1.append(value)
    else:
        print("values are not less than 5")

print(list1)
