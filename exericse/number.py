import random

while True:
    # Generate a new number each game
    secret_number = random.randint(1, 10)
    print("\nI'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        # Ask for the user's guess
        number = int(input("Enter your guess: "))

        if number == secret_number:
            print("🎉 Congratulations, you guessed it!")
            break  # Exit the inner loop when correct
        elif number > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        else:
            print("Nope, your guess is a bit low. Give it another shot!")

    # Ask if the player wants to play again
    playing_again = input("Do you want to play again? (yes/no): ").lower()
    if playing_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break  # Exit the outer loop
