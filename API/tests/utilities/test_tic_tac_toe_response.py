from API.utilities.tic_tac_toe_response import success_response, error_response

def test_success_response():
    board = "XOXOXO   "
    winner = "X"
    played_pawn = "X"

    result = success_response(board, winner, played_pawn)

    assert result["code"] == 200
    assert result["data"]["board"] == board
    assert result["data"]["winner"] == winner
    assert result["data"]["played_pawn"] == played_pawn

def test_error_response():
    error_msg = "Invalid move"

    result = error_response(error_msg)

    assert result["code"] == 400
    assert result["message"] == error_msg