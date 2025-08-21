from dotenv import dotenv_values
from fastapi.testclient import TestClient

from API.main import app
from API.models.tic_tac_toe import EndStatus

from API.config import GRID_LENGTH

client = TestClient(app)

def test_new_game():
    response = client.get("/tic_tac_toe/new_game")
    assert response.status_code == 200
    assert response.json() == {
        "code" : 200,
        "data": {
            "board": ' ' * pow(GRID_LENGTH, 2),
            "winner": None,
            "played_pawn": None
        }
    }


def test_valid_place_pawn():
    response = client.post("/tic_tac_toe/place_pawn", json={
        "game_str": " XO OOX  ",
        "pawn_type": "X",
        "cell_number": 0
    })

    assert response.status_code == 200
    data = response.json()
    print(response.json())
    assert data["data"]["board"][0] == "X"
    assert data["data"]["played_pawn"] == "X"
    assert data["data"]["winner"] in [None] + [status.value for status in 
    EndStatus]

def test_invalid_move_on_other_pawn():
    response = client.post("/tic_tac_toe/place_pawn", json={
        "game_str": "XXXOOOXXX",
        "pawn_type": "O",
        "cell_number": 0
    })

    data = response.json()
    print(data)
    assert data["code"] == 400
    assert data["message"] == "The selected place isn't available !"

def test_out_of_bounds_cell():
    response = client.post("/tic_tac_toe/place_pawn", json={
        "game_str": "OXXOXOXOX",
        "pawn_type": "X",
        "cell_number": 10
    })
    assert response.status_code == 422

def test_invalid_pawn_type():
    response = client.post("/tic_tac_toe/place_pawn", json={
        "game_str": "XOO  OX X",
        "pawn_type": "Z",
        "cell_number": 0
    })
    assert response.status_code == 422


def test_get_settings():
    response = client.get("/tic_tac_toe/settings")
    assert response.status_code == 200
    config = dotenv_values(".env")
    assert response.json() == {k: v for k, v in config.items()}