##Second method
## for loop for the iteration
UserName = input('Please Enter your Name ')
UserAge = int(input('Please Enter your Age '))
Years = 100 - UserAge
num = int(input('Please enter how many time you want to print'))
for i in range(num):
    print ('you will turn 100 years old in' + '\t' + str(Years) + '\n')
