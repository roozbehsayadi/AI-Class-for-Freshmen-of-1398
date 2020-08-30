def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(0, 3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == 'x':
                return +1
            elif b[row][0] == 'o': 
                return -1
    # Checking for Columns for X or O victory.
    for col in range(0, 3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == 'x':
                return +1
            elif b[0][col] == 'o':
                return -1
    # Checking for Diagonals for X or O victory.
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == 'x':
            return +1
        elif b[0][0] == 'o':
            return -1
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == 'x':
            return +1
        elif b[0][2] == 'o':
            return -1
    # Else if none of them have won then return 0
    return 0

# Driver code
if __name__ == "__main__":
    board = [['x', '_', 'o'],
             ['_', '_', 'o'],
             ['o', '_', 'x']]
    value = evaluate(board)
    print("The value of this board is", value)
# source: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-2-evaluation-function
