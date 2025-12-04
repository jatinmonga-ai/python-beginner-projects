import random 
import string

while True:
    length = input("Enter password length (or 'exit' to quit): ")
    if length == "exit":
        break
    length = int(length)
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    print("Your password is:", password, "\n")
    
 input("Press Enter to exit...")
   


