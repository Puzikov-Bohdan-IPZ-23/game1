import argparse

class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))

    def make_move(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                print(f'Гравець {self.current_player} виграв!')
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Невірний хід. Спробуйте ще раз.')
        return False

    def check_winner(self, row, col):
        # Перевірка рядків, стовпців та діагоналей
        if all(self.board[row][c] == self.current_player for c in range(self.size)) or \
           all(self.board[r][col] == self.current_player for r in range(self.size)) or \
           all(self.board[i][i] == self.current_player for i in range(self.size)) or \
           all(self.board[i][self.size - 1 - i] == self.current_player for i in range(self.size)):
            return True
        return False

    def play(self):
        while True:
            self.print_board()
            try:
                row, col = map(int, input(f'Гравець {self.current_player}, введіть координати (рядок і стовпчик через пробіл): ').split())
                if self.make_move(row, col):
                    self.print_board()
                    break
            except ValueError:
                print('Будь ласка, введіть два числа через пробіл.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Гра Хрестики-Нулики.")
    parser.add_argument("--size", type=int, default=3, help="Розмір поля (за замовчуванням 3x3).")
    args = parser.parse_args()

    game = TicTacToe(args.size)
    game.play()
