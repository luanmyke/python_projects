import random

# initialize game variables
board = ["-"] * 9
currentPlayer = "X"
winner = None
gameRunning = True

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
        # ask for input from current player
        ipn = int(input("Enter a number 1 - 9: ")) - 1
        # check if selected spot is available
        if board[ipn] == "-":
            # update board with player's move
            board[ipn] = currentPlayer
            break
        else:
            print("That spot is already taken. Try again.")

# main game loop
while gameRunning :
    # print current state of game board
    printBoard(board)
    # ask current player to make a move
    playerMove(board)
