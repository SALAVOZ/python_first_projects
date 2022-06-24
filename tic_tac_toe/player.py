import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_square_for_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_square_for_move(self, main):
        is_valid_input = False
        square_number = None
        while not is_valid_input:
            try:
                square_number = int(input('Your round. Choose square: '))
                if square_number in main.get_available_squares():
                    is_valid_input = True
                else:
                    raise ValueError
            except ValueError:
                print('Write valid square: ')
        return square_number


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_square_for_move(self, main):
        return random.choice(main.get_available_squares())