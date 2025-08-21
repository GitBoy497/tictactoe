from engines import Bot, TicTacToe
from models.tic_tac_toe import PawnType

def test_tic_tac_toe():
    game = TicTacToe()
    bot = Bot()
    game_str_before = "X OX  XO " # empty indexes: 1 4 5 8
    pawn_type = PawnType.X

    result = bot.play_tic_tac_toe(game, game_str_before, pawn_type)

    assert result.count(pawn_type.value) > game_str_before.count(pawn_type.value)
    assert any(result[i] != ' ' for i in [1, 4, 5, 8])
