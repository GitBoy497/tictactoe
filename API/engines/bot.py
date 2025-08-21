import random

from .tic_tac_toe import TicTacToe
from API.models.tic_tac_toe import PawnType

class Bot:
    """Represent a bot to play game."""

    def play_tic_tac_toe(self, game_engine: TicTacToe, game_str: str, pawn_type: PawnType):
        """Play a turn in a tic tac toe game."""
        empty_cells = [index for index, char in enumerate(game_str) if char == ' ']

        choosen_cell = random.choice(empty_cells)

        return game_engine.play_turn(game_str, pawn_type, choosen_cell)