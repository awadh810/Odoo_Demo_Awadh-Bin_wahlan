import random

# Game configure
number_to_guess = random.randint(1, 100)  # the range of guess number will be between this scope 1 و 100
total_attempts = 10  # عدد المحاولات المسموح بها
counter = 0
total_hint = 0

def get_hint(guess , number_to_guess , s):
    if number_to_guess - guess <= 10 and s == '+':
        print("Hint: The correct number is between ", {guess + 1}, {guess + 10})
    else:
        print("Hint: The correct number is greater than ", {guess})

    if guess - number_to_guess <= 10 and s == '-':
        print("Hint: The correct number is between ", {guess - 10}, " ", {guess - 1})
    else:
        print("Hint: The correct number is less than ", {guess})

def start_game():
    counter = 0
    hint = 0
    while counter < total_attempts:
        guess = int(input("Enter your guess number here: "))
        counter += 1
        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < number_to_guess:
            print("The number you choose is less than the correct number.")

        elif guess == '0' and total_hint != hint:
            get_hint()
        else:
            print("The number you choose is greater than the correct number.")
            get_hint(guess , number_to_guess , '-')


if __name__ == "__main__":
    start_game()
    if counter == total_attempts:
        print("Sorry, you've used all your attempts. The correct number was " ,  {number_to_guess})
