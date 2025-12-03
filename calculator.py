# Simple Calculator Program
# Created by Jatin Monga

# Ask user for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask user for operation
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# Perform operation
if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid Input")
