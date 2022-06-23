import random

def guess(max_number):
    random_number = random.randint(1, max_number)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input('Guess number between 1 and {}: '.format(max_number)))
        if guess_number > random_number:
            print('too high')
        if guess_number < random_number:
            print('too low')
    print('you win!!! you guessed the number {}'.format(random_number))


if __name__ == '__main__':
    guess(20)
