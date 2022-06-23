import random


def guess(max_number):
    low = 1
    high = max_number
    feedback = ''
    guess_number = 0
    while feedback != 'c':
        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess_number = low
        feedback = input('Is {} low(L) or high(H) or correct(C): '.format(guess_number)).lower()
        if feedback == 'h':
            high = guess_number - 1
        if feedback == 'l':
            low = guess_number + 1
    print('yeah! Computer won. It guessed the number {}'.format(guess_number))


if __name__ == '__main__':
    guess(100)

