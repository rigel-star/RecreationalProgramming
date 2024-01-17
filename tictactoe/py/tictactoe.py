import math 
import sys

sys.setrecursionlimit(1000000)

SCORES = {
    "X": 1,
    "O": -1,
    "tie": 0
}

def equals3(a, b, c):
    return a == b and b == c and a != '?'

def checkWinner(board):
    winner = None
    # check horizontally
    for i in range(3):
        if equals3(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]
    # check vertically
    for i in range(3):
        if equals3(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]

    # check diagonally
    if equals3(board[0][0], board[1][1], board[2][2]):
        winner = board[1][1]
    if equals3(board[0][2], board[1][1], board[2][0]):
        winner = board[1][1]

    openSlots = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '?': openSlots += 1

    if winner is None and openSlots == 0:
        return "tie"
    return winner

def minimax(board, alpha, beta, isMaxPlayer, turn):
    result = checkWinner(board)
    if result: return SCORES.get(result)
    if isMaxPlayer:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '?':
                    board[i][j] = turn
                    best_score = max(best_score, minimax(board, alpha, beta, False, "O"))
                    board[i][j] = '?' # undo the change
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '?':
                    board[i][j] = turn
                    best_score = min(best_score, minimax(board, alpha, beta, True, "X"))
                    board[i][j] = '?'
        return best_score

def print_grid(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print("\n")

def turn_computer(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '?':
                board[i][j] = "X"
                score = minimax(board, 0, 0, False, "O")
                board[i][j] = '?'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = "X"

def turn_human(board):
    while True:
        print("Place O in: ")
        x = int(input("X: "))
        y = int(input("Y: "))
        if x >= 0 or x < 3 or y >= 0 or y < 3:
            if board[x][y] == "?":
                board[x][y] = "O"
                break
            else:
                print("Invalid move. Place O in empty cell.")
        else:
            print(f"Invalid move. Index out of bounds: ({x}, {y})")

def main():
    board = [['?', '?', '?'], ['?', '?', '?'], ['?', '?', '?']]
    winner = None
    print_grid(board)
    while winner is None:
        turn_human(board)
        turn_computer(board)
        print_grid(board)
        winner = checkWinner(board)
    print()
    print_grid(board)

main()