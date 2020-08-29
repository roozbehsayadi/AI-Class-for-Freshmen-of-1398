
def create_empty_board(): 
    return [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]

def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(0, 3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == 'x':
                return +1
            if b[row][0] == 'o': 
                return -1
    # Checking for Columns for X or O victory.
    for col in range(0, 3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == 'x':
                return +1
            if b[0][col] == 'o':
                return -1
    # Checking for Diagonals for X or O victory.
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == 'x':
            return +1
        if b[0][0] == 'o':
            return -1
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == 'x':
            return +1
        if b[0][2] == 'o':
            return -1
    # Else if none of them have won then return 0
    return 0

def game_over(board):
    if evaluate(board) == 0:
        return False
    else:
        return True

def empty_cells(board):
    cells = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == '_':
                cells.append((x, y))
    return cells

def is_valid_move(x, y, board):
    if board[x][y] == '_':
        return True
    else:
        return False


if __name__ == "__main__":
    pass

# source: https://github.com/Cledersonbc/tic-tac-toe-minimax/blob/master/py_version/minimax.py
