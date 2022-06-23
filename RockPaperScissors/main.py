import random


def play():
    user_choise = input('Rock(r) or Paper(p) or Scissors(s): ').lower()
    computer_choise = random.choice(['r', 'p', 's'])
    if user_choise == computer_choise:
        return 'tie!'
    if user_choise == 'r' and computer_choise == 's' or user_choise == 'p' and computer_choise == 'r' \
        or user_choise == 's' and computer_choise == 'p':
        return f'your choise is {user_choise}, computer choise is {computer_choise} ;you win!'
    return f'your choise is {user_choise}, computer choise is {computer_choise}; you lost!'


if __name__ == '__main__':
    print(play())

