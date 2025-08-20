from pydantic import BaseModel

class MoveRequest(BaseModel):
    game_str: str
    pawn_type: str
    cell_number: int