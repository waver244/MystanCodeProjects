"""
File: hangman.py
Name:Yin Jun (Ingrid) Zeng
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This function plays hangman game.
    Player keeps inputting till making N_TURNS times of mistakes or winning the game.
    If the input is correct, the updated word on console will be displayed.
    Player has N_TURNS chances for the game. Every wrong input will reduce the chances.
    Non-single-alphabet input is an illegal format.
    """
    hint = ''  # The displayed hint for players
    hp = N_TURNS  # Remaining chances for players
    answer = random_word()  # The answer randomly selected
    for i in range(len(answer)):
        hint += '_'
    while hp != 0 and hint != answer:
        my_guessed = ''  # The guessed result so far
        print('The word looks like: ' + hint)
        print('You have ' + str(hp) + ' guesses left.')
        data = input('Your guess: ')  # The guess
        data = data.upper()  # case-insensitive
        if not data.isalpha() or len(data) > 1:  # Illegal format
            print('illegal format.')
        else:
            if data in answer:  # Correct
                print('You are correct!')
                for i in range(len(answer)):
                    if data == answer[i]:
                        my_guessed += data
                    else:
                        my_guessed += hint[i]
                hint = my_guessed  # Updating the displayed hint on console
            else:  # Wrong
                print('There is no ' + str(data.upper()) + '\'s in the word.')
                hp += -1  # Deducting one chance
    if hp == 0:  # Game over
        print('You are completely hung :（')
        print('The word was : ' + answer)
    else:  # Win
        print('You win!!')
        print('The word was : ' + answer)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
