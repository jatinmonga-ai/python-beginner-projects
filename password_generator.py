import random
import string

define generate_password(length):
       characters= string.ascii_letter + string.digits + string.punctuation
       password= ' '.join(random.choice(characters) for_in range(length))
       return password

password_length = int(input("Enter password length: "))
print("Your generated password is : ", generate_password(password_length)
