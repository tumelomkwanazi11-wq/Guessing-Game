secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess the secret number between 1 and 10:"))
    if guess != secret_number:
        print("Wrong guess. Try again!")
print("Congratulations! You guessed the secret number.")
