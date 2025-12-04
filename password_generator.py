import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    user_input = input("Enter password length (or type 'exit' to quit): ")
    
    if user_input == "exit":
        print("Goodbye!")
        break
    
    length = int(user_input)
    password = generate_password(length)
    print("Your password is:", password)
    print()


