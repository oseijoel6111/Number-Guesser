from colors import *
from random import randint


# Welcome Screen Msg
def welcome_screen():
    print(BLUE, '**** Welcome To Your World Of Guessing *****')
    user_input = int(input(WHITE + 'Choose Your Level\n'
                                   '1. Normal (1 - 50)\n'
                                   '2. Intermediate (1 - 200)\n'
                                   '3. Hard (1 - 500)\n'
                                   '4. Exit Application\n\n'
                                   'Enter Request : '))
    # calling a function and passing user_input to it
    guess_range = user_option(user_input)
    if guess_range != 0:
        generate_random_number(guess_range)


# user's option
def user_option(user_input):
    guess_range = 0
    if user_input == 1:
        guess_range = 50
    elif user_input == 2:
        guess_range = 200
    elif user_input == 3:
        guess_range = 500
    elif user_input == 4:
        print('***** Thanks For Using Our App, Hope To See You Again **** ')
        exit(1)
    else:
        print(RED, 'Invalid Request, Try Again.')
        welcome_screen()
    return guess_range


def generate_random_number(guess_range):
    #  Generate random number between certain range
    generate_number = randint(1, guess_range)

    # user chances
    user_chances = 4

    # accepting the user input and validating, if it matches the generated number
    for i in range(4):
        user_guess = int(input(WHITE + 'Provide Your Guess Number : '))

    # Determine if the guess is correct
        if user_guess == generate_number:
            print(GREEN, f'Hurray!!!!, You Guess It Correct')
            break
        elif user_guess > generate_number:
            print(YELLOW, 'Your Guess Too High, Try Again.')
        elif user_guess < generate_number:
            print(YELLOW, 'Your Guess Too Low, Try Again')

    #  reduce the user chances and prompt user chances left
        user_chances -= 1
        print(f'Number Of Chances Left is {user_chances}')

    # inform user of the correct guess number
    if user_chances == 0:
        print(RED, f'Sorry The Correct Guess is {generate_number}')


welcome_screen()