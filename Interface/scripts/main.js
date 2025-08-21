const API_URL  = "http://127.0.0.1:8000/"
let playerSymbol = null;
let boardString = null;

const settings = {}

function getURLEndpoint(endpoint){
    return new URL(endpoint, API_URL);
}

function selectSymbol(symbol){
    playerSymbol = symbol

    document.getElementById('X-selector').style.display = "none";
    document.getElementById('O-selector').style.display = "none";
    document.getElementById('symbol-information').innerText = `You are the ${playerSymbol}`;

    fetchNewGame();
}

function restartGame() {
    document.getElementById('board').style.display = "none";
    document.getElementById('restart-button').style.display = "none";
    info_element = document.getElementById("status-information");
    info_element.classList = '';
    info_element.innerText = '';

    document.getElementById('symbol-information').innerText = "Choose the symbol you want to use by clicking on it";
    document.getElementById('X-selector').style.display = "inline-block";
    document.getElementById('O-selector').style.display = "inline-block";
}

async function fetchNewGame() {
  try {
    const response = await fetch(getURLEndpoint('tic_tac_toe/new_game'));
    const data = await response.json();

    document.getElementById('restart-button').style.display = "inline-block";
    document.getElementById('board').style.display = "block";

    boardString = data.data.board;
    renderBoard(boardString);
  } catch (error) {
    console.error("Failed to fetch new game:", error);
  }
}

function renderBoard(boardString) {
    const board = document.getElementById('board');
    board.innerHTML = '';
    const cells = boardString.split('');
    const size = Math.sqrt(cells.length);

    board.style.display = "grid";
    board.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
    board.style.width = `${size * 110 }px`;
    board.style.height = `${size * 110}px`;

    cells.forEach((value, index) => {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.textContent = value.trim();
        cell.dataset.index = index;
        cell.addEventListener('click', () => handleClick(index));
        board.appendChild(cell);
    });
}

function handleClick(index) {
    const cell = document.querySelector(`.cell[data-index="${index}"]`);
    info_element = document.getElementById("status-information")
    if (cell.textContent.trim() !== '') {
        info_element.innerText = "There's already a pawn there !";
        info_element.classList.add("error");
        return;
    };
    info_element.classList.remove("error");
    info_element.innerText = '';

    const moveRequest = {
        game_str: boardString,
        pawn_type: playerSymbol,
        cell_number: index
    };


    fetch(getURLEndpoint('tic_tac_toe/place_pawn'), {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(moveRequest)
    })
    .then(response => {
        if (!response.ok) {
            info_element.innerText = `An error has occured : code ${response.status}`;
            info_element.classList.add("error");
            throw new Error(`HTTP error code ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
       if (data.code == 200) {
            boardString = data.data.board
            renderBoard(boardString)
            if (data.data.winner != null){
                handleEndGame(data.data.winner);
            }
        }else{
            info_element.innerText = `An error has occured ${data.message} - code ${data.code}`;
            info_element.classList.add("error");
        }
    })
    .catch(err => {
        console.error("Erro catch : ", err.message);
    });
}

function handleEndGame(endStatus){
    console.log(endStatus);
    document.querySelectorAll('.cell').forEach(cell => {
    cell.classList.add('disabled');
    });
    if (endStatus[0] == playerSymbol){
        info_element.innerText = "You win, congrats !";
        info_element.classList.add("win");
    } else if (endStatus == "Draw"){
        info_element.innerText = "It's a draw, well played.";
        info_element.classList.add("draw");
    } else {
        info_element.innerText = "You lose, maybe next time.";
        info_element.classList.add("lose");
    }
}