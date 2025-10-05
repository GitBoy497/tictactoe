import random

from .bot_interface import BotInterface  

from config import GRID_LENGTH, PAWNS_TO_ALIGN
from engines import TicTacToe
from models.tic_tac_toe import PawnType

class TicTacToeBot(BotInterface):
    """Represents a bot to play a tic tac toe game."""

    def play(self, game_engine: TicTacToe, game_str: str, pawn_type: PawnType):
        """Play a turn in a tic tac toe game."""
        game_list = game_engine.str_to_list_grid(game_str)
        player_pawn_type = PawnType.O if pawn_type == PawnType.X else PawnType.X

        move: int

        pawn_to_play = self._find_best_move(game_list, pawn_type)
        if pawn_to_play is not None :
            move = pawn_to_play
            print('Go')
        elif (pawn_to_play := self._find_best_move(game_list, player_pawn_type)) is not None:
            move = pawn_to_play
            print('Stop')
        else:
            empty_cells = [index for index, char in enumerate(game_str) if char == ' ']

            move = random.choice(empty_cells)

        print(move)
        return game_engine.play_turn(game_str, pawn_type, move)
    
    def _find_best_move(
            self,
            game_list: list[list[str]], 
            pawn: PawnType
        ) -> int | None :
        """Find the best move to align (size - 1) pawns in a row, column or diagonal."""
        # Lines check
        for i_row in range(GRID_LENGTH):
            row = game_list[i_row]
            if row.count(pawn.value) == PAWNS_TO_ALIGN - 1 and row.count(' ') == 1:
                return row.index(' ') + i_row*3

        # Column check
        for i_col in range(GRID_LENGTH):
            col = [game_list[i_row][i_col] for i_row in range(GRID_LENGTH)]
            if col.count(pawn.value) == PAWNS_TO_ALIGN - 1 and col.count(' ') == 1:
                return col.index(' ') * 3 + i_col

        # Main diagonal check : left to right
        main_diag = [game_list[idx][idx] for idx in range(GRID_LENGTH)]
        if main_diag.count(pawn.value) == PAWNS_TO_ALIGN - 1 and main_diag.count(' ') == 1:
            return main_diag.index(' ') * (GRID_LENGTH + 1)

        # Anti diagonal check : right to left
        anti_diag = [
            game_list[idx][GRID_LENGTH - 1 - idx] 
            for idx in range(GRID_LENGTH)
        ]
        if anti_diag.count(pawn.value) == PAWNS_TO_ALIGN - 1 and anti_diag.count(' ') == 1:
            idx = anti_diag.index(' ')
            return idx * GRID_LENGTH + (GRID_LENGTH - 1 - idx)

        return None
    