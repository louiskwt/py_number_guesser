from game_setup import Game
# i for input variable
i = ''

while i != 'y' or i != 'c':
    print('Choose the mode of the game by typeing (c) to let the computer guess your number or (y) for you to guess a number generated by computer | You can press (q) to quit')
    i = input()
    if i == 'c':
        Game.computer_guess(100)
        break
    elif i == 'y':
        Game.guess(100)
        break

    if i == 'q':
        break
