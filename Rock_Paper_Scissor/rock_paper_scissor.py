import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("Goodbye!, it was nice to play with you.")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Try again.")
        continue

    # Convert number to actual move
    moves = { "1": "Rock", "2": "Paper", "3": "Scissors" }
    user_move = moves[choice]

    # Computer randomly picks a move
    computer_move = random.choice(["Rock", "Paper", "Scissors"])

    print(f"\nYou chose: {user_move}")
    print(f"Computer chose: {computer_move}")

    # Decide winner
    if user_move == computer_move:
        print("It's a tie!")
    elif (user_move == "Rock" and computer_move == "Scissors") \
        or (user_move == "Paper" and computer_move == "Rock") \
        or (user_move == "Scissors" and computer_move == "Paper"):
        print("You win!")
    else:
        print("You lose!")

print("Press Enter to exit")




