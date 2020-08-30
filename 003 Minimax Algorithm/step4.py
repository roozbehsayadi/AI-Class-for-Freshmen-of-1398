from random import choice
from time import sleep
from math import inf

human = "x"
computer = "o"


def create_empty_board():
    return [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(0, 3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == computer:
                return +1
            if b[row][0] == human:
                return -1
    # Checking for Columns for X or O victory.
    for col in range(0, 3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == computer:
                return +1
            if b[0][col] == human:
                return -1
    # Checking for Diagonals for X or O victory.
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == computer:
            return +1
        if b[0][0] == human:
            return -1
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == computer:
            return +1
        if b[0][2] == human:
            return -1
    # Else if none of them have won then return 0
    return 0


def game_over(board):
    # check if somebody wins or not
    if evaluate(board) == 0:
        return False
    else:
        return True


def empty_cells(board):
    cells = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == "_":
                cells.append((x, y))
    return cells


def is_valid_move(x, y, board):
    if board[x][y] == "_":
        return True
    else:
        return False


def set_move(x, y, board, player):
    if not is_valid_move(x, y, board):
        return False
    board[x][y] = player
    return True


def clear_screen():
    print("\x1b[H\x1b[2J\x1b[3J", end="")


def print_board(board):
    for row in board:
        print(row)


def player(board):
    print("enter x ,y for your move")
    x, y = input().split()
    x, y = int(x), int(y)
    if not set_move(x, y, board, player=human):
        # get input again
        player(board)


###############################################


def minimax(board, depth, is_computer):
    # return type: (x, y), optimum_score
    if depth == 0 or game_over(board):
        return (-1, -1), evaluate(board)

    player = computer if is_computer else human

    # setup minimum or maximum variable
    if is_computer:
        best = [(-1, -1), -inf]
    else:
        best = [(-1, -1), +inf]

    # explore all possible moves
    for x, y in empty_cells(board):

        # handle board copies
        board[x][y] = player
        _, score = minimax(board, depth - 1, not is_computer)
        board[x][y] = "_"  # revert board change

        # maximizer
        if is_computer and (score > best[1]):
            best = [(x, y), score]
        # minimizer
        if (not is_computer) and (score < best[1]):
            best = [(x, y), score]

    return best


def ai(board):
    print("ai is thinking")
    depth = len(empty_cells(board))
    (x, y), _ = minimax(board, depth, is_computer=True)
    set_move(x, y, board, player=computer)


if __name__ == "__main__":
    board = create_empty_board()
    player_turn = True
    while len(empty_cells(board)) > 0 and not game_over(board):
        # clear_screen()
        print_board(board)
        if player_turn:
            player(board)
        else:
            ai(board)
        player_turn = not player_turn

    print_board(board)
    result = evaluate(board)
    if result == +1:
        print("you lost")
    elif result == -1:
        print("you won")
    else:
        print("tie")

# source: https://github.com/Cledersonbc/tic-tac-toe-minimax/blob/master/py_version/minimax.py
