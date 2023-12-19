# Function 1 to draw the Tic Tac Toe board

def display_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--|---|--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--|---|--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

initial_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

display_board(initial_board)

def player_input(position)

position = int(input('choose position (1-9): '))
# board[0][position-1] = 'X'

marker =
while marker != "X" and marker != "0":
    marker = input("Player 1, do you to be X or O?")

    player1 = marker:
    if player1 == "X":
        player2 ="O"

    else player2 = "X"

return 
