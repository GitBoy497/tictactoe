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

    def str_to_list_grid(self, game_str: str):
        """"""
        return [game_str[
                row_number*GRID_LENGTH : (row_number+1)*GRID_LENGTH
                ] for row_number in range(GRID_LENGTH)
            ]

    def _check_columns(self, game_str: str, pawn_type: PawnType):
        """Check if a givien pawn type is algin on columns."""
        grid = self.str_to_list_grid(game_str)
        
        for column in range(GRID_LENGTH):
            for row in range(GRID_LENGTH - PAWNS_TO_ALIGN + 1):
                if all(grid[row+i][column] == pawn_type for i in range(PAWNS_TO_ALIGN)):
                    return True
        return False

    def _check_diagonals(self, game_str: str, pawn_type: PawnType):
        """Check if a givien pawn type is algin on diagonals."""
        grid = self.str_to_list_grid(game_str)

        availables_indexes_start = GRID_LENGTH - PAWNS_TO_ALIGN + 1

        # left to right diagonals
        for row in range(availables_indexes_start):
            for column in range(availables_indexes_start):
                if all(grid[row+i][column+i] == pawn_type for i in range(PAWNS_TO_ALIGN)):
                    return True

        # right to left diagonals
        for r in range(availables_indexes_start):
            for c in range(PAWNS_TO_ALIGN - 1, GRID_LENGTH):
                if all(grid[r+i][c-i] == pawn_type for i in range(PAWNS_TO_ALIGN)):
                    return True

        return False
