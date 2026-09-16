import math

print("welcome to the basic Calculator")
num =int(input("pick a function: \n 1) Addition \n 2) Subtraction\n"))

if num == 1:
   num1 = float(input("what is the first number: "))
   num2 = float(input("what is the second number: "))
   print(num1 + num2)
elif num == 2:
    print("The second number will subtract from the first")
    num1 = float(input("what is the first number: "))
    num2 = float(input("what is the second number: "))
    print(num1 - num2)
else:
    print("this is not one of the listed option")
