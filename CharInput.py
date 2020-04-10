## First method of implementation
## Used input(), \t, \n, int(), str()

UserName = raw_input('Please Enter your Name ')
UserAge = 100 - int(input('Please Enter your Age '))
num = int(input('Please enter how many time you want to print'))
print(num * ('you will turn 100 years old in'+'\t' +str(UserAge) +'\n'))
