# python program to create a simple calculator
# by Pornima Madan Salve
# 3 steps to build calculator program
# 1. functions for operations
# 2. user input
# 3. print result

# step 1 : create functions
# function to add two numbers
def addition(number1,number2):
    return number1+number2

# function to subtract two numbers
def subtraction(number1,number2):
    return number1-number2

# function to multiplication two numbers
def multiplication(number1,number2):
    return number1*number2

# function to divide two numbers
def divide(number1,number2):
    return number1/number2

# function to average two numbers
def average(number1,number2):
    return (number1+number2)/2


print("please select a operation:\n"\
    "1. addition\n"\
    "2. subtraction\n"\
    "3. multiplication\n"\
    "4. division\n"\
    "5. average\n")

select = int(input("select a operation from 1,2,3,4,5:"))

number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))

# step 3 : print the result
if select == 1:
    print(number1, "+", number2, "=",\
          addition(number1, number2))
    
elif select == 2:
    print(number1, "-", number2, "=",\
         subtraction(number1, number2))
    
elif select == 3:
    print(number1, "*", number2, "=",\
        multiplication(number1, number2))
    
elif select == 4:
    print(number1, "/", number2, "=",\
        divide(number1, number2))
    
elif select == 5:
    print("(",number1, "+", number2,")","/", "2", "=",\
          average(number1, number2))

else:
    print("Invalid operation please select again")