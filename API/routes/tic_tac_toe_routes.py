from dotenv import dotenv_values
from fastapi import APIRouter
from typing import Union

from bots import TicTacToeBot
from engines import TicTacToe
from models.tic_tac_toe import (
    PawnType,
    NewGameRequest,
    MoveRequest, 
    SuccessResponseModel, 
    ErrorResponseModel
)
from utilities.tic_tac_toe_response import success_response, error_response

router = APIRouter()

bot = TicTacToeBot()
tic_tac_toe = TicTacToe ()

@router.post("/new_game", response_model=SuccessResponseModel)
def create_game(new_game: NewGameRequest):
    """Create a tic tac toe game."""
    game_str = tic_tac_toe.create_game() 
    if new_game.choosen_pawn_type == PawnType.O :
        game_str = bot.play(
                        tic_tac_toe, 
                        game_str, 
                        PawnType.X
                        )
    return success_response(
            game_str, 
            None, 
            None
        )

@router.post("/place_pawn", response_model=Union[SuccessResponseModel, ErrorResponseModel])
def play_turn(move: MoveRequest):
    """Play a turn in a tic tac toe game. 
    """
    try:
        game_str = tic_tac_toe.play_turn(
            move.game_str, 
            move.pawn_type, 
            move.cell_number
        )

        if tic_tac_toe.get_game_status(game_str) is None :
            bot_pawn_type = PawnType.X if move.pawn_type == PawnType.O else PawnType.O
            game_str = bot.play(
                tic_tac_toe, 
                game_str, 
                bot_pawn_type
                )

        return success_response(
            game_str, 
            tic_tac_toe.get_game_status(game_str), 
            move.pawn_type
        )
    except ValueError as error :
        return error_response(str(error))


@router.get("/settings")
def get_settings():
    """Get the currents settings on which the game's based on"""
    config = dotenv_values(".env")
    return {k: v for k, v in config.items()}