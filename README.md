# tictactoe
microservice-based project aiming to build a flexible and extensible Tic Tac Toe game, with potential to evolve into a multi-game platform.

## 📖 Table of Contents
- [Game Rules](#-tic-tac-toe-rules)
- [Architecture Overview](#-services)
    - [API Reference](#-api)
    - [Interface](#️-interface)
- [Getting Started](#)

## 🎮 Tic Tac Toe Rules

Two players compete on a 3x3 grid with the goal of being the first to align three of their pawns horizontally, vertically, or diagonally.

### 🧩 Pawn Types

- One player uses the `X` pawn  
- The other player uses the `O` pawn

### 🔄 Turn-Based Gameplay

- Players take turns alternately  
- On each turn, a player places their symbol in an empty cell

### 🏁 End of the Game

- If a player aligns three of their pawns, they win  
- If all cells are filled and no player has aligned three pawns, the game ends in a draw

📚 *Source:* [Official Game Rules – Tic Tac Toe](https://officialgamerules.org/game-rules/tic-tac-toe/)

## 🧱 Services

This app uses a **microservices architecture**, allowing:
- Reusability of the API across different interfaces
- Easy integration of future mini-games

### 📡 API
Here you will find all the detailled information on the API service.

#### 🔗 Endpoints
The API allows you to :
- Create a new Tic Tac Toe game
- Play a turn in a current Tic Tac Toe game and inform you on the game status
- Get settings of a Tic Tac Toe game

For detailed information on each endpoint, including request/response formats refer to the `routes` and `models` folders.

#### 🧪 Test
To test the service, navigate to the `API/tests` directory and run the following command:  

*▶ PowerShell (Windows)*
```powershell
$env:PYTHONPATH = ".."
pytest -vv
```
*▶ Bash (Linux/macOS)*
```sh
PYTHONPATH=.. pytest -vv
```

### 🖥️ Interface
> _To be documented_: current UI, future plans (CLI, web, mobile, etc.)

## 🚀 Getting Started
In this section, you will find all you need to run the API smoothly and start playing with ease.

### ✅ Prerequisites

- Python **3.10** or higher

### 📦 Installation

Navigate to the root directory of the project and install dependencies:

```bash
pip install -r requirements.txt
```

### ▶️ Launch the API

Start the server using **Uvicorn**:
```sh
uvicorn main.py
```
The API will be accessible locally at `http://127.0.0.1:8000` by default.

### 🕹️ Play the game

Use the provided interface or connect your own frontend to interact with the API.

Enjoy ! 😉

## Contributors
<a href="https://github.com/GitBoy497"><img src="https://avatars.githubusercontent.com/u/80398114?v=4" title="FuriousSmasher" width="50" height="50"></a>
