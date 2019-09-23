from random import randint

__author__ = 'Martin Boe'
__email__ = 'martinb@nmbu.no'


def guess_a_number():
    """Returns the number you guessed unless that number is 0, then the
    loop runs again"""
    guessed_number = 0
    while guessed_number < 1:
        guessed_number = int(input('Your guess: '))
    return guessed_number


def sum_two_dice():
    """Returns the sum of two dice"""
    return randint(1, 6) + randint(1, 6)


def is_equal(number1, number2):
    """Checks if two numbers are equal. Returns True or False"""
    return number1 == number2


if __name__ == '__main__':

    equal_numbers = False
    number_of_tries = 3
    score_two_dice = sum_two_dice()

    while equal_numbers is False and number_of_tries > 0:
        guess = guess_a_number()
        equal_numbers = is_equal(score_two_dice, guess)

        if not equal_numbers:
            print('Wrong, try again!')
            number_of_tries -= 1

    if number_of_tries > 0:
        print('You won {} points.'.format(number_of_tries))
    else:
        print('You lost. Correct answer: {}.'.format(score_two_dice))
