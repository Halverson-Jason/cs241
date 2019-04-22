import random
from random import randint

def game_intro():
    print("Welcome to the number guessing game!")
    random_seed = input("Enter random seed: ")
    random.seed(random_seed)

def get_random():
    low = 1
    high = 100
    return randint(low, high)

def guess_number(random_number):
    number_guessed = 0
    counter = 0
    while(number_guessed != random_number):
        number_guessed = int(input("\nPlease enter a guess: "))
        counter += 1

        if number_guessed < random_number :
            print("Higher")
        elif number_guessed > random_number :
            print("Lower")

    print("Congratulations. You guessed it!")
    print("It took you %d guesses.\n" % (counter))

def play_again():
    play_again = input("Would you like to play again (yes/no)? ")

    if play_again == 'no':
        print("Thank you. Goodbye.")
        return False
    else:
        return True

def game_play():
    next_game = True
    while(next_game):
        guess_number(get_random())
        next_game = play_again()
        
game_intro()
game_play()