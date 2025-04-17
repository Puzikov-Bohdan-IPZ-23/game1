import argparse
from colorama import init, Back, Style

init(autoreset=True)

class TicTacToe:
    def __init__(self, size=3, bgcolor="black"):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'
        self.bgcolor = bgcolor
        self.bg = self.get_background_color(bgcolor)
 
    def get_background_color(self, color_name):
        colors = {
            "black": Back.BLACK,
            "red": Back.RED,
            "green": Back.GREEN,
            "yellow": Back.YELLOW,
            "blue": Back.BLUE,
            "magenta": Back.MAGENTA,
            "cyan": Back.CYAN,
            "white": Back.WHITE
        }
        return colors.get(color_name.lower(), Back.BLACK)

    def print_board(self):
        for i, row in enumerate(self.board):
            row_str = '|'.join(self.bg + cell + Style.RESET_ALL for cell in row)
            print(row_str)
            if i < self.size - 1:
                print('-' * (self.size * 2 - 1))

    def make_move(self, row, col):
        row -= 1
        col -= 1

        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.print_board()
                print(f'Гравець {self.current_player} виграв!')
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Невірний хід. Спробуйте ще раз.')
        return False

    def check_winner(self, row, col):
        if all(self.board[row][c] == self.current_player for c in range(self.size)):
            return True
        if all(self.board[r][col] == self.current_player for r in range(self.size)):
            return True
        if all(self.board[i][i] == self.current_player for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == self.current_player for i in range(self.size)):
            return True
        return False

    def play(self):
        print(f"Колір фону: {self.bgcolor.upper()}")
        print("Введіть координати у форматі: рядок і стовпчик через пробіл (наприклад, 1 1)")
        while True:
            self.print_board()
            try:
                row, col = map(int, input(f'Гравець {self.current_player}, введіть координати: ').split())
                if self.make_move(row, col):
                    break
            except ValueError:
                print('Будь ласка, введіть два числа через пробіл.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Гра Хрестики-Нулики.")
    parser.add_argument("--size", type=int, default=3, help="Розмір поля (за замовчуванням 3x3).")
    parser.add_argument("--bgcolor", choices=["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"],
                        default="black", help="Колір фону поля (за замовчуванням: black).")
    args = parser.parse_args()

    game = TicTacToe(size=args.size, bgcolor=args.bgcolor)
    game.play()
