from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def print_board_numbers(self):
        for row in [[str(j) for j in range(i * 3, (i + 1) * 3)] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def get_available_squares(self):
        return [i for i, letter in enumerate(self.board) if letter == ' ']

    def is_board_free(self):
        # ЕСЛИ ХОТЬ ОДИН ПУСТОЙ, ЗНАЧИТ True
        # ЕСЛИ ПУСТЫХ НЕТ, ТО False
        return any([square == ' ' for square in self.board])

    def make_move(self, letter, square_number):
        self.board[square_number] = letter

    def play(self, x_player, o_player, obj, showNumbers=False):
        letter = 'X'
        while True:
            if not self.is_board_free():
                print('Tie')
                exit(0)
            self.print_board()
            if showNumbers:
                self.print_board_numbers()
            print('\n')
            if letter == 'X':
                square = x_player.get_square_for_move(obj)
            elif letter == 'O':
                square = o_player.get_square_for_move(obj)
            self.make_move(letter, square)

            if any([all([self.board[j] == letter for j in range(i * 3, (i + 1) * 3)]) for i in range(3)]) or \
                    any([all([self.board[j] == letter for j in range(i, 9, 3)]) for i in range(3)]):
                print('Winner is {}'.format(letter))
                self.print_board()
                exit(0)
            letter = 'X' if letter == 'O' else 'O'


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    game = TicTacToe()
    game.play(x_player, o_player, game)
