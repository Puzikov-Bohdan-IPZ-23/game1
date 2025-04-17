import pytest
from Tic_Tac_Toe import TicTacToe
from unittest import mock

# 📌 Фікстура: створює нову гру перед кожним тестом
@pytest.fixture
def game():
    return TicTacToe(size=3)

#  Тест 1: Початковий стан поля
def test_initial_state(game):
    assert all(cell == ' ' for row in game.board for cell in row)
    assert game.current_player == 'X'

#  Тест 2: Валідний хід змінює стан
def test_valid_move(game):
    assert game.make_move(1, 1) is False
    assert game.board[0][0] == 'X'
    assert game.current_player == 'O'

#  Тест 3: Невалідний хід — мок для capsys
def test_invalid_move(game, capsys):
    game.make_move(1, 1)
    game.make_move(1, 1)  # Повторний хід у ту саму клітинку
    captured = capsys.readouterr()
    assert "Невірний хід" in captured.out

#  Параметризація: перемога по горизонталі, вертикалі, діагоналям
@pytest.mark.parametrize("board, move, player", [
    ([['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], (1, 3), 'X'),   # горизонталь
    ([['X', ' ', ' '], ['X', ' ', ' '], [' ', ' ', ' ']], (3, 1), 'X'),   # вертикаль
    ([['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']], (3, 3), 'X'),   # головна діагональ
    ([[' ', ' ', 'X'], [' ', 'X', ' '], [' ', ' ', ' ']], (3, 1), 'X')    # побічна діагональ
])
def test_winning_combinations(board, move, player):
    game = TicTacToe(size=3)
    game.board = board
    game.current_player = player
    assert game.make_move(*move) is True

#  Мокування: перевіримо що print_board викликається під час виграшу
def test_print_called_on_win():
    game = TicTacToe(size=3)
    game.board = [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    game.current_player = 'X'
    with mock.patch('builtins.print') as mocked_print:
        game.make_move(1, 3)
        mocked_print.assert_any_call('Гравець X виграв!')

#  Маркер: помітимо як "critical"
@pytest.mark.critical
def test_switching_players(game):
    game.make_move(1, 1)
    assert game.current_player == 'O'
