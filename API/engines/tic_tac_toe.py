import os
import re

class TicTacToe:
    """Represent a tic tac toe game"""

    def __init__(self):
        self.grid_length = int(os.getenv("GRID_LENGTH"))
        self.pawns_to_align = int(os.getenv("PAWNS_TO_ALIGN"))

    def create_game(self):
        """Create a tic tac toe game."""
        return ' ' * pow(self.grid_length, 2)

    def play_turn(self, game_str, pawn_type, cell_number):
        """Play a turn by placing a pawn on the grid."""
        if not self._is_place_available(game_str, cell_number):
            return ValueError("The selected place isn't available !")

        game_str = self._replace_char(game_str, cell_number, pawn_type)

        return game_str

    def _replace_char(self, str, index, new_char):
        """Replace a char in a string with an other one."""
        listed_char = list(str)
        listed_char[index] = new_char
        return "".join(listed_char)

    def _is_place_available(self, game_str, cell_number):
        """Check if a cell_number on the given grid is free."""
        return game_str[cell_number] == " "

    def get_game_status(self, game_str):
        """Return the status of the given game."""

        if self._check_pawns_alignement(game_str, "X"):
            return 1
        elif self._check_pawns_alignement(game_str, "O"):
            return 2
        elif not (" " in game_str):
            return 0
        else :
            return None

    def _check_pawns_alignement(self, game_str, pawn_type):
        """Check if a given pawn type has pawns align."""
        return (
            self._check_rows(game_str, pawn_type) or
            self._check_columns(game_str, pawn_type) or
            self._check_diagonals(game_str, pawn_type)
        )
    
    def _check_rows(self, game_str, pawn_type):
        """Check if a givien pawn type is algin on rows."""
        pattern = pawn_type * self.pawns_to_align
        return pattern in game_str

    def _check_columns(self, game_str, pawn_type):
        """Check if a givien pawn type is algin on columns."""
        spacing = self.grid_length -1

        pattern = f".{{0,{spacing}}}({re.escape(pawn_type)})"
        for _ in range(self.pawns_to_align - 1):
            pattern += f".{{{spacing}}}\\1"

        return bool(re.search(pattern, game_str))

    def _check_diagonals(self, game_str, pawn_type):
        """Check if a givien pawn type is algin on diagonals."""
        # X...X...X (3x3)
        left_to_right_pattern = (
            f"({re.escape(pawn_type)})"
            + "".join([
                f".{{{self.grid_length}}}\\1"
                for _ in range(self.pawns_to_align - 1)
            ])
        )

        # ..X.X.X.. (3x3)
        right_to_left_pattern = (
            f".{{{self.grid_length-1}}}({re.escape(pawn_type)})"
            + "".join([
                f".{{{self.grid_length-2}}}\\1"
                for _ in range(self.pawns_to_align - 1)
            ])
        )

        return (
            bool(re.search(left_to_right_pattern, game_str)) or 
            bool(re.search(right_to_left_pattern, game_str))
        )
