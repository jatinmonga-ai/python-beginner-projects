import random
import string

define generate_password(length):
       characters= string.ascii_letters + string.digits + string.punctuation
       password= ''.join(random.choice(characters) for _ in range(length))
       return password

password_length = int(input("Enter password length: "))
print("Your generated password is : ", generate_password(password_length))
