def success_response(board, winner, played_pawn):
    """Create a reponse for successfull operation."""
    return {
        "code" : 200,
        "data": {
            "board": board,
            "winner": winner,
            "played_pawn": played_pawn
        }
    }

def error_response(error_message):
    """Create a reponse in case of error."""
    return {
        "code" : 400,
        "message" : error_message
    }