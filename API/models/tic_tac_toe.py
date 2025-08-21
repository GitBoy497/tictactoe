from enum import Enum
from typing import Dict
from pydantic import BaseModel, conint, constr

from config import GRID_LENGTH

grid_str_size = pow(GRID_LENGTH,2)

class PawnType(str, Enum):
    X = "X"
    O = "O"

class MoveRequest(BaseModel):
    game_str: constr(min_length=grid_str_size, max_length=grid_str_size)
    pawn_type: PawnType
    cell_number: conint(ge=0, le=grid_str_size-1)

class EndStatus(str, Enum):
    DRAW = "Draw"
    X = "X wins"
    O = "O wins"

class GameData(BaseModel):
    board: str
    winner: EndStatus | None = None
    played_pawn: str | None = None

class SuccessResponseModel(BaseModel):
    code : int
    data : GameData

class ErrorResponseModel(BaseModel):
    code : int
    message : str