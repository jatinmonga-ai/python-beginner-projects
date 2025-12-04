##Caculator

import math 
def add(x,y):
   return x+y

def subtract(x,y):
   return x-y

def multiplication(x,y):
   return x*y

def division(x,y):
    if y==0:
        return"Cannot divide by zero"
    return x/y

def sqrt(x):
    if x<0:
        return"Cannot do squrt of negative numbers"
    return math.sqrt(x)

while True:
     print("Choose one option")
     print("1." "Add")
     print("2." "Subtract")
     print("3." "Multiplication")
     print("4." "Division")
     print("5." "Squrt")
     print("6." "Exit")

     choice=(input("Enter your option(1,2,3,4,5,6): "))

     if choice=="6":
         print("goodbye")
         break
     else:
         num1=float(input("Enter your first number: "))
         num2=float(input("Enter your second number: "))


     if choice== "1":
        print("result: ", add(num1,num2))
     elif choice=="2":
        print(subtract(num1,num2))
     elif choice=="3":
        print(multiplication(num1,num2))
     elif choice=="4":
        print(division(num1,num2))
     elif choice=="5":
       num_choice = input("Do you want the square root of first number (1) or second number (2)? ")
       if num_choice == "1":
         print("Result: ", sqrt(num1))
       elif num_choice == "2":
         print("Result: ", sqrt(num2))
       else:
         print("Invalid choice")
     else:
         print("Invalid input")
         
input("Press Enter to exit")
    

