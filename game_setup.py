import random


class Game(object):
    """
        The Game object represents the set up and the two modes of the game that are available
    """

    def __init__(self, mode):
        self.mode = mode

    def guess(x):
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {x} '))
            if guess < random_number:
                print(guess)
                print('Sorry, guess again. Too low')
            elif guess > random_number:
                print(guess)
                print('Sorry, guess again. Too high')

        print(
            f"Good job, you have guessed the random number:  {random_number}")

    def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low  # could also be high b/c low = high
            feedback = input(
                f'Is {guess} too high (h), too Low (l) or correct (c)?')
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1

        print(f'Yay! the computer guessed your number {guess} correctly')
