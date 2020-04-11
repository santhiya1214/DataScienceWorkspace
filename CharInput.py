'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.Extras:   
	• Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)'''




## First method of implementation
## Used input(), \t, \n, int(), str()san

UserName = raw_input('Please Enter your Name ')
UserAge = 100 - input('Please Enter your Age ')
num = int(input('Please enter how many time you want to print'))
print(num * ('you will turn 100 years old in'+'\t' +str(UserAge) +'\n'))
