from dotenv import dotenv_values
from fastapi import APIRouter

from ..engines.tic_tac_toe import TicTacToe
from ..models.tic_tac_toe import MoveRequest

router = APIRouter()

tic_tac_toe = TicTacToe ()

@router.get("/new_game")
def create_game():
    """Create a tic tac toe game."""
    return tic_tac_toe.create_game()


@router.post("/place_pawn")
def play_turn(move: MoveRequest):
    """Play a turn in a tic tac toe game. 
    """
    try:
        game_str = tic_tac_toe.play_turn(
            move.game_str, 
            move.pawn_type, 
            move.cell_number
        )

        return {
            "board" : game_str,
            "status" : tic_tac_toe.get_game_status(game_str)
        }
    except ValueError as e :
        return e


@router.get("/settings")
def get_settings():
    """Get the currents settings on which the game's based on"""
    config = dotenv_values(".env")
    return {k: v for k, v in config.items()}