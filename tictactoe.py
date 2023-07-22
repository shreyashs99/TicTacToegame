import random
 
print("Welcome to TicTacToe")
print("Let's play")

board =["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",]
currentPlayer = "X"
Winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#take player input
def playerInput(board):
    inp = int(input("Please enter a number 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in that spot!")

# check for win or tite
def checkHorizontle(board):
    global Winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner = board[6]
        return True
    
def checkRow(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner = board[3]
        return True
    
def checkDiag(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        Winner = board[2]
        return True


def checkWin(board):
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        printBoard(board)
        print(f"The Winner is {Winner}!")
        gameRunning = False
        exit()


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a Tie!")
        gameRunning = False
        


# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()



#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)






    

    