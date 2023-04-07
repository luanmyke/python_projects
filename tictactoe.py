import random

# initialize game variables
board = ["-"] * 9
currentPlayer = "X"
gameRunning = True
winner = None

# function to print game board
def printBoard(board):
    fmtstr = '|'.join(board)
    fmtstr = '\n'.join(fmtstr[i:i+6] for i in range(0, len(fmtstr), 6))
    fmtstr = fmtstr[:5] + fmtstr[6:]
    fmtstr = fmtstr[:11] + fmtstr[12:]
    print(fmtstr)

# function for player to make a move
def playerMove(board):
    while True:
        ipn = int(input("Enter a number 1 - 9: ")) - 1
        if board[ipn] == "-":
            board[ipn] = currentPlayer
            break
        else:
            print("That spot is already taken. Try again.")

def switchPlayer(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else :
        currentPlayer = "X"

             
# heckWinHorizontal function
def checkWinHorizontal(board):
    if board[0] == board[1] == board[2] != "-":
        print(f"{currentPlayer} Won !")
        return True
    elif board[3] == board[4] == board[5] != "-" :
        print(f"{currentPlayer} Won !")
        return True
    elif board[6] == board[7] == board[8] != "-":
        print(f"{currentPlayer} Won !")
        return True
    else:
        return False

# checkIfWin function
def checkIfWin(board):
    global gameRunning
    if checkWinHorizontal(board):
        gameRunning = False

# main game loop
while gameRunning:
    printBoard(board)
    playerMove(board)
    checkIfWin(board)
    switchPlayer(board)
