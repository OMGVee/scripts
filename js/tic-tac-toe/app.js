const gameBoard = document.querySelector("#gameboard")
const info = document.querySelector("#info")
const startCells = ["", "", "", "", "", "", "", "", ""]
let go = 'cross'
info.textContent = go + " goes first"

function createBoard() {
    startCells.forEach((cell, index) => {
        const cellElement = document.createElement("div")
        cellElement.classList.add("square")
        cellElement.id = index
        cellElement.addEventListener('click', addGo)
        gameBoard.append(cellElement)
    })
}
createBoard()

function addGo(e) {
    const goDisplay = document.createElement('div')
    goDisplay.classList.add(go)
    e.target.append(goDisplay)
    go = go === 'cross'?'circle':'cross'
    info.textContent = go + "'s turn"
    e.target.removeEventListener('click', addGo)
    checkScore()
    console.log(e.target)
}

function checkScore() {
    const allSquares = document.querySelectorAll(".square")
    const winningCombos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    winningCombos.forEach(array=>{
        const crossWins = array.every(cell => allSquares[cell].firstChild?.classList.contains("cross"))
        if (crossWins) {
            info.textContent = "Cross Wins"
            allSquares.forEach(square => square.replaceWith(square.cloneNode(true)))
            return
        }
    })
    winningCombos.forEach(array=>{
        const circleWins = array.every(cell => allSquares[cell].firstChild?.classList.contains("circle"))
        if (circleWins) {
            info.textContent = "Circle Wins"
            allSquares.forEach(square => square.replaceWith(square.cloneNode(true)))
            return
        }
    })
}