import pytest
from engines import TicTacToe
from models.tic_tac_toe import PawnType, EndStatus
from config import GRID_LENGTH

@pytest.fixture
def game():
    return TicTacToe()

def test_create_game(game):
    board = game.create_game()
    assert isinstance(board, str)
    assert len(board) == GRID_LENGTH ** 2
    assert all(cell == " " for cell in board)

def test_play_turn_valid(game):
    board = game.create_game()
    updated_board = game.play_turn(board, PawnType.X, 0)
    assert updated_board[0] == PawnType.X

def test_play_turn_invalid(game):
    board = game.create_game()
    board = game.play_turn(board, PawnType.X, 0)
    with pytest.raises(ValueError, match="The selected place isn't available"):
        game.play_turn(board, PawnType.O, 0)

def test_get_game_status_win_row(game):
    board = "XXX      "
    assert game.get_game_status(board) == EndStatus.X

def test_get_game_status_win_column(game):
    board = "X  X  X  "
    assert game.get_game_status(board) == EndStatus.X

def test_get_game_status_win_diagonal(game):
    board = "X   X   X"
    assert game.get_game_status(board) == EndStatus.X

def test_get_game_status_draw(game):
    board = "XOXXOOOXX"
    assert game.get_game_status(board) == EndStatus.DRAW

def test_get_game_status_none(game):
    board = "XO XO    "
    assert game.get_game_status(board) is None
