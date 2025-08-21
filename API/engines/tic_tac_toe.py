import re

from config import GRID_LENGTH, PAWNS_TO_ALIGN
from models.tic_tac_toe import PawnType, EndStatus

class TicTacToe:
    """Represent a tic tac toe game"""

    def create_game(self):
        """Create a tic tac toe game."""
        return ' ' * pow(GRID_LENGTH, 2)

    def play_turn(self, game_str: str, pawn_type: PawnType, cell_number: int):
        """Play a turn by placing a pawn on the grid."""
        if not self._is_place_available(game_str, cell_number):
            raise ValueError("The selected place isn't available !")

        game_str = self._replace_char(game_str, cell_number, pawn_type)

        return game_str

    def _replace_char(self, str: str, index: int, new_char: str):
        """Replace a char in a string with an other one."""
        listed_char = list(str)
        listed_char[index] = new_char
        return "".join(listed_char)

    def _is_place_available(self, game_str: str, cell_number: int):
        """Check if a cell_number on the given grid is free."""
        return game_str[cell_number] == " "

    def get_game_status(self, game_str: str):
        """Return the status of the given game."""

        if self._check_pawns_alignement(game_str, "X"):
            return EndStatus.X
        elif self._check_pawns_alignement(game_str, "O"):
            return EndStatus.O
        elif not (" " in game_str):
            return EndStatus.DRAW
        else :
            return None

    def _check_pawns_alignement(self, game_str: str, pawn_type: PawnType):
        """Check if a given pawn type has pawns align."""
        return (
            self._check_rows(game_str, pawn_type) or
            self._check_columns(game_str, pawn_type) or
            self._check_diagonals(game_str, pawn_type)
        )
    
    def _check_rows(self, game_str: str, pawn_type: PawnType):
        """Check if a givien pawn type is algin on rows."""
        pattern = pawn_type * PAWNS_TO_ALIGN
        for i in range(0, len(game_str), GRID_LENGTH):
            row = game_str[i:i + GRID_LENGTH]
            if pattern in row:
                return True
        return False

    def _check_columns(self, game_str: str, pawn_type: PawnType):
        """Check if a givien pawn type is algin on columns."""
        spacing = GRID_LENGTH -1

        pattern = f".{{0,{spacing}}}({re.escape(pawn_type)})"
        for _ in range(PAWNS_TO_ALIGN - 1):
            pattern += f".{{{spacing}}}\\1"

        return bool(re.search(pattern, game_str))

    def _check_diagonals(self, game_str: str, pawn_type: PawnType):
        """Check if a givien pawn type is algin on diagonals."""
        # X...X...X (3x3)
        left_to_right_pattern = (
            f"({re.escape(pawn_type)})"
            + "".join([
                f".{{{GRID_LENGTH}}}\\1"
                for _ in range(PAWNS_TO_ALIGN - 1)
            ])
        )

        # ..X.X.X.. (3x3)
        right_to_left_pattern = (
            f".{{{GRID_LENGTH-1}}}({re.escape(pawn_type)})"
            + "".join([
                f".{{{GRID_LENGTH-2}}}\\1"
                for _ in range(PAWNS_TO_ALIGN - 1)
            ])
        )

        return (
            bool(re.search(left_to_right_pattern, game_str)) or 
            bool(re.search(right_to_left_pattern, game_str))
        )
