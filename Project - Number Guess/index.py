import random

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")

def number():
    return random.randint(1, 100)

def game():
    """Start the guessing game"""
    playing = True

    while playing:
        difficulty = input('Choose a difficulty. "y" for easy, any other key for hard: ')
        attempts = 10 if difficulty == 'y' else 5
        random_num = number()

        while attempts > 0:
            try:
                print(f"You have {attempts} attempts remaining.")
                num_guess = int(input('Make a guess: '))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if num_guess == random_num:
                print(f"That's correct! You guessed {num_guess} correctly.")
                break
            elif num_guess > random_num:
                print("Too high.")
            else:
                print("Too low.")

            attempts -= 1

        if attempts == 0:
            print(f'Game Over. The correct number was {random_num}.')

        play_again = input('Press "y" to play again or any other key to exit: ') == 'y'
        if not play_again:
            print("Thank you for playing!")
            playing = False

game()
